#!/usr/bin/env python3
import sys
import subprocess
import os
import signal

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QLabel, QFormLayout, QLineEdit, QHBoxLayout, QCheckBox
)
from PySide6.QtCore import Qt

# ------------------------------------------------------------------
# CONFIG – adapt if needed
# ------------------------------------------------------------------
WORKSPACE_DIR = "/root/ur_ws_sim"
PACKAGE_NAME  = "my_ur10e_moveit_config"
LAUNCH_FILE   = "custom_rs.launch.py"

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
        # capture output so we see real ROS error
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
    """
    Runs in bash:

      cd /root/ur_ws_sim
      source /opt/ros/humble/setup.bash
      source /root/ur_ws_sim/install/setup.bash
      source /root/ur_ws_sim/install/hemi_motion_rs/share/hemi_motion_rs/local_setup.bash
      ros2 launch my_ur10e_moveit_config custom_rs.launch.py ...
    """
    global motion_proc

    # Only allow one launch at a time
    if motion_proc is not None and motion_proc.poll() is None:
        return False, "A motion is already running. Stop it first."

    launch_cmd = f"""
        cd {WORKSPACE_DIR} && \
        source {ROS_SETUP} && \
        source {WS_SETUP} && \
        source {HEMI_SETUP} && \
        ros2 launch {PACKAGE_NAME} {LAUNCH_FILE} \
            launch_rviz:={params['launch_rviz']} \
            run_id:={params['run_id']} \
            camera_name:={params['camera_name']} \
            hemi_radius:={params['hemi_radius']} \
            max_poses:={params['max_poses']} \
            hemi_num_latitudes:={params['hemi_num_latitudes']} \
            hemi_points_per_lat:={params['hemi_points_per_lat']}
    """

    try:
        motion_proc = subprocess.Popen(["bash", "-lc", launch_cmd])
        return True, None
    except Exception as e:
        return False, str(e)


def stop_motion():
    global motion_proc
    if motion_proc is not None and motion_proc.poll() is None:
        motion_proc.terminate()
        try:
            motion_proc.wait(timeout=5)
        except Exception:
            motion_proc.kill()
        motion_proc = None
        return True
    return False

class HemisphereGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hemisphere Motion (UR10e + Realsense)")

        # Dark style
        self.setStyleSheet("""
            QWidget {
                background-color: #1f232a;
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
        """)

        self.current_params: dict | None = None
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Hemisphere Motion Parameters")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title)

        form = QFormLayout()
        self.e_hemi_radius = QLineEdit("0.33")
        self.e_max_poses = QLineEdit("100")
        self.e_num_lat = QLineEdit("12")
        self.e_pts_lat = QLineEdit("20")
        self.e_run_id = QLineEdit("run_001")
        self.e_camera_name = QLineEdit("realsense")

        form.addRow("Hemisphere radius [m]:", self.e_hemi_radius)
        form.addRow("Max poses:", self.e_max_poses)
        form.addRow("Num latitudes:", self.e_num_lat)
        form.addRow("Points per latitude:", self.e_pts_lat)
        form.addRow("Run ID:", self.e_run_id)
        form.addRow("Camera name:", self.e_camera_name)
        layout.addLayout(form)

        self.cb_rviz = QCheckBox("Launch RViz")
        self.cb_rviz.setChecked(True)
        layout.addWidget(self.cb_rviz)

        # Buttons
        btn_layout = QHBoxLayout()
        self.apply_btn = QPushButton("Apply Changes")
        self.btn_start = QPushButton("Start")
        self.btn_stop = QPushButton("Stop")
        self.btn_home = QPushButton("Go to Home")  # no functionality

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
            "camera_name": self.e_camera_name.text(),
            "launch_rviz": "true" if self.cb_rviz.isChecked() else "false",
        }

    def on_apply(self):
        self.current_params = self._collect_params_from_ui()
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
            # Show full ROS error, but still ask if we should continue
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
                "custom_rs.launch.py started with applied hemisphere parameters.",
            )

    def on_stop(self):
        if stop_motion():
            QMessageBox.information(self, "Stopped", "Motion process terminated.")
            self.btn_start.setEnabled(True)
        else:
            QMessageBox.information(self, "Info", "No running motion process.")


def main():
    app = QApplication(sys.argv)
    gui = HemisphereGui()
    gui.resize(600, 280)
    gui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
