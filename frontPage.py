from PySide6.QtWidgets import QMainWindow, QMenu,QWidget, QMessageBox, QLineEdit, QInputDialog, QTextEdit, QVBoxLayout, QDialog, QLabel, QHBoxLayout, QComboBox, QPushButton,QStackedWidget,  QSizePolicy, QPlainTextEdit,QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QStackedWidget,QLabel, QFormLayout, QLineEdit, QHBoxLayout
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTreeView, QFileSystemModel,
    QMenu, QMessageBox )
from PySide6.QtCore import QTimer, Qt,  QProcess
from PySide6.QtGui import QImage, QPixmap , QTextCursor, QFont
from PySide6.QtWidgets import QScrollArea, QGridLayout

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QFileSystemModel, QTreeView,
    QMenu, QMessageBox
)

from PySide6.QtCore import QObject, Signal, Slot, QThread, Qt
from PySide6.QtWidgets import QWidget, QMessageBox, QLabel
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices


from PySide6.QtCore import Qt, QThread, Slot
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QProgressBar, QSizePolicy
from PySide6.QtGui import QFontMetrics

from PySide6.QtCore import QObject, Signal, Slot, Qt, QThread
from PySide6.QtWidgets import QWidget, QLabel, QMessageBox

from PySide6.QtCore import QObject, Signal, Slot, Qt, QThread
from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import (
    QWidget, QLabel, QProgressBar, QHBoxLayout, QSizePolicy,
    QMessageBox
)


import cv2
#import pyrealsense2 as rs
#from Real_Sense_Sensor_Widget import RealSenseSensorWidget
from PySide6.QtCore import QTimer
from ui_pro import Ui_MainWindow
from connect_arm_widget import Ui_Form
from intel_realsense_ui import Ui_Form_2
from motion_pages import HemiPage
from pathlib import Path


import importlib.util
import inspect
from sim_test import HemiPage, PlanarPage, launch_node,InfinityPage


from calibration_ui import calibrate_form 
import re
import time
from PySide6.QtCore import QSize
from calibration_ui import calibrate_form
from PySide6.QtCore import QTimer, QSize
from PySide6.QtWidgets import (
    QWidget, QPushButton, QMessageBox, QInputDialog,
    QLineEdit, QDialog
)

import shutil

import os, sys, shlex, subprocess, traceback, time, signal
from PySide6.QtCore import QObject, Signal, Slot
import shlex


import glob
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap





PACKAGE_NAME = "calib_mtc"
LAUNCH_FILE = "calib_mtc_style.launch.py"
#SOURCE_PDF = Path("/root/ur_ws_sim/data/run_001/results/multi_sensor_report.pdf")
RESULTS_DIR = Path("/root/GUI/Result")

YAML_PATH = Path("/root/calib_mtc/src/calib_mtc/params/motion_defaults.yaml")

# --- Add global process handle ---
motion_proc = None
proc = None




