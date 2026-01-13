#!/usr/bin/env python3
import sys
import subprocess
import os
import signal
import time
import glob, os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QLabel, QFormLayout, QLineEdit, QHBoxLayout, QCheckBox
)
from PySide6.QtCore import Qt
import subprocess
import re
import subprocess
import shlex
# ------------------------------------------------------------------
# CONFIG – adapt if needed
# ------------------------------------------------------------------
WORKSPACE_DIR = "/root/ur_ws_sim"
PACKAGE_NAME  = "my_ur10e_moveit_config"
#LAUNCH_FILE   = "custom_rs_webcam.launch.py"   # <-- combined launch
# motion_page.py

LAUNCH_RS_ONLY   = "custom_rs.launch.py"         # <-- create / use this
LAUNCH_RS_WEBCAM = "custom_rs_webcam.launch.py"  # <-- your current one
LAUNCH_ZED_RS_WEBCAM = "custom_zed_rs_webcam.launch.py"

ROS_SETUP  = "/opt/ros/humble/setup.bash"
WS_SETUP   = "/root/ur_ws_sim/install/setup.bash"
HEMI_SETUP = "/root/ur_ws_sim/install/hemi_motion_rs/share/hemi_motion_rs/local_setup.bash"
# ------------------------------------------------------------------

motion_proc: subprocess.Popen | None = None  # global Popen handle


def switch_controllers():
    """
    Runs in bash:

      cd /root/ur_ws_sim
      source /opt/ros/humble/setup.bash
      source /root/ur_ws_sim/install/setup.bash
      source /root/ur_ws_sim/install/hemi_motion_rs/share/hemi_motion_rs/local_setup.bash
      ros2 control switch_controllers \
          --activate scaled_joint_trajectory_controller \
          --strict \
          --start-asap
    Returns (ok: bool, msg: str) where msg contains stdout+stderr on failure.
    """
    cmd = f"""
        cd {WORKSPACE_DIR} && \
        source {ROS_SETUP} && \
        source {WS_SETUP} && \
        source {HEMI_SETUP} && \
        ros2 control switch_controllers \
            --activate scaled_joint_trajectory_controller \
            --strict \
            --start-asap || true
    """

    try:
        result = subprocess.run(
            ["bash", "-lc", cmd],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            msg = (
                "ros2 control switch_controllers failed\n\n"
                f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}"
            )
            return False, msg
        return True, "Controller switch OK"
    except Exception as e:
        return False, f"Exception while switching controllers: {e}"
    
    
