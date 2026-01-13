# motion_pages.py

import subprocess
from pathlib import Path

import importlib.util
import inspect
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QMessageBox, QStackedWidget,
    QLabel, QFormLayout, QLineEdit, QHBoxLayout
)
from PySide6.QtCore import Qt

PACKAGE_NAME = "calib_mtc"
LAUNCH_FILE = "calib_mtc_style.launch.py"

#YAML_PATH = Path("root/ur_ws_sim/src/calib_mtc/src/calib_mtc/params/motion_defaults.yaml")
YAML_PATH = Path("/root/ur_ws_sim/src/calib_mtc/src/calib_mtc/params/motion_defaults.yaml")


motion_proc = None  # global process handle


def load_yaml_dict():
    import yaml
    if not YAML_PATH.exists():
        return {"calib_mtc": {"ros__parameters": {}}}
    with open(YAML_PATH, "r") as f:
        return yaml.safe_load(f) or {"calib_mtc": {"ros__parameters": {}}}


def save_yaml_dict(data: dict):
    import yaml
    YAML_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(YAML_PATH, "w") as f:
        yaml.safe_dump(data, f, sort_keys=False)
    return True


def smart_set(params: dict, key: str, value: str):
    v = value.strip()
    if not v:
        return
    if v.startswith("[") and v.endswith("]"):
        params[key] = v
        return
    params[key] = v


def update_params_in_yaml(new_params: dict):
    data = load_yaml_dict()
    calib = data.setdefault("calib_mtc", {})
    ros_params = calib.setdefault("ros__parameters", {})
    for k, v in new_params.items():
        smart_set(ros_params, k, v)
    return save_yaml_dict(data)

def launch_node(node_name: str):
    global motion_proc
    try:
        if motion_proc is not None and motion_proc.poll() is None:
            return False, "A motion is already running. Stop it first."

        cmd = f"""
            source /opt/ros/humble/setup.bash && \
            source /root/ur_ws_sim/install/setup.bash && \
            ros2 launch {PACKAGE_NAME} {LAUNCH_FILE} node_name:={node_name}
        """

        motion_proc = subprocess.Popen(
            ["bash", "-lc", cmd],
            start_new_session=True
        )

        return True, None
    except Exception as e:
        return False, str(e)


"""
def launch_node(node_name: str):
    global motion_proc
    try:
        # Only allow one motion at a time
        if motion_proc is not None and motion_proc.poll() is None:
            return False, "A motion is already running. Stop it first."
        motion_proc = subprocess.Popen([
            "ros2", "launch", PACKAGE_NAME, LAUNCH_FILE,
            f"node_name:={node_name}"
        ])
        return True, None
    except Exception as e:
        return False, str(e)
"""

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
# ---------- Custom LineEdit with Scroll-to-Change Float ----------
class ScrollFloatLineEdit(QLineEdit):
    def __init__(self, step=0.1, parent=None):
        super().__init__(parent)
        self.step = step

    def wheelEvent(self, event):
        text = self.text().strip()
        if not text:
            # Empty → treat as 0.0
            value = 0.0
        else:
            try:
                value = float(text)
            except ValueError:
                # Not a valid float → ignore scroll (or call super to pass event on)
                event.ignore()
                return

        delta = event.angleDelta().y()

        if delta > 0:
            value += self.step      # scroll up → increase
        elif delta < 0:
            value -= self.step      # scroll down → decrease
        else:
            event.ignore()
            return

        # Avoid weird long floats
        value = round(value, 4)

        self.setText(str(value))
        event.accept()