class ResultExplorerWidget(QWidget):
    def __init__(self, base_dir: str, params: dict, parent=None):
        super().__init__(parent)
        self.base_dir = base_dir
        self.params = params

        # Ensure the folder exists
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        
        title = QLabel("Calibration Results")
        title.setStyleSheet("""
            QLabel {
                background-color: #1a1a1a;
                color: white;
                padding: 6px;
                border-radius: 6px;
            }
        """)
        layout.addWidget(title)

        # Model
        self.model = QFileSystemModel(self)
        self.model.setRootPath(str(RESULTS_DIR))
        self.model.setNameFilters(["*.pdf"])
        self.model.setNameFilterDisables(False)
        self.model.setReadOnly(False)

        # View
        self.view = QTreeView(self)
        self.view.setModel(self.model)
        self.view.setRootIndex(self.model.index(str(RESULTS_DIR)))
        self.view.setSelectionBehavior(QTreeView.SelectionBehavior.SelectRows)
        self.view.setAlternatingRowColors(True)
        self.view.setSortingEnabled(True)
        self.view.sortByColumn(0, Qt.SortOrder.AscendingOrder)
        self.view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                # ✅ ADD THIS HERE
        self.view.setStyleSheet("""
            QTreeView {
                background-color: #242424;
                color: white;
                alternate-background-color: #2a2a2a;
                selection-background-color: #1a1a1a;
                selection-color: white;
                outline: 0;
            }

            QTreeView::item:selected {
                background-color: #1a1a1a;
                color: white;
            }

            QTreeView::item:selected:!active {
                background-color: #1a1a1a;
                color: white;
            }

            QTreeView::item:hover {
                background-color: #2e2e2e;
            }
        """)
        self.view.setColumnWidth(0, 260)
        self.view.setColumnHidden(2, True)  # hide file type/size column (optional)

        layout.addWidget(self.view)

        # Signals
        self.view.doubleClicked.connect(self.open_item)
        self.view.customContextMenuRequested.connect(self.show_context_menu)

    def refresh(self):
        """Forces model/view to update if new files were copied in."""
        self.model.setRootPath(str(RESULTS_DIR))
        self.view.setRootIndex(self.model.index(str(RESULTS_DIR)))

    def _path_from_index(self, index):
        if not index.isValid():
            return None
        return Path(self.model.filePath(index))

    def open_item(self, index):
        path = self._path_from_index(index)
        if path and path.is_file():
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))

    def show_context_menu(self, pos):
        index = self.view.indexAt(pos)
        path = self._path_from_index(index)

        if not path or not path.exists():
            return

        menu = QMenu(self)
        open_act = menu.addAction("Open")
        open_folder_act = menu.addAction("Open Containing Folder")
        rename_act = menu.addAction("Rename")
        delete_act = menu.addAction("Delete")

        action = menu.exec_(self.view.viewport().mapToGlobal(pos))

        if action == open_act:
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))

        elif action == open_folder_act:
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(path.parent)))

        elif action == rename_act:
            self.view.edit(index)

        elif action == delete_act:
            reply = QMessageBox.question(
                self,
                "Delete Result",
                f"Delete '{path.name}'?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.model.remove(index)




class CameraPortDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Camera Port")
        self.setMinimumWidth(400)
        self.setContentsMargins(0, 0, 0, 0)
 


# from your_ui_file import Ui_Form_2  # keep your existing UI class

class CameraMonitorWidget(QWidget):
    """
    Reuses Ui_Form_2 with a tabWidget.
    Automatically shows tabs based on hemi_page.current_params:
      - run_id
      - use_realsense
      - use_webcam
    """
    def __init__(self, hemi_page, parent=None):
        super().__init__(parent)
        self.hemi_page = hemi_page

        self.ui = Ui_Form_2()
        self.ui.setupUi(self)

        # Disable buttons you said are not needed
        if hasattr(self.ui, "pushButton"):   # select/add
            self.ui.pushButton.setEnabled(False)
            self.ui.pushButton.hide()
        if hasattr(self.ui, "pushButton_2"): # clear
            self.ui.pushButton_2.setEnabled(False)
            self.ui.pushButton_2.hide()

        self.ui.tabWidget.setTabsClosable(False)

        # start empty
        while self.ui.tabWidget.count() > 0:
            self.ui.tabWidget.removeTab(0)

        # Poll params and update UI if run_id / toggles change
        self._last_key = None
        self._poll = QTimer(self)
        self._poll.timeout.connect(self.refresh_from_params)
        self._poll.start(500)  # check twice per second

        self.refresh_from_params()

    def _read_params(self):
        params = getattr(self.hemi_page, "current_params", None) or {}
        run_id = str(params.get("run_id", "")).strip()         # e.g. "run_003"
        use_rs = bool(params.get("use_realsense", False))
        use_wc = bool(params.get("use_webcam", False))
        use_zed_left = bool(params.get("use_zed_left", False))
        use_zed_right = bool(params.get("use_zed_right", False))
        return run_id, use_rs, use_wc, use_zed_left, use_zed_right

    def _clear_tabs(self):
        while self.ui.tabWidget.count() > 0:
            w = self.ui.tabWidget.widget(0)
            self.ui.tabWidget.removeTab(0)
            if w is not None:
                w.deleteLater()

    def refresh_from_params(self):
        run_id, use_rs, use_wc, use_zed_left, use_zed_right = self._read_params()
        key = (run_id, use_rs, use_wc, use_zed_left, use_zed_right)

        if key == self._last_key:
            return
        self._last_key = key

        self._clear_tabs()

        if not run_id:
            # show one informative tab
            info = QWidget()
            info.setStyleSheet("background:#111;")
            lay = QVBoxLayout(info)
            lbl = QLabel("No Run ID set.\nGo to Connect Arm → set Run ID → Apply Changes.")
            lbl.setStyleSheet("color:white; font-size:16px;")
            lbl.setAlignment(Qt.AlignCenter)
            lay.addWidget(lbl)
            self.ui.tabWidget.addTab(info, "Info")
            return

        if not (use_rs or use_wc or use_zed_right or use_zed_left):
            info = QWidget()
            info.setStyleSheet("background:#111;")
            lay = QVBoxLayout(info)
            lbl = QLabel(f"{run_id} selected.\nNo cameras enabled.\nEnable RealSense and/or Webcam and/or zed in Connect Arm → Apply Changes.")
            lbl.setStyleSheet("color:white; font-size:16px;")
            lbl.setAlignment(Qt.AlignCenter)
            lay.addWidget(lbl)
            self.ui.tabWidget.addTab(info, "Info")
            return

        base = f"/root/ur_ws_sim/data/{run_id}/images"

        if use_rs:
            rs_folder = os.path.join(base, "realsense")
            rs_view = FolderImageViewer(rs_folder, title=f"{run_id} — RealSense", poll_ms=200)
            self.ui.tabWidget.addTab(rs_view, "RealSense")

        if use_wc:
            wc_folder = os.path.join(base, "webcam")
            wc_view = FolderImageViewer(wc_folder, title=f"{run_id} — Webcam", poll_ms=200)
            self.ui.tabWidget.addTab(wc_view, "Webcam")

        if use_zed_left:
            zed_left_folder = os.path.join(base, "zed_left_raw")
            zed_left_view = FolderImageViewer(zed_left_folder, title=f"{run_id} — ZED Left", poll_ms=200)
            self.ui.tabWidget.addTab(zed_left_view, "ZED Left")

        if use_zed_right:   
            zed_right_folder = os.path.join(base, "zed_right_raw")
            zed_right_view = FolderImageViewer(zed_right_folder, title=f"{run_id} — ZED Right", poll_ms=200)
            self.ui.tabWidget.addTab(zed_right_view, "ZED Right")

        self.ui.tabWidget.setCurrentIndex(0)
class ClickableLabel(QLabel):
    clicked = Signal(str)

    def __init__(self, path: str, parent=None):
        super().__init__(parent)
        self._path = path

    def mousePressEvent(self, ev):
        self.clicked.emit(self._path)
        super().mousePressEvent(ev)

class FolderImageViewer(QWidget):
    """
    Displays MANY images from a folder (thumbnail grid) and refreshes periodically.
    Adds new images as they appear. Click a thumbnail to preview larger.
    Includes a Clear button that deletes ONLY images in this folder.
    """
    def __init__(
        self,
        folder: str,
        title: str = "",
        poll_ms: int = 250,
        thumb_size: int = 220,
        columns: int = 3,
        max_images: int = 2000,
        parent=None
    ):
        super().__init__(parent)
        self.folder = folder
        self.title = title
        self.poll_ms = poll_ms
        self.thumb_size = thumb_size
        self.columns = columns
        self.max_images = max_images

        self._known_paths = set()
        self._labels_by_path = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(8)

        # ---- Title row + Clear button ----
        header_row = QHBoxLayout()
        header_row.setContentsMargins(0, 0, 0, 0)

        self.title_lbl = QLabel(title)
        self.title_lbl.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.title_lbl.setStyleSheet("color:white; font-size:16px;")
        header_row.addWidget(self.title_lbl, 1)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setFixedWidth(90)
        self.clear_btn.setStyleSheet("""
            QPushButton{
                background:#242424; color:white;
                border:1px solid #444; border-radius:10px;
                padding:6px 10px;
            }
            QPushButton:hover{ border:1px solid #666; }
            QPushButton:pressed{ background:#3a3a3a; }
        """)
        self.clear_btn.clicked.connect(self._on_clear_clicked)
        header_row.addWidget(self.clear_btn, 0, Qt.AlignRight)

        layout.addLayout(header_row)

        # --- Scroll area for the gallery ---
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet("QScrollArea{background:#111; border:1px solid #333;}")
        layout.addWidget(self.scroll, 1)

        # --- Container inside scroll area ---
        self.grid_host = QWidget()
        self.grid = QGridLayout(self.grid_host)
        self.grid.setContentsMargins(10, 10, 10, 10)
        self.grid.setSpacing(10)
        self.scroll.setWidget(self.grid_host)

        # Info label (shows folder / status)
        self.info_lbl = QLabel("")
        self.info_lbl.setStyleSheet("color:#aaa;")
        layout.addWidget(self.info_lbl)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._tick)
        self.timer.start(self.poll_ms)

        self._tick()  # initial load

    def set_folder(self, folder: str):
        self.folder = folder
        self._clear_gallery()
        self._tick()

    def _clear_gallery(self):
        # remove all labels/widgets
        for path, lbl in list(self._labels_by_path.items()):
            lbl.setParent(None)
            lbl.deleteLater()
        self._labels_by_path.clear()
        self._known_paths.clear()

        # clear layout items
        while self.grid.count():
            item = self.grid.takeAt(0)
            w = item.widget()
            if w:
                w.setParent(None)
                w.deleteLater()

    def _list_images_sorted(self):
        if not self.folder or not os.path.isdir(self.folder):
            return []

        exts = ("*.png", "*.jpg", "*.jpeg", "*.bmp")
        files = []
        for e in exts:
            files.extend(glob.glob(os.path.join(self.folder, e)))

        files.sort(key=lambda p: os.path.getmtime(p))  # oldest -> newest
        return files

    def _add_thumbnail(self, path: str):
        pm = QPixmap(path)
        if pm.isNull():
            return

        thumb = pm.scaled(
            self.thumb_size, self.thumb_size,
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        lbl = ClickableLabel(path)
        lbl.setPixmap(thumb)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("""
            QLabel{
                background:#0f0f0f;
                border:1px solid #333;
                padding:6px;
                border-radius:8px;
            }
            QLabel:hover{
                border:1px solid #666;
            }
        """)
        lbl.setToolTip(os.path.basename(path))
        lbl.clicked.connect(self._open_preview)

        idx = len(self._labels_by_path)
        row = idx // self.columns
        col = idx % self.columns
        self.grid.addWidget(lbl, row, col)

        self._labels_by_path[path] = lbl
        self._known_paths.add(path)

    def _open_preview(self, path: str):
        dlg = QDialog(self)
        dlg.setWindowTitle(os.path.basename(path))
        dlg.resize(900, 700)

        lay = QVBoxLayout(dlg)
        lab = QLabel()
        lab.setAlignment(Qt.AlignCenter)
        lay.addWidget(lab, 1)

        pm = QPixmap(path)
        if not pm.isNull():
            lab.setPixmap(pm.scaled(dlg.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

        dlg.exec()

    def _enforce_limit(self):
        if self.max_images <= 0:
            return
        if len(self._labels_by_path) <= self.max_images:
            return

        remove_count = len(self._labels_by_path) - self.max_images
        paths_sorted = sorted(self._labels_by_path.keys(), key=lambda p: os.path.getmtime(p))

        for p in paths_sorted[:remove_count]:
            lbl = self._labels_by_path.pop(p, None)
            self._known_paths.discard(p)
            if lbl:
                lbl.setParent(None)
                lbl.deleteLater()

        self._reflow_grid()

    def _reflow_grid(self):
        widgets = list(self._labels_by_path.values())

        while self.grid.count():
            self.grid.takeAt(0)

        for i, w in enumerate(widgets):
            row = i // self.columns
            col = i % self.columns
            self.grid.addWidget(w, row, col)

    def _on_clear_clicked(self):
        # Only delete images inside THIS folder
        if not self.folder or not os.path.isdir(self.folder):
            QMessageBox.warning(self, "No folder", f"Folder not found:\n{self.folder}")
            return

        reply = QMessageBox.question(
            self,
            "Clear images",
            f"Delete ALL images in:\n{self.folder}\n\nThis only clears this camera folder.",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply != QMessageBox.Yes:
            return

        exts = ("*.png", "*.jpg", "*.jpeg", "*.bmp")
        deleted = 0
        failed = 0

        for e in exts:
            for path in glob.glob(os.path.join(self.folder, e)):
                try:
                    os.remove(path)
                    deleted += 1
                except Exception:
                    failed += 1

        # refresh UI
        self._clear_gallery()
        self._tick()

        if failed == 0:
            QMessageBox.information(self, "Cleared", f"Deleted {deleted} images.")
        else:
            QMessageBox.warning(self, "Partial", f"Deleted {deleted} images.\nFailed: {failed}")

    def _tick(self):
        if not self.folder or not os.path.isdir(self.folder):
            self.info_lbl.setText(f"No folder: {self.folder}")
            return

        files = self._list_images_sorted()
        if not files:
            self.info_lbl.setText(f"No images in: {self.folder}")
            return

        added = 0
        for path in files:
            if path not in self._known_paths:
                self._add_thumbnail(path)
                added += 1

        if added:
            self._enforce_limit()
            bar = self.scroll.verticalScrollBar()
            bar.setValue(bar.maximum())

        self.info_lbl.setText(f"{len(self._labels_by_path)} images  |  Folder: {self.folder}")

class ConnectArmWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.stackedWidget_3.setCurrentIndex(0)

        # Automation settings
        self._auto_mode = True           # auto-chain enabled
        self._final_step = "plane"       # "plane" or "half_sphere"
        self._min_pause_ms = 5000        # >= 5s between steps

        # Disable top buttons (only code can toggle)
        for btn in [
            self.ui.pushButton,   # config
            self.ui.pushButton_2, # roscore
            self.ui.pushButton_3, # calibrate
            #self.ui.pushButton_4, # driver
            #self.ui.pushButton_5, # moveit
            #self.ui.pushButton_6  # final
        ]:
            btn.setEnabled(False)
            btn.setCheckable(True)

                # ... your existing code ...
    #___________________________________________________________________________________________________________________________________________________________
        # --- Create stackedWidget_23 in right_main_container ---

        self.ui.terminal_3.setMinimumHeight(500)
        self.ui.terminal_3.setMaximumHeight(700)

        self.motion_stack = QStackedWidget(self.ui.terminal_3)
        self.motion_stack.setObjectName("stackedWidget_23")
        self.motion_stack.setStyleSheet("background-color: #1a1a1a;")

        # Make sure right_main_cointainer has a layout
        layout = self.ui.right_main_cointainer.layout()
        if layout is None:
            from PySide6.QtWidgets import QVBoxLayout
            layout = QVBoxLayout(self.ui.right_main_cointainer)
        layout.addWidget(self.motion_stack)
        self.run_home

        # Mode flag
        self._mode = "real"   # "real" or "sim"

        # ✅ Default = real motion pages
        self._use_motion_pages_from("/root/GUI/motion_pages.py")
        self.motion_stack.hide()

        # Create pages
        #self.hemi_page = HemiPage(parent=self.motion_stack)
        #self.planar_page = PlanarPage(parent=self.motion_stack)  # your existing planar widget

        #self.motion_stack.addWidget(self.hemi_page)    # index 0
        #self.motion_stack.addWidget(self.planar_page)  # index 1

        #self.motion_stack.hide()  # start hidden

        # Hemisphere button
        #self.ui.pushButton_7.clicked.connect(self.show_hemi_page)

        # Planar button
        #self.ui.pushButton_8.clicked.connect(self.show_planar_page)

        # Home button
        #self.ui.pushButton_14.clicked.connect(self.hide_motion_pages)

        # Flow button -> nav only
        self.ui.congigureBtn.clicked.connect(self.config)
        self.ui.roscoreBtn.clicked.connect(self.roscore)
        self.ui.calibrateBtn.clicked.connect(self.calibrate)
        self.ui.launchdriverBtn.clicked.connect(self.driver)
        #self.ui.launchmoveitBtn_2.clicked.connect(self.moveit)
        self.ui.Simulation.clicked.connect(self.config)

        # Real actions (manual)
        self.ui.congigureBtn.clicked.connect(self.config_ip)
        self.ui.Simulation.clicked.connect(self.start_simulation)
        self.ui.calibrateBtn.clicked.connect(self.calibrate_robot)
        self.ui.launchdriverBtn.clicked.connect(self.launch_driver)


        #self.ui.cbSimulationMode.toggled.connect(self.on_mode_changed)
        self._bind_motion_buttons_for_mode()

        # ⬇️ Start automation from STEP 2 (ROS Core)
        # One click on "roscore" runs ROS + auto-chains the rest.
        #self.ui.roscoreBtn.clicked.connect(self._auto_start_from_roscore)

        # Keep manual hooks for testing (not used in auto flow)
        #self.ui.roscoreBtn.clicked.connect(self.start_roscore)
        #self.ui.calibrateBtn.clicked.connect(self._auto_calibrate_robot)
        #self.ui.launchdriverBtn.clicked.connect(self._auto_launch_driver)
        #self.ui.launchmoveitBtn_2.clicked.connect(self._auto_launch_moveit)

        # Final-task buttons (manual)
        #self.ui.pushButton_7.clicked.connect(self.run_half_sphere)
        #self.ui.pushButton_8.clicked.connect(self.run_plane)

        # Back button
        self.backBtn_22 = QPushButton("Back", self.ui.page_2)
        self.backBtn_22.setStyleSheet(self._backBtnStyle())
        self.ui.verticalLayout_9.addWidget(self.backBtn_22)
        self.backBtn_22.clicked.connect(lambda: self._goBack())
    def goto_hemi(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.motion_stack.show()
        self.motion_stack.setCurrentWidget(self.hemi_page)
        if hasattr(self.ui, "pushButton_7"):
            self.ui.pushButton_7.setChecked(True)

    def goto_planar(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.motion_stack.show()
        self.motion_stack.setCurrentWidget(self.planar_page)
        if hasattr(self.ui, "pushButton_8"):
            self.ui.pushButton_8.setChecked(True)

    def goto_inf(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.motion_stack.show()
        self.motion_stack.setCurrentWidget(self.infinitypage)
        if hasattr(self.ui, "pushButton_9"):
            self.ui.pushButton_9.setChecked(True)


    def _load_module_from_path(self, module_name: str, path: str):
        spec = importlib.util.spec_from_file_location(module_name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod

    def _clear_motion_stack(self):
        # remove + delete old pages
        while self.motion_stack.count():
            w = self.motion_stack.widget(0)
            self.motion_stack.removeWidget(w)
            w.deleteLater()

    def _make_page(self, cls):
        """
        Supports BOTH styles:
          - New style: Page(run_home=..., go_back=..., parent=...)
          - Old style: Page(parent=...)
        """
        sig = inspect.signature(cls.__init__)
        if "run_home" in sig.parameters and "go_back" in sig.parameters:
            return cls(run_home=self.run_home, go_back=self._hide_motion_pages, parent=self.motion_stack)
        return cls(parent=self.motion_stack)

    def _use_motion_pages_from(self, module_path: str):
        """
        module_path: e.g. "/root/GUI/motion_pages.py" or "/root/GUI/sim_test.py"
        """
        mod = self._load_module_from_path("motion_pages_impl", module_path)

        self._clear_motion_stack()

        # create pages from the selected module
        # NOTE: sim_test.py pages expect (run_home, go_back, parent)
        # NOTE: motion_pages.py might be old style (parent only) -> handled by _make_page()

        self.hemi_page = self._make_page(mod.HemiPage)
        self.motion_stack.addWidget(self.hemi_page)     # index 0

        if hasattr(mod, "PlanarPage"):
            self.planar_page = self._make_page(mod.PlanarPage)
            self.motion_stack.addWidget(self.planar_page)   # index 1

        if hasattr(mod, "InfinityPage"):
            self.infinitypage = self._make_page(mod.InfinityPage)
            self.motion_stack.addWidget(self.infinitypage)  # index 2

    def _hide_motion_pages(self):
        self.motion_stack.hide()
        if hasattr(self.ui, "pushButton_7"):
            self.ui.pushButton_7.setChecked(False)
        if hasattr(self.ui, "pushButton_8"):
            self.ui.pushButton_8.setChecked(False)
        if hasattr(self.ui, "pushButton_9"):
            self.ui.pushButton_9.setChecked(False)

    def show_hemi_page(self):
        # make sure we are on the correct UI page
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.motion_stack.show()
        self.motion_stack.setCurrentWidget(self.hemi_page)
    
    def _make_page(self, cls):
        """
        Supports BOTH styles:
        - New style: Page(run_home=..., go_back=..., parent=...)
        - Old style: Page(parent=...)
        Also tolerates missing run_home by passing a dummy function.
        """
        import inspect
        sig = inspect.signature(cls.__init__)

        # fallback home callback
        home_cb = getattr(self, "run_home", lambda: None)

        if "run_home" in sig.parameters and "go_back" in sig.parameters:
            return cls(run_home=home_cb, go_back=self._hide_motion_pages, parent=self.motion_stack)

        return cls(parent=self.motion_stack)

  
    def _disconnect_if_connected(self, signal):
        try:
            signal.disconnect()
        except Exception:
            pass

    def _bind_motion_buttons_for_mode(self):
        """
        In sim mode: buttons 7/8/9 open hemi/planar/inf pages.
        In real mode: keep old behavior (whatever you had).
        """
        # Always clear previous connections (safe)


        if self._mode == "sim":
            # ✅ Simulation navigation
            self.ui.pushButton_7.clicked.connect(self.goto_hemi)    # Hemisphere
            self.ui.pushButton_8.clicked.connect(self.goto_planar)  # Planar
            self.ui.pushButton_9.clicked.connect(self.goto_inf)     # Infinity
            self.ui.pushButton_14.clicked.connect(self.run_home)    # Home
        else:
            # ✅ Real robot mode (restore original behavior)
            # Put here whatever your old connections were.
            # If you had show_hemi_page only:
            self.ui.pushButton_7.clicked.connect(self.show_hemi_page)
            #self.ui.pushButton_14.clicked.connect(self.run_home) 
            # If in real mode these buttons should do nothing, just leave them unconnected
            # or connect them to existing real functions:
            # self.ui.pushButton_8.clicked.connect(self.goto_planar)  # if real planar exists
            # self.ui.pushButton_9.clicked.connect(self.goto_inf)     # if real infinity exists
            # self.ui.pushButton_14.clicked.connect(self.run_home)    # if home exists

    def run_home(self):
        """
        Home button behavior.

        - In SIM mode: hide motion pages + go back to simulation menu (no ROS node needed).
        - In REAL mode: you can later launch your real home node here.
        """
        if self._mode == "sim":
            # In simulation, just go back / hide motion UI
            self._hide_motion_pages()
            return

        # REAL robot: keep it safe for now (no crash)
        # If you want, replace this later with real home-node launch.
        try:
            self._hide_motion_pages()
        except Exception:
            pass




    '''def show_planar_page(self):
            self.motion_stack.show()
            self.motion_stack.setCurrentWidget(self.planar_page)

    def hide_motion_pages(self):
            self.motion_stack.hide()'''

    '''def goto_hemi(self):
        # Simulation page / "menu" page
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.motion_stack.show()
        self.motion_stack.setCurrentWidget(self.hemi_page)
        self.ui.pushButton_7.setChecked(True)

    def goto_planar(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.motion_stack.show()
        self.motion_stack.setCurrentWidget(self.planar_page)
        self.ui.pushButton_8.setChecked(True)

    def _hide_motion_pages(self):
            # Called by "Back" from Hemi/Planar
        self.motion_stack.hide()
            # Optionally go back to some default page
            # self.ui.stackedWidget_3.setCurrentIndex(0)
        if hasattr(self.ui, "pushButton_7"):
            self.ui.pushButton_7.setChecked(False)
        if hasattr(self.ui, "pushButton_8"):
            self.ui.pushButton_8.setChecked(False)

    def run_home(self):
        ok, err = launch_node("home_node")
        if ok:
            QMessageBox.information(self, "Launching", "Launched home_node")
        else:
            QMessageBox.critical(self, "Error", err or "Unknown error")

    '''


    # -----------------------
    # Styles / Navigation
    # -----------------------
    def _backBtnStyle(self):
        return ("""
            QPushButton {
                font-size: 18pt;
                background-color: #1a1a1a;
                color: white;
                border: 1px solid gray;
                border-radius: 20px;
                padding: 8px;
            }
            QPushButton:pressed {
                background-color: white;
                color: black;
            }
        """)

    def _goBack(self):
        idx = self.ui.stackedWidget_3.currentIndex()
        if idx == 5:
            self.ui.stackedWidget_3.setCurrentIndex(0)
            self.ui.pushButton.setChecked(True)
            self.ui.pushButton_2.setChecked(False)
        self.ui.roscoreBtn.setIconSize(QSize(17, 16))

    # --- Navigation logic (updates pages + highlights) --- togel 1 2 3 4
    def config(self):
        sender = self.sender()

        if sender == self.ui.Simulation:
            self.ui.stackedWidget_3.setCurrentIndex(1)
            self.ui.pushButton.setChecked(True)
            self.ui.pushButton_2.setChecked(True)
            self.ui.pushButton_3.setChecked(True)
        elif sender == self.ui.congigureBtn:
            self.ui.stackedWidget_3.setCurrentIndex(3)
            self.ui.pushButton.setChecked(True)

    def roscore(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.pushButton_2.setChecked(True)

    def calibrate(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.pushButton_3.setChecked(True)

    def driver(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.pushButton_2.setChecked(True)
    '''
    def moveit(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.pushButton_5.setChecked(True)
'''
    # -----------------------
    # Validation / Dialogs
    # -----------------------
    def get_full_ip(self, entry_field):
        try:
            ip = entry_field.text().strip()
        except Exception as e:
            self.show_ip_error(f"Invalid widget passed to get_full_ip: {e}")
            return None

        ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if not re.match(ip_pattern, ip):
            self.show_ip_error("Invalid IP format. Example: 192.168.1.10")
            self.ui.stackedWidget_3.setCurrentIndex(0)
            self.ui.pushButton.setChecked(False)
            return None

        parts = ip.split(".")
        if any(not part.isdigit() or not (0 <= int(part) <= 255) for part in parts):
            self.show_ip_error("Each part of IP must be between 0 and 255.")
            self.ui.stackedWidget_3.setCurrentIndex(0)
            self.ui.pushButton.setChecked(False)
            return None

        return ip

    def show_ip_error(self, message):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Invalid IP Address")
        msg.setText(message)
        msg.setStyleSheet("""
            QMessageBox { background-color:white; color: black; }
            QMessageBox QLabel { background-color:white; color: black; }
            QMessageBox QPushButton { background-color: #f0f0f0; color: black; }
        """)
        msg.exec()

    def show_password_dialog(self):
        dialog = QInputDialog(self)
        dialog.setWindowTitle("Sudo Password")
        dialog.setLabelText("Enter your sudo password:")
        dialog.setTextEchoMode(QLineEdit.EchoMode.Password)
        dialog.setStyleSheet("""
            QInputDialog { background-color: white; color: black; }
            QLabel { color: black; }
            QLineEdit { background-color: white; color: black; }
            QPushButton { background-color: #f0f0f0; color: black; }
        """)
        ok = dialog.exec()
        return dialog.textValue(), ok == QDialog.Accepted

    # -----------------------
    # Command helpers (Linux/bash)
    # -----------------------
    '''def run_sudo_command(self, command):
        
        if not self.robot_ip:
            return 
        if not hasattr(self, 'terminal_3_text_edit'):
        # Dynamically create QTextEdit widget if not already created
            self.terminal_3_text_edit = QTextEdit(self.ui.right_main_cointainer)
            self.terminal_3_text_edit.setObjectName("terminal_3")
            self.ui.verticalLayout.addWidget(self.terminal_3_text_edit)  # Add to layout
    
        password, accepted = self.show_password_dialog()
        if accepted and password:
                try:
                    sudo_command = f"echo '{password}' | sudo -S {command}; echo 'Press Enter to close...'; read"
            

                    proc = subprocess.Popen(
                        ['gnome-terminal', '--', 'bash', '-c', sudo_command],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    stdout, stderr = proc.communicate(password + '\n')

                    if proc.returncode == 0:
                        self.terminal_3_text_edit.append("✅ Command succeeded!\n" + stdout)
                        QTimer.singleShot(2000, lambda : self.run_command("bash robot_control.sh config_ip_2 dummy {self.robot_ip}", "pinging robot ip"))
                    else:
                        self.terminal_3_text_edit.append("❌ Command failed!\n" + stderr)
                except Exception as e:
                    self.terminal_3_text_edit.append(f"⚡ Exception: {str(e)}")
        else:
                self.terminal_3_text_edit.append("⚡ No password entered.")'''
    


    '''def run_command(self, command, title=""):
    # Ensure terminal widget exists
        if not hasattr(self, 'terminal_3_text_edit'):
        # Dynamically create QTextEdit widget if not already created
            self.terminal_3_text_edit = QTextEdit(self.ui.right_main_cointainer)
            self.terminal_3_text_edit.setObjectName("terminal_3")
            self.ui.verticalLayout.addWidget(self.terminal_3_text_edit)  # Add to layout

        self.terminal_3_text_edit.append(f"\n>>> {title or command}\n")

        try:
        # Use your sros() bash function to source EVERYTHING
        # bash -i ensures ~/.bashrc (with sros) is loaded
            full_cmd = f"sros; {command}"

            subprocess.Popen(
                ['bash', '-i', '-c', full_cmd],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
        )

            self.terminal_3_text_edit.append(f"{title or command} launched in new terminal.\n")
        except Exception as e:
            self.terminal_3_text_edit.append(f"Error: {str(e)}\n")'''



    def launch_set_ip(self, ip_pc: str, ip_robot: str):
        try:
            bash_cmd = (
            "sros; "
            f"ip addr flush dev enp2s0; "
            f"ip addr add {ip_pc}/24 dev enp2s0;"
            
            )

            proc = subprocess.Popen(
                ["bash", "-i", "-c", bash_cmd],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                start_new_session=True  
            )
            return True, None

        except Exception as e:
            return False, str(e)
        
    def launch_ur10e_control(self, ip_robot: str):

        main = self.window()
        
        main.procman.stop_all()

        os.environ["ROS_LOCALHOST_ONLY"] = "1"

        script_path = "/root/GUI/start_ur_driver.sh"
        cmd = f"bash -lc '{script_path} {ip_robot}'"
        main.procman.start(cmd, log_path="/tmp/start_driver.log")
        self.driver_proc = subprocess.Popen(
            ["/bin/bash", script_path, ip_robot],
            stdin=subprocess.DEVNULL,
 
            
            text=True,
            start_new_session=True  
        )
        # ✅ Share the handle with the main window (MySideBar)
        main = self.window()
        main.driver_proc = self.driver_proc

    def launch_simulation(self):
        main = self.window()
        
        main.procman.stop_all()   # optional: stop previous run before starting a new one

        # Make DDS stable (optional but recommended)
        os.environ["ROS_LOCALHOST_ONLY"] = "1"

        script_path = "/root/GUI/start_sim.sh"
        cmd = f"bash -lc '{script_path}'"
        main.procman.start(cmd, log_path="/tmp/start_sim.log")

        self.moveit_proc = subprocess.Popen(
               
            ["/bin/bash", script_path],
            stdin=subprocess.DEVNULL,
           
            text=True,
            start_new_session=True  
        )
    
    def launch_thws_moveit(self):

        main = self.window()
        if main.procman.any_alive():
            main.procman.stop_all()

        os.environ["ROS_LOCALHOST_ONLY"] = "1"

        script_path = "/root/GUI/start_thws_moveit.sh"
        cmd = f"bash -lc '{script_path}'"
        main.procman.start(cmd, log_path="/tmp/start_thws_moveit.log")
        self.moveit_proc = subprocess.Popen(
               
            ["/bin/bash", script_path],
            stdin=subprocess.DEVNULL,
           
            text=True,
            start_new_session=True  
        )
            

    def start_driver(self, cmd: str):
        # Prevent double-start
        if getattr(self, "driver_proc", None) is not None and self.driver_proc.poll() is None:
            print("[INFO] Driver already running, not starting again.")
            return

        # Make DDS more stable for single-machine GUI use
        os.environ["ROS_LOCALHOST_ONLY"] = "1"

        log_path = "/tmp/driver_launch.log"
        logf = open(log_path, "w")

        self.driver_proc = subprocess.Popen(
            ["bash", "-lc", cmd],
            start_new_session=True,          # ✅ this is what makes killpg work
            stdout=logf,
            stderr=subprocess.STDOUT,
            text=True
        )
        main = self.window()
        if hasattr(main, "_managed_procs"):
            main._managed_procs.append(self.driver_proc)
        main.driver_proc = self.driver_proc
        print(f"[INFO] Started driver PID={self.driver_proc.pid} log={log_path}")



    
    
    
    # -----------------------
    # Step 1–2 manual actions
    # -----------------------
    def config_ip(self):
        pc_ip = self.get_full_ip(self.ui.PC_IP)
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not pc_ip or not robot_ip:
            return
        self.launch_set_ip(pc_ip, robot_ip)

    #def start_roscore(self):
        #self.run_command("robot_control.sh start_roscore", "Start ROS Core")
    
    # ======================================================
    # AUTO-CHAINED Actions (Step 2 -> Step 6)
    # ======================================================
    '''
    def _advance_after_delay(self, next_callable, delay_ms=None):
        if delay_ms is None:
            delay_ms = self._min_pause_ms
        QTimer.singleShot(delay_ms, next_callable)

    def _toast(self, text: str, ms: int = 1600):
        # tiny on-screen cue (optional)
        lbl = QLabel(text, self)
        lbl.setStyleSheet("""
            QLabel{
                background:#2d2f36; color:#00ff88;
                padding:6px 12px; border-radius:10px; font-size:14px;
            }""")
        lbl.move(16, 16)
        lbl.show()
        QTimer.singleShot(ms, lbl.deleteLater)

    def _auto_start_from_roscore(self):
        """STEP 2: Click 'roscore' → auto-run all the way to final task."""
        self.roscore()  # visual
        self.start_roscore()
        self._toast("ROS Core started → Calibrate next…")
        if self._auto_mode:
            self._advance_after_delay(self._auto_calibrate_robot)

    def _auto_calibrate_robot(self):
        """STEP 3: Calibrate → Driver."""
        self.calibrate()
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            self._auto_mode = False
            return
        self._run_and_get_terminal(f"robot_control.sh calibrate_robot {robot_ip}", "Launch Calibration")
        self._toast("Calibrating → Driver next…")
        if self._auto_mode:
            self._advance_after_delay(self._auto_launch_driver)

    def _auto_launch_driver(self):
        """STEP 4: Driver → MoveIt."""
        self.driver()
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            self._auto_mode = False
            return
        self._run_and_get_terminal(f"robot_control.sh launch_driver {robot_ip}", "Launch Robot Driver")
        self._toast("Driver up → MoveIt next…")
        if self._auto_mode:
            self._advance_after_delay(self._auto_launch_moveit)

    def _auto_launch_moveit(self):
        """STEP 5: MoveIt → Final task."""
        self.moveit()
        self._run_and_get_terminal("robot_control.sh launch_moveit", "Launch MoveIt")
        self._toast("MoveIt up → Path plan…")
        if self._auto_mode:
            self._advance_after_delay(self._auto_final_task)

    def _auto_final_task(self):
        """STEP 6: Path plan, then stop auto."""
        if self._final_step == "half_sphere":
            self._toast("Running Half-Sphere Path")
            self.run_half_sphere()
        else:
            self._toast("Running Plane Path")
            self.run_plane()
        self._auto_mode = False
    '''
    # -----------------------
    # Manual Final Tasks
    # -----------------------
    def calibrate_robot(self):
        
        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            return
        self.launch_thws_moveit()
        
    def launch_driver(self):
        if self._mode != "real":
            self._use_motion_pages_from("/root/GUI/motion_pages.py")
            self._mode = "real"
            self._bind_motion_buttons_for_mode()   # ✅ restore old behavior

        robot_ip = self.get_full_ip(self.ui.Robot_IP)
        if not robot_ip:
            return
        self.launch_ur10e_control(robot_ip)

    '''
    def launch_moveit(self):
        self.run_command("robot_control.sh launch_moveit", "Launch MoveIt")

    def run_plane(self):
        self.run_command("robot_control.sh run_plane", "Run plane.py")

    def run_half_sphere(self):
        self.run_command("robot_control.sh run_half_sphere", "Run half_sphere.py")'''
            
    def start_simulation(self):
        # switch to simulation motion pages
        if self._mode != "sim":
            self._use_motion_pages_from("/root/GUI/sim_test.py")
            self._mode = "sim"
            self._bind_motion_buttons_for_mode()   # ✅ rebind buttons for sim navigation

        # Do NOT open hemi page automatically
        # Only launch simulation backend
        self.launch_simulation()
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QLineEdit, QFormLayout
from PySide6.QtGui import QDoubleValidator, QIntValidator

class CalibrationPatternDialog(QDialog):
    """
    Small popup: choose pattern.
    For now: only Checkerboard is functional.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calibration Pattern")
        self.setFixedWidth(320)

        self.setStyleSheet("""
            QDialog { background-color: #1a1a1a; color: white; }
            QLabel { color: white; }
            QLineEdit {
                background-color: #242424; color: white;
                border: 1px solid #444; border-radius: 6px;
                padding: 6px;
            }
            QPushButton {
                background-color: #242424; color: white;
                border: 1px solid #444; border-radius: 10px;
                padding: 8px 12px;
            }
            QPushButton:pressed { background-color: #3a3a3a; }
        """)

        root = QVBoxLayout(self)
        root.setContentsMargins(14, 14, 14, 14)
        root.setSpacing(10)

        title = QLabel("Select calibration target")
        title.setStyleSheet("font-size: 15px; font-weight: 600;")
        root.addWidget(title)

        # Options (radio is better than checkbox for mutual exclusion)
        self.rb_checker = QRadioButton("Checkerboard (regular)")
        self.rb_charuco = QRadioButton("Charuco (not implemented yet)")
        self.rb_checker.setChecked(True)

        root.addWidget(self.rb_checker)
        root.addWidget(self.rb_charuco)

        # Inputs (only meaningful for checkerboard)
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignLeft)

        self.nx_edit = QLineEdit("7")
        self.ny_edit = QLineEdit("10")
        self.square_edit = QLineEdit("0.022")

        self.nx_edit.setValidator(QIntValidator(1, 200, self))
        self.ny_edit.setValidator(QIntValidator(1, 200, self))
        self.square_edit.setValidator(QDoubleValidator(0.0001, 10.0, 6, self))

        form.addRow("nx:", self.nx_edit)
        form.addRow("ny:", self.ny_edit)
        form.addRow("square-size (m):", self.square_edit)

        root.addLayout(form)

        # Disable inputs if charuco selected
        def update_enabled():
            enabled = self.rb_checker.isChecked()
            self.nx_edit.setEnabled(enabled)
            self.ny_edit.setEnabled(enabled)
            self.square_edit.setEnabled(enabled)

        self.rb_checker.toggled.connect(update_enabled)
        self.rb_charuco.toggled.connect(update_enabled)
        update_enabled()

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch(1)

        self.cancel_btn = QPushButton("Cancel")
        self.ok_btn = QPushButton("OK")

        self.cancel_btn.clicked.connect(self.reject)
        self.ok_btn.clicked.connect(self.accept)

        btn_row.addWidget(self.cancel_btn)
        btn_row.addWidget(self.ok_btn)

        root.addLayout(btn_row)

    def get_values(self) -> dict:
        """
        Returns config dict.
        For now only checkerboard is supported.
        """
        if self.rb_charuco.isChecked():
            return {
                "pattern": "charuco",   # not implemented yet
            }

        nx = int(self.nx_edit.text() or "7")
        ny = int(self.ny_edit.text() or "10")
        sq = float(self.square_edit.text() or "0.022")

        return {
            "pattern": "checkerboard",
            "nx": nx,
            "ny": ny,
            "square_size": sq,
        }


# ----------------------------
# Worker (UNCHANGED LOGIC)
# ----------------------------
class CalibrationWorker(QObject):
    progress = Signal(str)             # sends "Step 1/4: ... "
    finished = Signal(bool, str)


    SOURCES = [
        "/opt/ros/humble/setup.bash",
        "/root/ur_ws_sim/install/setup.bash",
    ]

    SCRIPTS_DIR = "/root/ur_ws_sim/tools/scripts"

    def __init__(self, base_dir: str, params: dict, parent=None):
        super().__init__(parent)
        self.base_dir = base_dir
        self.params = params 
    def _script(self, name: str) -> str:
        p = os.path.join(self.SCRIPTS_DIR, name)
        if not os.path.exists(p):
            raise FileNotFoundError(f"Script not found: {p}")
        return p

    def _run_one(self, title: str, args: list[str], cwd: str):
        self.progress.emit(title)

        if args and args[0] == "python3":
            args[0] = sys.executable

        sources_existing = []
        for s in self.SOURCES:
            if os.path.exists(s):
                sources_existing.append(s)
            else:
                print(f"[WARN] source file not found: {s}")

        source_cmd = " && ".join(f"source {shlex.quote(s)}" for s in sources_existing)
        run_cmd = " ".join(shlex.quote(x) for x in args)
        bash_cmd = f"set -e; {source_cmd} && {run_cmd}" if source_cmd else f"set -e; {run_cmd}"

        subprocess.run(["bash", "-lc", bash_cmd], cwd=cwd, check=True)

    @Slot()
    def run(self):
        try:
            scripts_multi = self.SCRIPTS_DIR
            scripts_rs = "/root/ur_ws_sim/tools/realsense_calib"

            # --- inputs from GUI ---
            run_id = str(self.params.get("run_id", "")).strip()
            if not run_id:
                raise RuntimeError("run_id is empty. Please enter a Run ID in the GUI.")

            use_realsense = bool(self.params.get("use_realsense", False))
            use_webcam    = bool(self.params.get("use_webcam", False))
            use_zed_left = bool(self.params.get("use_zed_left", False))
            use_zed_right = bool(self.params.get("use_zed_right", False))
            nx = int(self.params.get("nx", 7))
            ny = int(self.params.get("ny", 10))
            square_size = float(self.params.get("square_size", 0.022))
            if not (use_realsense or use_webcam or use_zed_left or use_zed_right):
                raise RuntimeError("No cameras selected for calibration.")

            rs_name = str(self.params.get("camera_name", "realsense")).strip() or "realsense"

            # --- resolve which pipeline to use (but execute with ONE loop) ---
            steps = []

            # If ONLY RealSense -> use your realsense_calib scripts
            if use_realsense and (not use_webcam and not use_zed_left and not use_zed_right  ):
                calib_path = f"/root/ur_ws_sim/data/{run_id}/calib/CameraParams_{rs_name}.npz"

                steps = [
                    (
                        "Step 1/4: RealSense camera calibration …",
                        [
                            "python3", "/root/ur_ws_sim/tools/realsense_calib/camera_calibration.py",
                            "--run-id", run_id,
                            "--camera-name", rs_name,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--output", calib_path,
                            "--show",
                        ],
                        scripts_rs,
                    ),
                    (
                        "Step 2/4: RealSense pose estimation (PnP) …",
                        [
                            "python3", "/root/ur_ws_sim/tools/realsense_calib/camera_pose_estimation_PnP.py",
                            "--run-id", run_id,
                            "--camera-name", rs_name,
                            "--calib", calib_path,
                        ],
                        scripts_rs,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration (Tsai) …",
                        [
                            "python3", "/root/ur_ws_sim/tools/realsense_calib/hand_eye_calibration.py",
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--camera-name", rs_name,
                            "--method", "Tsai",
                        ],
                        scripts_rs,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", "/root/ur_ws_sim/tools/realsense_calib/make_calibration_report.py",
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--camera-name", rs_name,
                        ],
                        scripts_rs,
                    ),
                ]

            # If BOTH RealSense + Webcam -> use your multi-camera pipeline
            elif use_realsense and use_webcam and not use_zed_left and not use_zed_right :
                steps = [
                    (
                        "Step 1/4: Multi-camera calibration …",
                        [
                            "python3", self._script("multi_camera_calibration.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--cameras", "realsense", "webcam",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 2/4: Pose estimation (PnP) …",
                        [
                            "python3", self._script("multi_camera_PnP.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--cams", "realsense", "webcam",
                            "--square-size", str(square_size),
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration …",
                        [
                            "python3", self._script("multi_sensor_handeye_opt.py"),
                            "--run-id", run_id,
                            "--no-of-runs", "10",
                            "--cams", "realsense", "webcam",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", self._script("generate_multi_sensor_report.py"),
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--cams", "realsense", "webcam",

                        ],
                        scripts_multi,
                    ),
                ]
            # If BOTH RealSense + Webcam -> use your multi-camera pipeline
            elif use_realsense and use_zed_left and not use_webcam and not use_zed_right:
                steps = [
                    (
                        "Step 1/4: Multi-camera calibration …",
                        [
                            "python3", self._script("multi_camera_calibration.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--cameras", "realsense", "zed_left_raw",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 2/4: Pose estimation (PnP) …",
                        [
                            "python3", self._script("multi_camera_PnP.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--cams", "realsense", "zed_left_raw",
                            "--square-size", str(square_size),
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration …",
                        [
                            "python3", self._script("multi_sensor_handeye_opt.py"),
                            "--run-id", run_id,
                            "--no-of-runs", "10",
                            "--cams", "realsense", "zed_left_raw",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", self._script("generate_multi_sensor_report.py"),
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--cams", "realsense", "zed_left_raw",
                        ],
                        scripts_multi,
                    ),
                ]

                # If BOTH RealSense + Webcam -> use your multi-camera pipeline
            elif use_realsense and use_zed_right and not use_webcam and not use_zed_left:
                steps = [
                    (
                        "Step 1/4: Multi-camera calibration …",
                        [
                            "python3", self._script("multi_camera_calibration.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--cameras", "realsense", "zed_right_raw",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 2/4: Pose estimation (PnP) …",
                        [
                            "python3", self._script("multi_camera_PnP.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--cams", "realsense", "zed_right_raw",
                            "--square-size", str(square_size),
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration …",
                        [
                            "python3", self._script("multi_sensor_handeye_opt.py"),
                            "--run-id", run_id,
                            "--no-of-runs", "10",
                            "--cams", "realsense", "zed_right_raw",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", self._script("generate_multi_sensor_report.py"),
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--cams", "realsense", "zed_right_raw",
                        ],
                        scripts_multi,
                    ),
                ]
            elif use_zed_left and use_zed_right and not use_webcam and not use_realsense:
                steps = [
                    (
                        "Step 1/4: Multi-camera calibration …",
                        [
                            "python3", self._script("multi_camera_calibration.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--cameras", "zed_left_raw", "zed_right_raw",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 2/4: Pose estimation (PnP) …",
                        [
                            "python3", self._script("multi_camera_PnP.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--cams", "zed_left_raw", "zed_right_raw",
                            "--square-size", str(square_size),
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration …",
                        [
                            "python3", self._script("multi_sensor_handeye_opt.py"),
                            "--run-id", run_id,
                            "--no-of-runs", "10",
                            "--cams", "zed_left_raw", "zed_right_raw",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", self._script("generate_multi_sensor_report.py"),
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--cams", "zed_left_raw", "zed_right_raw",
                        ],
                        scripts_multi,
                    ),
                ]

            elif use_zed_left and use_zed_right and use_realsense and not use_webcam:
                steps = [
                    (
                        "Step 1/4: Multi-camera calibration …",
                        [
                            "python3", self._script("multi_camera_calibration.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--cameras", "zed_left_raw", "zed_right_raw", "realsense",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 2/4: Pose estimation (PnP) …",
                        [
                            "python3", self._script("multi_camera_PnP.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--cams", "zed_left_raw", "zed_right_raw", "realsense",
                            "--square-size", str(square_size),
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration …",
                        [
                            "python3", self._script("multi_sensor_handeye_opt.py"),
                            "--run-id", run_id,
                            "--no-of-runs", "10",
                            "--cams", "zed_left_raw", "zed_right_raw", "realsense",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", self._script("generate_multi_sensor_report.py"),
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--cams", "zed_left_raw", "zed_right_raw", "realsense",
                        ],
                        scripts_multi,
                    ),
                ]
            elif use_zed_left and use_zed_right and use_realsense and use_webcam:
                steps = [
                    (
                        "Step 1/4: Multi-camera calibration …",
                        [
                            "python3", self._script("multi_camera_calibration.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--square-size", str(square_size),
                            "--cameras", "zed_left_raw", "zed_right_raw", "realsense","webcam",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 2/4: Pose estimation (PnP) …",
                        [
                            "python3", self._script("multi_camera_PnP.py"),
                            "--run-id", run_id,
                            "--nx", str(nx),
                            "--ny", str(ny),
                            "--cams", "zed_left_raw", "zed_right_raw", "realsense","webcam",
                            "--square-size", str(square_size),
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 3/4: Hand–eye calibration …",
                        [
                            "python3", self._script("multi_sensor_handeye_opt.py"),
                            "--run-id", run_id,
                            "--no-of-runs", "10",
                            "--cams", "zed_left_raw", "zed_right_raw", "realsense","webcam",
                        ],
                        scripts_multi,
                    ),
                    (
                        "Step 4/4: Creating calibration report …",
                        [
                            "python3", self._script("generate_multi_sensor_report.py"),
                            "--base-dir", "/root/ur_ws_sim/data",
                            "--run-id", run_id,
                            "--cams", "zed_left_raw", "zed_right_raw", "realsense","webcam",
                        ],
                        scripts_multi,
                    ),
                ]

            elif use_zed_left and not use_zed_right and not use_realsense and use_webcam:
                            steps = [
                                (
                                    "Step 1/4: Multi-camera calibration …",
                                    [
                                        "python3", self._script("multi_camera_calibration.py"),
                                        "--run-id", run_id,
                                        "--nx", str(nx),
                                        "--ny", str(ny),
                                        "--square-size", str(square_size),
                                        "--cameras", "zed_left_raw", "webcam",
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 2/4: Pose estimation (PnP) …",
                                    [
                                        "python3", self._script("multi_camera_PnP.py"),
                                        "--run-id", run_id,
                                        "--nx", str(nx),
                                        "--ny", str(ny),
                                        "--cams", "zed_left_raw","webcam",
                                        "--square-size", str(square_size),
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 3/4: Hand–eye calibration …",
                                    [
                                        "python3", self._script("multi_sensor_handeye_opt.py"),
                                        "--run-id", run_id,
                                        "--no-of-runs", "10",
                                        "--cams", "zed_left_raw", "webcam",
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 4/4: Creating calibration report …",
                                    [
                                        "python3", self._script("generate_multi_sensor_report.py"),
                                        "--base-dir", "/root/ur_ws_sim/data",
                                        "--run-id", run_id,
                                        "--cams", "zed_left_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                            ]
            elif not use_zed_left and use_zed_right and not use_realsense and use_webcam:
                            steps = [
                                (
                                    "Step 1/4: Multi-camera calibration …",
                                    [
                                        "python3", self._script("multi_camera_calibration.py"),
                                        "--run-id", run_id,
                                        "--nx", str(nx),
                                        "--ny", str(ny),
                                        "--square-size", str(square_size),
                                        "--cameras", "zed_right_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 2/4: Pose estimation (PnP) …",
                                    [
                                        "python3", self._script("multi_camera_PnP.py"),
                                        "--run-id", run_id,
                                        "--nx", str(nx),
                                        "--ny", str(ny),
                                        "--cams", "zed_right_raw","webcam",
                                        "--square-size", str(square_size),
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 3/4: Hand–eye calibration …",
                                    [
                                        "python3", self._script("multi_sensor_handeye_opt.py"),
                                        "--run-id", run_id,
                                        "--no-of-runs", "10",
                                        "--cams", "zed_right_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 4/4: Creating calibration report …",
                                    [
                                        "python3", self._script("generate_multi_sensor_report.py"),
                                        "--base-dir", "/root/ur_ws_sim/data",
                                        "--run-id", run_id,
                                        "--cams", "zed_right_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                            ]
            elif use_zed_left and use_zed_right and not use_realsense and use_webcam:
                            steps = [
                                (
                                    "Step 1/4: Multi-camera calibration …",
                                    [
                                        "python3", self._script("multi_camera_calibration.py"),
                                        "--run-id", run_id,
                                        "--nx", str(nx),
                                        "--ny", str(ny),
                                        "--square-size", str(square_size),
                                        "--cameras", "zed_left_raw", "zed_right_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 2/4: Pose estimation (PnP) …",
                                    [
                                        "python3", self._script("multi_camera_PnP.py"),
                                        "--run-id", run_id,
                                        "--nx", str(nx),
                                        "--ny", str(ny),
                                        "--cams", "zed_left_raw", "zed_right_raw","webcam",
                                        "--square-size", str(square_size),
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 3/4: Hand–eye calibration …",
                                    [
                                        "python3", self._script("multi_sensor_handeye_opt.py"),
                                        "--run-id", run_id,
                                        "--no-of-runs", "10",
                                        "--cams", "zed_left_raw", "zed_right_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                                (
                                    "Step 4/4: Creating calibration report …",
                                    [
                                        "python3", self._script("generate_multi_sensor_report.py"),
                                        "--base-dir", "/root/ur_ws_sim/data",
                                        "--run-id", run_id,
                                        "--cams", "zed_left_raw", "zed_right_raw","webcam",
                                    ],
                                    scripts_multi,
                                ),
                            ]
            



            # If ONLY Webcam -> not defined (you can add later)
            else:
                raise RuntimeError("Webcam-only calibration not implemented. Enable RealSense or enable both cameras.")

            # --- execute (ONE unified loop) ---
            for title, args, cwd in steps:
                self._run_one(title, args, cwd=cwd)

            self.finished.emit(True, "Calibration pipeline completed successfully.")

        except FileNotFoundError as e:
            traceback.print_exc()
            self.finished.emit(False, str(e))
        except subprocess.CalledProcessError as e:
            traceback.print_exc()
            self.finished.emit(False, f"Command failed with exit code {e.returncode}.")
        except Exception as e:
            traceback.print_exc()
            self.finished.emit(False, f"Unexpected error:\n{e}")


# -----------------------
# Page with NON-JUMPING progress UI
# ----------------------------
class CalibrationPage(QWidget):
    def __init__(self,hemi_page, params=None, parent=None):
        
        super().__init__(parent)
        self.params = params or {}
        
        self.hemi_page = hemi_page
        self.ui = calibrate_form()
        self.ui.setupUi(self)
        # Replace your status_label with a fixed-size "progress row"
        self._create_progress_row()

     

        self.ui.pushButton_111.clicked.connect(self.start_full_calibration)
        #self.ui.pushButton_222.clicked.connect(self.run_save_report_only)
        self.ui.pushButton_222.clicked.connect(self.saveResults)
     

        self._thread = None
        self._worker = None
    def show_info(self, msg: str):
        QMessageBox.information(self, "Info", msg)

    def show_error(self, msg: str):
        QMessageBox.critical(self, "Error", msg)

        
 

    RESULTS_DIR = Path("/root/GUI/Result")

    def store_latest_calibration_result(self):
        params = getattr(self.hemi_page, "current_params", None) or {}

        run_id = str(params.get("run_id", "")).strip()
        if not run_id:
            raise RuntimeError("run_id is empty. Please enter a Run ID in the GUI.")

        use_webcam    = bool(params.get("use_webcam", False))
        use_realsense = bool(params.get("use_realsense", False))
        use_zed_left  = bool(params.get("use_zed_left", False))
        use_zed_right = bool(params.get("use_zed_right", False))

        results_dir = Path(f"/root/ur_ws_sim/data/{run_id}/results")

        only_realsense = (
            use_realsense and not use_webcam and not use_zed_left and not use_zed_right
        )

        source_pdf = results_dir / ("calib_report_realsense.pdf" if only_realsense else "multi_sensor_report.pdf")

        if not source_pdf.exists():
            print(f"⚠️ Report not found: {source_pdf}")
            return None

        RESULTS_DIR.mkdir(parents=True, exist_ok=True)

        existing = sorted(RESULTS_DIR.glob("Result *.pdf"))
        next_index = 1
        for p in existing:
            if p.stem.startswith("Result "):
                try:
                    num = int(p.stem.replace("Result ", "").strip())
                    next_index = max(next_index, num + 1)
                except ValueError:
                    pass

        dest = RESULTS_DIR / f"Result {next_index}.pdf"
        shutil.copy2(source_pdf, dest)
        return dest

    # ---------- UI helpers ----------
    def _create_progress_row(self):
        """
        Adds a small progress bar + message INSIDE widget_7
        (bar on top, text below, no layout jump)
        """

        container = self.ui.widget_7   # <-- IMPORTANT: target widget_7

        # Ensure widget_7 has a layout
        layout = container.layout()
        if layout is None:
            layout = QVBoxLayout(container)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setSpacing(6)

        # --- Progress bar (small & thin) ---
        self.progressBar = QProgressBar(container)
        self.progressBar.setRange(0, 4)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFixedHeight(6)
        self.progressBar.setFixedWidth(300) 
        self.progressBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.progressBar.setStyleSheet("""
            QProgressBar {
                border: none;
                background-color: #2a2f38;
                border-radius: 3px;
            }
            QProgressBar::chunk {
                background-color: #3daee9;
                border-radius: 3px;
            }
        """)

        # --- Message label (fixed height, no wrap) ---
        self.progressLabel = QLabel("", container)
        self.progressLabel.setFixedHeight(18)
        self.progressLabel.setWordWrap(False)
        self.progressLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.progressLabel.setStyleSheet("color: white;")

        # Add to widget_7 layout (bar above text)
        layout.addWidget(self.progressBar)
        layout.addWidget(self.progressLabel)
         # ✅ CENTER THEM
        layout.setAlignment(self.progressBar, Qt.AlignHCenter)
        layout.setAlignment(self.progressLabel, Qt.AlignHCenter)



    def _set_elided_progress_text(self, text: str):
        """
        Keeps label one-line and prevents layout changes by eliding with "...".
        """
        fm = QFontMetrics(self.progressLabel.font())
        # Use current width; if 0 (not shown yet), use a safe fallback
        w = self.progressLabel.width()
        if w <= 10:
            w = 500
        self.progressLabel.setText(fm.elidedText(text, Qt.ElideRight, w))

    def _set_busy(self, busy: bool):
        if busy:
            self.ui.pushButton_111.setEnabled(False)
            self.ui.pushButton_222.setEnabled(False)
            self.setCursor(Qt.WaitCursor)
        else:
            self.ui.pushButton_111.setEnabled(True)
            self.ui.pushButton_222.setEnabled(True)
            self.unsetCursor()

    def _reset_progress_ui(self):
        self.progressBar.setRange(0, 4)
        self.progressBar.setValue(0)
        self._set_elided_progress_text("")

        # ---------- Full calibration (threaded) ----------

        # ... your existing __init__ and other methods ...
    @Slot()
    def start_full_calibration(self):
        if self._thread is not None:
            QMessageBox.information(self, "Already running", "Calibration is already in progress.")
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))

        params0 = getattr(self.hemi_page, "current_params", None)
        print("[CalibrationPage] hemi_page id =", id(self.hemi_page), "current_params =", params0)

        if not params0:
            QMessageBox.warning(
                self,
                "No parameters applied",
                "Please open the Hemisphere Motion page and press 'Apply Changes' first "
                "(this saves run_id + camera selection)."
            )
            return

        run_id = str(params0.get("run_id", "")).strip()
        if not run_id:
            QMessageBox.warning(self, "Missing Run ID", "Run ID is empty. Please set it in Hemisphere Motion page.")
            return

        # ✅ Ask checkerboard settings
        dlg = CalibrationPatternDialog(self)
        if dlg.exec() != QDialog.Accepted:
            return

        pattern_cfg = dlg.get_values()
        if pattern_cfg.get("pattern") != "checkerboard":
            QMessageBox.information(self, "Not implemented", "Charuco is not implemented yet.")
            return

        # ✅ Make a COPY of params and inject values
        params = dict(params0)
        params["calib_pattern"] = "checkerboard"
        params["nx"] = int(pattern_cfg["nx"])
        params["ny"] = int(pattern_cfg["ny"])
        params["square_size"] = float(pattern_cfg["square_size"])

        # -------------------------
        # Thread + worker creation
        # -------------------------
        self._thread = QThread(self)
        self._worker = CalibrationWorker(base_dir, params)   # ✅ use modified params
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.run)

        self._worker.progress.connect(self.handle_worker_progress)
        self._worker.finished.connect(self.handle_worker_finished)

        self._worker.finished.connect(self._thread.quit)
        self._thread.finished.connect(self._worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.finished.connect(self._clear_thread_refs)

        self._set_busy(True)
        self._reset_progress_ui()
        self._set_elided_progress_text("Starting calibration …")
        self._thread.start()

    @Slot()
    def _clear_thread_refs(self):
        """Called after QThread has finished."""
        self._thread = None
        self._worker = None

    @Slot(str)
    def handle_worker_progress(self, text: str):
        # Update progress bar using "Step X/4"
        m = re.search(r"Step\s+(\d+)\s*/\s*(\d+)", text)
        if m:
            step = int(m.group(1))
            total = int(m.group(2))
            self.progressBar.setRange(0, total)
            self.progressBar.setValue(step)

        self._set_elided_progress_text(text)

    @Slot(bool, str)
    def handle_worker_finished(self, success: bool, message: str):
        self._set_busy(False)

        if success:
            self.progressBar.setValue(self.progressBar.maximum())
        self._set_elided_progress_text(message)

        if success:
            QMessageBox.information(self, "Calibration finished", message + " 🎉")
        else:
            QMessageBox.critical(self, "Calibration failed", message)

        # Clear references only when thread is actually finished
        if self._thread is not None:
            self._thread.finished.connect(self._clear_thread_refs)

    def _clear_thread_refs(self):
        self._thread = None
        self._worker = None


    @Slot()
    def run_save_report_only(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        params = getattr(self.hemi_page, "current_params", None) or {}
        if not params:
            QMessageBox.warning(
                self,
                "No parameters applied",
                "Please open the Hemisphere Motion page and press 'Apply Changes' first."
            )
            return

        run_id = str(params.get("run_id", "")).strip()
        if not run_id:
            QMessageBox.warning(self, "Missing Run ID", "Run ID is empty. Please set it in Hemisphere Motion page.")
            return

        # --- read toggles (single source of truth) ---
        use_realsense = bool(params.get("use_realsense", False))
        use_webcam    = bool(params.get("use_webcam", False))
        use_zed_left  = bool(params.get("use_zed_left", False))
        use_zed_right = bool(params.get("use_zed_right", False))

        # Build cams list in a consistent order
        cams = []
        if use_zed_left:
            cams.append("zed_left_raw")
        if use_zed_right:
            cams.append("zed_right_raw")
        if use_realsense:
            cams.append("realsense")
        if use_webcam:
            cams.append("webcam")

        if not cams:
            QMessageBox.warning(self, "No cameras", "No cameras enabled. Enable at least one camera and try again.")
            return

        # "Only RealSense" special-case: use the RS report script, not multi-sensor
        only_realsense = use_realsense and (not use_webcam) and (not use_zed_left) and (not use_zed_right)
        rs_name = str(params.get("camera_name", "realsense")).strip() or "realsense"

        self._set_busy(True)
        self.progressBar.setRange(0, 1)
        self.progressBar.setValue(0)
        self._set_elided_progress_text("Creating calibration report …")

        try:
            runner = CalibrationWorker(base_dir, params)

            if only_realsense:
                # Use your realsense single-camera PDF generator
                runner._run_one(
                    "Creating RealSense calibration report …",
                    [
                        "python3",
                        "/root/ur_ws_sim/tools/realsense_calib/make_calibration_report.py",
                        "--base-dir", "/root/ur_ws_sim/data",
                        "--run-id", run_id,
                        "--camera-name", rs_name,
                    ],
                    cwd="/root/ur_ws_sim/tools/realsense_calib",
                )
            else:
                # Multi-sensor report REQUIRES --cams
                runner._run_one(
                    "Creating multi-sensor calibration report …",
                    [
                        "python3",
                        runner._script("generate_multi_sensor_report.py"),
                        "--base-dir", "/root/ur_ws_sim/data",
                        "--run-id", run_id,
                        "--cams", *cams,
                    ],
                    cwd=runner.SCRIPTS_DIR,
                )

            self.progressBar.setValue(1)

        except subprocess.CalledProcessError as e:
            traceback.print_exc()
            QMessageBox.critical(self, "Report failed", f"Report creation failed with exit code {e.returncode}.")
            return
        except Exception as e:
            traceback.print_exc()
            QMessageBox.critical(self, "Report error", f"Unexpected error while creating report:\n{e}")
            return
        finally:
            self._set_busy(False)
            self._set_elided_progress_text("Report created ✅")

        QMessageBox.information(self, "Report saved", "Calibration report created successfully ✅")


    def saveResults(self): 
        result_path = self.store_latest_calibration_result() 
        if result_path is not None: 
            self.show_info(f"Saved result as {result_path.name}") 
        else: 
            self.show_error("No calibration PDF found to save.")

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.procman = ProcGroupManager() 
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.params = {}
        self.procman.stop_all()
       
        self._managed_procs = []

        # -----------------------------
        # Top window buttons / menus
        # -----------------------------
        self.menuBtn.clicked.connect(self.toggle_menu)
        self.closeBtn.clicked.connect(self.close_window)
        self.minimizeBtn.clicked.connect(self.minimize_window)
        self.restoreBtn.clicked.connect(self.restore_window)

        self.helpBtn.clicked.connect(self.toggle_center_menu)
        self.pushButton.clicked.connect(self.close_center_menu)

        self.centerMenuContainer.setVisible(False)
        self.centralwidget.updateGeometry()

        # -----------------------------
        # Result explorer in center menu
        # -----------------------------
        self.result_explorer = ResultExplorerWidget(base_dir="/root/GUI", params=self.params, parent=self)


        #self.result_explorer = ResultExplorerWidget(self)
        self.verticalLayout_7.removeWidget(self.stackedWidget)
        self.stackedWidget.setParent(None)
        self.stackedWidget.deleteLater()
        self.stackedWidget = None
        # If anything is running, stop it first
        self.window()._kill_ros_leftovers()

        container_layout = self.centerMenuContainer.layout()
        if container_layout is None:
            container_layout = QVBoxLayout(self.centerMenuContainer)
            container_layout.setContentsMargins(10, 40, 10, 10)
        container_layout.addWidget(self.result_explorer)

        for lbl in self.centerMenuContainer.findChildren(QLabel):
            if lbl.text().strip().lower() == "result":
                lbl.hide()

                # ---- Create ConnectArmWidget first (it owns hemi_page)
        self.connect_arm_page = ConnectArmWidget()

        # Replace page_2 with ConnectArmWidget
        self.stackedWidget_2.removeWidget(self.page_2)
        self.page_2.deleteLater()
        self.stackedWidget_2.insertWidget(2, self.connect_arm_page)

        # ---- Now create pages that need hemi_page
        self.calibration = CalibrationPage(self.connect_arm_page.hemi_page)
        self.connect_camera_page = CameraMonitorWidget(self.connect_arm_page.hemi_page)

        # Replace page_3 with CalibrationPage
        self.stackedWidget_2.removeWidget(self.page_3)
        self.page_3.deleteLater()
        self.stackedWidget_2.insertWidget(0, self.calibration)

        # Replace page (camera) with CameraMonitorWidget
        self.stackedWidget_2.removeWidget(self.page)
        self.page.deleteLater()
        self.stackedWidget_2.insertWidget(1, self.connect_camera_page)


        #self.connect_arm_page = ConnectArmWidget()
        #self.calibration = CalibrationPage(self.connect_arm_page.hemi_page)
        #self.connect_camera_page = CameraMonitorWidget(self.connect_arm_page.hemi_page)

        #self.stackedWidget_2.removeWidget(self.page)
        #self.page.deleteLater()
        #self.stackedWidget_2.insertWidget(1, self.connect_camera_page)

        # ==========================================================
        # IMPORTANT: Create ConnectArmWidget FIRST (it owns hemi_page)
        # ==========================================================
        #self.connect_arm_page = ConnectArmWidget()

        # Replace page_2 (assumed index 2) with ConnectArmWidget
        #self.stackedWidget_2.removeWidget(self.page_2)
        #self.page_2.deleteLater()
        #self.stackedWidget_2.insertWidget(2, self.connect_arm_page)
        #self.procman = ProcGroupManager()
        # ==========================================================
        # Create CalibrationPage using the SAME HemiPage instance
        # ==========================================================
        # ConnectArmWidget must expose self.hemi_page (created in its __init__)
        #self.calibration = CalibrationPage(self.connect_arm_page.hemi_page)

        # Replace page_3 with CalibrationPage
        #self.stackedWidget_2.removeWidget(self.page_3)
        #self.page_3.deleteLater()
        #self.stackedWidget_2.insertWidget(0, self.calibration)

        # -----------------------------
        # Connect camera page (index 1)
        # -----------------------------
        #self.connect_camera_page = IntelRealsense()
        #self.stackedWidget_2.removeWidget(self.page)
        #self.page.deleteLater()
        #self.stackedWidget_2.insertWidget(1, self.connect_camera_page)

        # -----------------------------
        # Sidebar navigation buttons
        # -----------------------------
        self.connect_camera_sensorBtn.clicked.connect(lambda: self.switch_page(1))
        self.conntct_armBtn.clicked.connect(lambda: self.switch_page(2))
        self.calibrate_Btn.clicked.connect(lambda: self.switch_page(0))

    # -----------------------------
    # Window controls
    # -----------------------------
    def close_window(self):
        try:
            if hasattr(self, "driver_proc") and self.driver_proc is not None:
                if self.driver_proc.poll() is None:
                    os.killpg(self.driver_proc.pid, signal.SIGINT)
                    time.sleep(1.0)
                    if self.driver_proc.poll() is None:
                        os.killpg(self.driver_proc.pid, signal.SIGTERM)
                        time.sleep(1.0)
                    if self.driver_proc.poll() is None:
                        os.killpg(self.driver_proc.pid, signal.SIGKILL)
                self.driver_proc = None
        except Exception as e:
            print(f"[WARN] Failed to stop driver: {e}")

       
        try:
            if hasattr(self, "procman"):
                self.procman.stop_all()
        except Exception as e:
            print(f"[WARN] procman.stop_all failed: {e}")

        self._kill_ros_leftovers()
        self.close()

    def _shutdown_all_processes(self):
        # 1) Ctrl+C
        for p in self._managed_procs:
            if p.poll() is None:
                try:
                    os.killpg(p.pid, signal.SIGINT)
                except ProcessLookupError:
                    pass
        time.sleep(1.0)

        # 2) SIGTERM
        for p in self._managed_procs:
            if p.poll() is None:
                try:
                    os.killpg(p.pid, signal.SIGTERM)
                except ProcessLookupError:
                    pass
        time.sleep(1.0)

        # 3) SIGKILL
        for p in self._managed_procs:
            if p.poll() is None:
                try:
                    os.killpg(p.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass

        self._managed_procs.clear()

    def closeEvent(self, event):
            try:
                if hasattr(self, "procman"):
                    self.procman.stop_all()
                if hasattr(self, "calibration") and getattr(self.calibration, "_thread", None) is not None:
                    self.calibration._thread.quit()
                    self.calibration._thread.wait(1000)
            except Exception:
                pass
            self._shutdown_all_processes()
            self._kill_ros_leftovers()
            event.accept()


    def minimize_window(self):
        self.showMinimized()

    def restore_window(self):
        if self.isFullScreen():
            self.showNormal()
            self.is_maximized = False
        else:
            self.showFullScreen()
            self.is_maximized = True

    # -----------------------------
    # Menu logic
    # -----------------------------
    def toggle_menu(self):
        current_width = self.leftMenuContainer.width()
        new_width = 228 if current_width == 50 else 50
        self.leftMenuContainer.setFixedWidth(new_width)

    def toggle_center_menu(self):
        self.centerMenuContainer.setVisible(not self.centerMenuContainer.isVisible())

    def close_center_menu(self):
        self.centerMenuContainer.setVisible(False)

    # -----------------------------
    # Page switching
    # -----------------------------
    def switch_page(self, index):
        self.stackedWidget_2.setCurrentIndex(index)

    # -----------------------------
    # Process shutdown helpers
        # -----------------------------
    def _kill_ros_leftovers(self):
        

        # optional: clear FastDDS shm locks (prevents weird DDS issues next start)
        try:
            subprocess.call(["bash", "-lc", "rm -rf /dev/shm/fastrtps* /dev/shm/ros2*"])
        except Exception:
            pass

        patterns = [
            r"ros2 launch my_ur10e_scene_description scene.launch.py",
            r"ros2_control_node",
            r"rviz2",
            r"controller_manager/spawner",
            r"spawner --controller-manager",
            r"urscript_interface",
            r"robot_state_publisher",
        ]

        # Try graceful first
        for pat in patterns:
            subprocess.call(["pkill", "-SIGINT", "-f", pat])
        time.sleep(2)

        # Then terminate
        for pat in patterns:
            subprocess.call(["pkill", "-SIGTERM", "-f", pat])
        time.sleep(1)

        # Last resort
        for pat in patterns:
            subprocess.call(["pkill", "-SIGKILL", "-f", pat])

 


class ProcGroupManager:
    def __init__(self):
        self.procs = []

    def start(self, cmd: str, log_path="/tmp/gui_ros_launch.log"):
        logf = open(log_path, "a", buffering=1)
        p = subprocess.Popen(
            ["bash", "-lc", cmd],
            start_new_session=True,
            stdin=subprocess.DEVNULL,
            stdout=logf,
            stderr=subprocess.STDOUT,
            text=True
        )
        self.procs.append(p)
        return p

    def stop_all(self):
        def kill_group(p, sig):
            if p is None or p.poll() is not None:
                return
            try:
                os.killpg(os.getpgid(p.pid), sig)
            except ProcessLookupError:
                pass

        for sig, wait_s in [(signal.SIGINT, 2.0), (signal.SIGTERM, 2.0), (signal.SIGKILL, 1.0)]:
            for p in self.procs:
                kill_group(p, sig)
            t0 = time.time()
            while time.time() - t0 < wait_s:
                if not any(p.poll() is None for p in self.procs if p is not None):
                    break
                time.sleep(0.05)

        self.procs = [p for p in self.procs if p is not None and p.poll() is None]