def launch_motion(params: dict):
    global motion_proc

    if motion_proc is not None and motion_proc.poll() is None:
        return False, "A motion is already running. Stop it first."

    use_zed_left  = bool(params.get("use_zed_left"))
    use_zed_right = bool(params.get("use_zed_right"))
    use_any_zed   = use_zed_left or use_zed_right
    use_realsense = bool(params.get("use_realsense"))
    use_webcam    = bool(params.get("use_webcam"))

    if (not use_any_zed) and (not use_realsense) and (not use_webcam):
        return False, "Enable at least one camera (ZED left/right and/or RealSense and/or Webcam)."

    # Choose launch file:
    # - If any ZED is enabled -> use multi-cam launch (custom_zed_rs_webcam.launch.py)
    # - Otherwise fall back to your RS-only / RS+webcam launch files
    if use_realsense and not use_webcam and not use_any_zed:
        launch_file = LAUNCH_RS_ONLY if use_webcam else LAUNCH_RS_ONLY
        use_multicam = False
    elif use_any_zed or use_realsense or use_webcam:
        launch_file = LAUNCH_ZED_RS_WEBCAM
        use_multicam = True


    # Common args (motion + rviz)
    args = [
        f"launch_rviz:={params['launch_rviz']}",
        f"run_id:={params['run_id']}",
        f"hemi_radius:={params['hemi_radius']}",
        f"max_poses:={params['max_poses']}",
        f"hemi_num_latitudes:={params['hemi_num_latitudes']}",
        f"hemi_points_per_lat:={params['hemi_points_per_lat']}",
    ]

    # -----------------------------
    # Multi-cam launch (ZED_RS_WEBCAM)
    # -----------------------------
    if use_multicam:
        camera_names = []
        image_topics = []

        # ZED left/right independently
        if use_zed_left:
            camera_names.append("zed_left_raw")
            image_topics.append("/zed/zed_node/left/color/raw/image")

        if use_zed_right:
            camera_names.append("zed_right_raw")
            image_topics.append("/zed/zed_node/right/color/raw/image")

        # RealSense (DO NOT CHANGE these parts)
        if use_realsense:
            camera_names.append("realsense")
            image_topics.append("/camera/camera/color/image_raw")

        # Webcam
        if use_webcam:
            camera_names.append("webcam")
            image_topics.append("/webcam/image_raw")

        # Driver launch flags
        args.append(f"launch_zed:={'true' if use_any_zed else 'false'}")
        args.append(f"launch_realsense:={'true' if use_realsense else 'false'}")
        args.append(f"launch_webcam:={'true' if use_webcam else 'false'}")

        # Match your CLI delays (these must exist as declared launch args in the .launch.py)
        args.append("other_cams_start_delay:=3.0")
        args.append("motion_start_delay:=7.0")

        # Webcam device (only if webcam enabled)
        if use_webcam:
            args.append(f"webcam_device:={params['webcam_device']}")

        # IMPORTANT: format exactly like your CLI: "['a','b']"
        # repr(list) produces "['a', 'b']" with spaces; we remove spaces after commas.
        cam_list_str = repr(camera_names).replace(", ", ",")
        topic_list_str = repr(image_topics).replace(", ", ",")

        args.append(f"camera_names:=\"{cam_list_str}\"")
        args.append(f"image_topics:=\"{topic_list_str}\"")

    # --------------------------------
    # RS-only / RS+webcam launch path
    # --------------------------------
    else:
        if use_realsense:
            # keep RS behavior untouched (your launch files may use camera_name)
            args.append("camera_name:=realsense")

        if use_webcam:
            # match your RS+webcam launch args
            args.append("webcam_camera_name:=webcam")
            args.append(f"webcam_device:={params['webcam_device']}")

    args_str = " \\\n            ".join(args)

    launch_cmd = f"""
        cd {WORKSPACE_DIR} && \
        source {ROS_SETUP} && \
        source {WS_SETUP} && \
        source {HEMI_SETUP} && \
        ros2 launch {PACKAGE_NAME} {launch_file} \
            {args_str}
    """

    try:
        motion_proc = subprocess.Popen(["bash", "-lc", launch_cmd], start_new_session=True)
        return True, None
    except Exception as e:
        return False, str(e)



def _stop_realsense_fallback():
    # 1) Try to find and kill the realsense process
    # pkill returns 0 if it killed something, 1 if nothing matched
    subprocess.run(["pkill", "-INT", "-f", "realsense2_camera_node"], check=False)
    subprocess.run(["pkill", "-TERM", "-f", "realsense2_camera_node"], check=False)

    # Also catch rs_launch / realsense launch wrappers if used
    subprocess.run(["pkill", "-INT", "-f", "realsense2_camera"], check=False)
    subprocess.run(["pkill", "-TERM", "-f", "realsense2_camera"], check=False)