class HemiPage(QWidget):
    def __init__(self, run_home, go_back, parent=None):
        super().__init__(parent)
        self.run_home_cb = run_home
        self.go_back_cb = go_back





        self.setStyleSheet("""
    QWidget {
        background-color: #1f232a;
        color: white;
    }

    /* --------- INPUT FIELDS --------- */
    QLineEdit {
        border: 0.5px solid white;
        border-radius: 6px;
        padding: 4px;
        background-color: #2a2f38;
        color: white;
    }

    /* --------- BUTTONS --------- */
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
        
        '''self.ed_radius = ScrollFloatLineEdit(step=0.1)

        # Num latitudes: integer-like, change by 1 per scroll
        self.ed_num_lat = ScrollFloatLineEdit(step=1.0)

        # Points per latitude: integer-like, change by 1 per scroll
        self.ed_pts_lat = ScrollFloatLineEdit(step=1.0)
        self.form.addRow("Center [x,y,z]:", self.ed_center)
        self.form.addRow("Radius:", self.ed_radius)
        self.form.addRow("Num latitudes:", self.ed_num_lat)
        self.form.addRow("Points per latitude:", self.ed_pts_lat)
        v.addLayout(self.form)

'''
        v = QVBoxLayout(self)
        v.setContentsMargins(10, 10, 10, 10)

        lbl = QLabel("<b>Hemisphere Motion</b>")
        lbl.setAlignment(Qt.AlignCenter)
        v.addWidget(lbl)

        self.form = QFormLayout()
        self.ed_center = QLineEdit()
        self.ed_radius = QLineEdit()
        self.ed_num_lat = QLineEdit()
        self.ed_pts_lat = QLineEdit()
        self.form.addRow("Center [x,y,z]:", self.ed_center)
        self.form.addRow("Radius:", self.ed_radius)
        self.form.addRow("Num latitudes:", self.ed_num_lat)
        self.form.addRow("Points per latitude:", self.ed_pts_lat)
        v.addLayout(self.form)

        btn_row = QHBoxLayout()
        self.apply_btn = QPushButton("Apply Changes")
        self.run_btn = QPushButton("Run")
        self.stop_btn = QPushButton("Stop")
        self.cont_btn = QPushButton("Continue")
        self.run_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.cont_btn.setEnabled(False)
        home_btn = QPushButton("Return to Home")
        back_btn = QPushButton("Back")
        btn_row.addWidget(self.apply_btn)
        btn_row.addWidget(self.run_btn)
        btn_row.addWidget(self.stop_btn)
        btn_row.addWidget(self.cont_btn)
        btn_row.addWidget(home_btn)
        btn_row.addWidget(back_btn)
        v.addLayout(btn_row)

        #self.setStyleSheet("background-color: #1f232a; color: white;")

        self.apply_btn.clicked.connect(self.apply_changes)
        self.run_btn.clicked.connect(self.run_motion)
        self.stop_btn.clicked.connect(self.stop_motion_btn)
        self.cont_btn.clicked.connect(self.continue_motion)
        home_btn.clicked.connect(self.run_home_cb)
        back_btn.clicked.connect(self.go_back_cb)

        self.load_from_yaml()

    def load_from_yaml(self):
        data = load_yaml_dict()
        params = data.get("calib_mtc", {}).get("ros__parameters", {})
        self.ed_center.setText(str(params.get("hemi_center_xyz", "[0.0, 0.0, 0.30]")))
        self.ed_radius.setText(str(params.get("hemi_radius", 0.33)))
        self.ed_num_lat.setText(str(params.get("hemi_num_latitudes", 20)))
        self.ed_pts_lat.setText(str(params.get("hemi_points_per_lat", 200)))

    def apply_changes(self):
        params = {
            "hemi_center_xyz": self.ed_center.text(),
            "hemi_radius": self.ed_radius.text(),
            "hemi_num_latitudes": self.ed_num_lat.text(),
            "hemi_points_per_lat": self.ed_pts_lat.text(),
        }
        if update_params_in_yaml(params):
            QMessageBox.information(self, "Saved", "Hemisphere parameters updated.")
            self.run_btn.setEnabled(True)
        else:
            QMessageBox.critical(self, "Error", "Failed to save YAML.")

    def run_motion(self):
        ok, err = launch_node("hemi_node")
        if ok:
            QMessageBox.information(self, "Launching", "Launched hemi_node")
            self.run_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.cont_btn.setEnabled(False)
        else:
            QMessageBox.critical(self, "Error", err or "Unknown error")

    def stop_motion_btn(self):
        if stop_motion():
            QMessageBox.information(self, "Stopped", "Motion stopped.")
            self.stop_btn.setEnabled(False)
            self.cont_btn.setEnabled(True)
        else:
            QMessageBox.warning(self, "Warning", "No motion running.")

    def continue_motion(self):
        self.run_btn.setEnabled(True)
        self.cont_btn.setEnabled(False)


class PlanarPage(QWidget):
    def __init__(self, run_home, go_back, parent=None):
        super().__init__(parent)
        self.run_home_cb = run_home
        self.go_back_cb = go_back

        self.setStyleSheet("""
    QWidget {
        background-color: #1f232a;
        color: white;
    }

    /* --------- INPUT FIELDS --------- */
    QLineEdit {
        border: 0.5px solid white;
        border-radius: 6px;
        padding: 4px;
        background-color: #2a2f38;
        color: white;
    }

    /* --------- BUTTONS --------- */
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

        v = QVBoxLayout(self)
        v.setContentsMargins(10, 10, 10, 10)

        lbl = QLabel("<b>Planar Motion</b>")
        lbl.setAlignment(Qt.AlignCenter)
        v.addWidget(lbl)

        self.form = QFormLayout()
        self.ed_center = QLineEdit()
        self.ed_width = QLineEdit()
        self.ed_length = QLineEdit()
        self.ed_rows = QLineEdit()
        self.ed_cols = QLineEdit()
        self.ed_safety = QLineEdit()

        self.form.addRow("Center [x,y,z]:", self.ed_center)
        self.form.addRow("Plane width:", self.ed_width)
        self.form.addRow("Plane length:", self.ed_length)
        self.form.addRow("Rows:", self.ed_rows)
        self.form.addRow("Cols:", self.ed_cols)
        self.form.addRow("Safety Z offset:", self.ed_safety)
        v.addLayout(self.form)

        btn_row = QHBoxLayout()
        self.apply_btn = QPushButton("Apply Changes")
        self.run_btn = QPushButton("Run")
        self.stop_btn = QPushButton("Stop")
        self.cont_btn = QPushButton("Continue")
        self.run_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.cont_btn.setEnabled(False)
        home_btn = QPushButton("Return to Home")
        back_btn = QPushButton("Back")
        btn_row.addWidget(self.apply_btn)
        btn_row.addWidget(self.run_btn)
        btn_row.addWidget(self.stop_btn)
        btn_row.addWidget(self.cont_btn)
        btn_row.addWidget(home_btn)
        btn_row.addWidget(back_btn)
        v.addLayout(btn_row)

        #self.setStyleSheet("background-color: #1f232a; color: white;")

        self.apply_btn.clicked.connect(self.apply_changes)
        self.run_btn.clicked.connect(self.run_motion)
        self.stop_btn.clicked.connect(self.stop_motion_btn)
        self.cont_btn.clicked.connect(self.continue_motion)
        home_btn.clicked.connect(self.run_home_cb)
        back_btn.clicked.connect(self.go_back_cb)

        self.load_from_yaml()

    def load_from_yaml(self):
        data = load_yaml_dict()
        params = data.get("calib_mtc", {}).get("ros__parameters", {})
        self.ed_center.setText(str(params.get("plane_center_xyz", "[0.0, 0.0, 0.40]")))
        self.ed_width.setText(str(params.get("plane_width", 0.40)))
        self.ed_length.setText(str(params.get("plane_length", 0.40)))
        self.ed_rows.setText(str(params.get("plane_rows", 5)))
        self.ed_cols.setText(str(params.get("plane_cols", 5)))
        self.ed_safety.setText(str(params.get("safety_z_offset", 0.0)))

    def apply_changes(self):
        params = {
            "plane_center_xyz": self.ed_center.text(),
            "plane_width": self.ed_width.text(),
            "plane_length": self.ed_length.text(),
            "plane_rows": self.ed_rows.text(),
            "plane_cols": self.ed_cols.text(),
            "safety_z_offset": self.ed_safety.text(),
        }
        if update_params_in_yaml(params):
            QMessageBox.information(self, "Saved", "Planar parameters updated.")
            self.run_btn.setEnabled(True)
        else:
            QMessageBox.critical(self, "Error", "Failed to save YAML.")

    def run_motion(self):
        ok, err = launch_node("planar_node")
        if ok:
            QMessageBox.information(self, "Launching", "Launched planar_node")
            self.run_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.cont_btn.setEnabled(False)
        else:
            QMessageBox.critical(self, "Error", err or "Unknown error")

    def stop_motion_btn(self):
        if stop_motion():
            QMessageBox.information(self, "Stopped", "Motion stopped.")
            self.stop_btn.setEnabled(False)
            self.cont_btn.setEnabled(True)
        else:
            QMessageBox.warning(self, "Warning", "No motion running.")

    def continue_motion(self):
        self.run_btn.setEnabled(True)
        self.cont_btn.setEnabled(False)



class InfinityPage(QWidget):
    def __init__(self, run_home, go_back, parent=None):
        super().__init__(parent)
        self.run_home_cb = run_home
        self.go_back_cb = go_back
        self.setStyleSheet("""
    QWidget {
        background-color: #1f232a;
        color: white;
    }

    /* --------- INPUT FIELDS --------- */
    QLineEdit {
        border: 0.5px solid white;
        border-radius: 6px;
        padding: 4px;
        background-color: #2a2f38;
        color: white;
    }

    /* --------- BUTTONS --------- */
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
        v = QVBoxLayout(self)
        lbl = QLabel("<b>Infinity Motion</b>")
        lbl.setAlignment(Qt.AlignCenter)
        v.addWidget(lbl)

        self.form = QFormLayout()
        self.ed_center = QLineEdit()
        self.ed_width = QLineEdit()
        self.ed_height = QLineEdit()
        self.ed_points = QLineEdit()
        # New controls to tune collision/retry behavior
        self.ed_safety = QLineEdit()
        self.ed_max_retries = QLineEdit()
        self.ed_retry_inc = QLineEdit()

        self.form.addRow("Center [x,y,z]:", self.ed_center)
        self.form.addRow("Infinity width:", self.ed_width)
        self.form.addRow("Infinity height:", self.ed_height)
        self.form.addRow("Number of points:", self.ed_points)
        self.form.addRow("Safety Z offset:", self.ed_safety)
        self.form.addRow("Max retries:", self.ed_max_retries)
        self.form.addRow("Retry Z increment:", self.ed_retry_inc)
        v.addLayout(self.form)

        btn_row = QHBoxLayout()
        self.apply_btn = QPushButton("Apply Changes")
        self.run_btn = QPushButton("Run")
        self.stop_btn = QPushButton("Stop")
        self.cont_btn = QPushButton("Continue")
        self.run_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.cont_btn.setEnabled(False)
        home_btn = QPushButton("Return to Home")
        back_btn = QPushButton("Back")
        btn_row.addWidget(self.apply_btn)
        btn_row.addWidget(self.run_btn)
        btn_row.addWidget(self.stop_btn)
        btn_row.addWidget(self.cont_btn)
        btn_row.addWidget(home_btn)
        btn_row.addWidget(back_btn)
        v.addLayout(btn_row)

        self.apply_btn.clicked.connect(self.apply_changes)
        self.run_btn.clicked.connect(self.run_motion)
        self.stop_btn.clicked.connect(self.stop_motion)
        self.cont_btn.clicked.connect(self.continue_motion)
        home_btn.clicked.connect(self.run_home_cb)
        back_btn.clicked.connect(self.go_back_cb)

        self.load_from_yaml()

    def load_from_yaml(self):
        data = load_yaml_dict()
        params = data.get("calib_mtc", {}).get("ros__parameters", {})
        self.ed_center.setText(str(params.get("infinity_center_xyz", "[0.0, 0.0, 0.60]")))
        self.ed_width.setText(str(params.get("infinity_width", 0.40)))
        self.ed_height.setText(str(params.get("infinity_height", 0.20)))
        self.ed_points.setText(str(params.get("infinity_points", 200)))
        # load new params (if present)
        self.ed_safety.setText(str(params.get("safety_z_offset", 0.0)))
        self.ed_max_retries.setText(str(params.get("infinity_max_retries", 4)))
        self.ed_retry_inc.setText(str(params.get("infinity_retry_z_increment", 0.02)))

    def apply_changes(self):
        params = {
            "infinity_center_xyz": self.ed_center.text(),
            "infinity_width": self.ed_width.text(),
            "infinity_height": self.ed_height.text(),
            "infinity_points": self.ed_points.text(),
            "safety_z_offset": self.ed_safety.text(),
            "infinity_max_retries": self.ed_max_retries.text(),
            "infinity_retry_z_increment": self.ed_retry_inc.text(),
        }
        if update_params_in_yaml(params):
            QMessageBox.information(self, "Saved", "Infinity parameters updated.")
            self.run_btn.setEnabled(True)
        else:
            QMessageBox.critical(self, "Error", "Failed to save YAML.")

    def run_motion(self):
        ok, err = launch_node("infinity_node")
        if ok:
            QMessageBox.information(self, "Launching", "Launched infinity_node")
            self.run_btn.setEnabled(False)
            self.stop_btn.setEnabled(True)
            self.cont_btn.setEnabled(False)
        else:
            QMessageBox.critical(self, "Error", err or "Unknown error")

    def stop_motion(self):
        if stop_motion():
            QMessageBox.information(self, "Stopped", "Motion stopped.")
            self.stop_btn.setEnabled(False)
            self.cont_btn.setEnabled(True)
        else:
            QMessageBox.warning(self, "Warning", "No motion running.")

    def continue_motion(self):
        self.run_btn.setEnabled(True)
        self.cont_btn.setEnabled(False)