def stop_motion():
    global motion_proc

    # If nothing running, still try stopping realsense just in case
    if motion_proc is None or motion_proc.poll() is not None:
        motion_proc = None
        _stop_realsense_fallback()
        return False

    pgid = motion_proc.pid  # because start_new_session=True

    # 1) Ctrl+C (SIGINT)
    try:
        os.killpg(pgid, signal.SIGINT)
    except ProcessLookupError:
        motion_proc = None
        _stop_realsense_fallback()
        return True

    for _ in range(30):
        if motion_proc.poll() is not None:
            motion_proc = None
            _stop_realsense_fallback()
            return True
        time.sleep(0.1)

    # 2) SIGTERM
    try:
        os.killpg(pgid, signal.SIGTERM)
    except ProcessLookupError:
        motion_proc = None
        _stop_realsense_fallback()
        return True

    for _ in range(20):
        if motion_proc.poll() is not None:
            motion_proc = None
            _stop_realsense_fallback()
            return True
        time.sleep(0.1)

    # 3) SIGKILL
    try:
        os.killpg(pgid, signal.SIGKILL)
    except ProcessLookupError:
        pass

    motion_proc = None
    _stop_realsense_fallback()
    return True


class HemiPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Hemisphere Motion (UR10e + Cameras)")

        # Dark style
        self.setStyleSheet("""
            QWidget {
                background-color: #1a1a1a;
                color: white;
            }

            QLineEdit {
                border: 0.5px solid white;
                border-radius: 6px;
                padding: 4px;
                background-color: #2a2f38;
                color: white;
            }

            QPushButton {
                border: 0.5px solid white;
                border-radius: 6px;
                padding: 6px 10px;
                background-color: #2a2f38;
                color: white;
            }

            QPushButton:hover {
                background-color: #3a3f48;
            }

            QPushButton:pressed {
                background-color: #454b55;
            }

            QPushButton:disabled {
                border: 0.5px solid #777;
                color: #777;
                background-color: #2a2f38;
            }

            QCheckBox {
                spacing: 8px;
            }
        """)

        self.current_params: dict | None = None
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Hemisphere Motion Parameters")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        # ---------- helper (can also be global) ----------
        def detect_webcam_device(match="046d:081b"):
            try:
                out = subprocess.check_output(["v4l2-ctl", "--list-devices"], text=True)
            except Exception:
                return None

            blocks = out.strip().split("\n\n")
            for block in blocks:
                if match.lower() in block.lower():
                    m = re.search(r"(/dev/video\d+)", block)
                    if m:
                        return m.group(1)
            return None

        # ---------- form ----------
        form = QFormLayout()

        # Motion params
        self.e_hemi_radius = QLineEdit("0.33")
        self.e_max_poses = QLineEdit("100")
        self.e_num_lat = QLineEdit("12")
        self.e_pts_lat = QLineEdit("20")
        self.e_run_id = QLineEdit("run_001")

        # RealSense
        self.e_camera_name = QLineEdit("realsense")

        # Webcam (CREATE FIRST)
        self.e_webcam_camera_name = QLineEdit("webcam")
        self.e_webcam_device = QLineEdit("")

        device = detect_webcam_device("046d:081b")
        self.e_webcam_device.setText(device if device else "Not found")

        # Add rows AFTER creation
        form.addRow("Hemisphere radius [m]:", self.e_hemi_radius)
        form.addRow("Max poses:", self.e_max_poses)
        form.addRow("Num latitudes:", self.e_num_lat)
        form.addRow("Points per latitude:", self.e_pts_lat)
        form.addRow("Run ID:", self.e_run_id)
        #form.addRow("RealSense camera name:", self.e_camera_name)
        #form.addRow("Webcam camera name:", self.e_webcam_camera_name)
        form.addRow("Webcam device:", self.e_webcam_device)
        

        layout.addLayout(form)

        # ---------- checkboxes ----------
        self.cb_use_realsense = QCheckBox("Enable Intel RealSense")
        self.cb_use_realsense.setChecked(True)
        layout.addWidget(self.cb_use_realsense)

        self.cb_use_webcam = QCheckBox("Enable Webcam")
        self.cb_use_webcam.setChecked(False)
        layout.addWidget(self.cb_use_webcam)
        self.cb_use_zed_left = QCheckBox("Enable ZED Left")
        self.cb_use_zed_left.setChecked(False)
        layout.addWidget(self.cb_use_zed_left)

        self.cb_use_zed_right = QCheckBox("Enable ZED Right")
        self.cb_use_zed_right.setChecked(False)
        layout.addWidget(self.cb_use_zed_right)

        def _toggle_webcam_fields():
            enabled = self.cb_use_webcam.isChecked()
            self.e_webcam_camera_name.setEnabled(enabled)
            self.e_webcam_device.setEnabled(enabled)

            if enabled:
                device = detect_webcam_device("046d:081b")
                if device:
                    self.e_webcam_device.setText(device)

        self.cb_use_webcam.stateChanged.connect(_toggle_webcam_fields)
        _toggle_webcam_fields()

        self.cb_rviz = QCheckBox("Launch RViz")
        self.cb_rviz.setChecked(True)
        layout.addWidget(self.cb_rviz)


        # ---------- buttons ----------
        btn_layout = QHBoxLayout()
        self.apply_btn = QPushButton("Apply Changes")
        self.btn_start = QPushButton("Start")
        self.btn_stop = QPushButton("Stop")
        self.btn_home = QPushButton("Go to Home")

        self.apply_btn.clicked.connect(self.on_apply)
        self.btn_start.clicked.connect(self.on_start)
        self.btn_stop.clicked.connect(self.on_stop)

        btn_layout.addWidget(self.apply_btn)
        btn_layout.addWidget(self.btn_start)
        btn_layout.addWidget(self.btn_stop)
        btn_layout.addWidget(self.btn_home)
        layout.addLayout(btn_layout)

        layout.addStretch(1)

        
    def _collect_params_from_ui(self) -> dict:
        return {
            "hemi_radius": self.e_hemi_radius.text(),
            "max_poses": self.e_max_poses.text(),
            "hemi_num_latitudes": self.e_num_lat.text(),
            "hemi_points_per_lat": self.e_pts_lat.text(),
            "run_id": self.e_run_id.text(),
            "launch_rviz": "true" if self.cb_rviz.isChecked() else "false",

            # ZED sides
            "use_zed_left": self.cb_use_zed_left.isChecked(),
            "use_zed_right": self.cb_use_zed_right.isChecked(),

            # RealSense
            "use_realsense": self.cb_use_realsense.isChecked(),
            "camera_name": "realsense",  # locked

            # Webcam
            "use_webcam": self.cb_use_webcam.isChecked(),
            "webcam_camera_name": "webcam",  # locked
            "webcam_device": self.e_webcam_device.text(),
        }


    def on_apply(self):
        self.current_params = self._collect_params_from_ui()
        print("[HemiPage] Apply pressed. self id =", id(self), "current_params =", self.current_params)
        QMessageBox.information(
            self,
            "Parameters saved",
            "Parameters have been saved.\nPress 'Start' to run with these values.",
        )

    def on_start(self):
        self.btn_start.setEnabled(False)

        if self.current_params is None:
            QMessageBox.warning(
                self,
                "No parameters applied",
                "Please press 'Apply Changes' before starting the motion.",
            )
            self.btn_start.setEnabled(True)
            return

        # 1) Try to switch controllers
        ok, msg = switch_controllers()
        if not ok:
            res = QMessageBox.question(
                self,
                "Controller switch failed",
                f"{msg}\n\nContinue and launch motion anyway?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if res == QMessageBox.No:
                self.btn_start.setEnabled(True)
                return

        # 2) Launch motion
        ok, err = launch_motion(self.current_params)
        if not ok:
            QMessageBox.critical(self, "Error", f"Could not start motion:\n{err}")
            self.btn_start.setEnabled(True)
        else:
            QMessageBox.information(
                self,
                "Started",
                f"{LAUNCH_FILE} started with applied parameters.",
            )

    def on_stop(self):
        if stop_motion():
            QMessageBox.information(self, "Stopped", "Motion process terminated.")
            self.btn_start.setEnabled(True)
        else:
            QMessageBox.information(self, "Info", "No running motion process.")

