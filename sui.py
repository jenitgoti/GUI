import sys
import subprocess
import time
import os

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTabWidget, QPushButton, QMainWindow
)
from PySide6.QtGui import QWindow
from PySide6.QtWidgets import QHBoxLayout, QFrame
from PySide6.QtCore import Qt

import Xlib.display



def get_window_id_by_name(name_substring):
    display = Xlib.display.Display()
    root = display.screen().root
    window_ids = root.query_tree().children

    for win in window_ids:
        try:
            name = win.get_wm_name()
            if name and name_substring in name:
                return win.id
        except:
            continue
    return None

class RealSenseTab(QWidget):
    def __init__(self):
        super().__init__()
        self.viewer_proc = None
        self.container = None

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button = QPushButton("Start RealSense Viewer")
        self.button.clicked.connect(self.launch_viewer)
        self.layout.addWidget(self.button)

        self.viewer_frame = QFrame()
        self.viewer_frame.setMinimumHeight(600)
        self.viewer_layout = QVBoxLayout(self.viewer_frame)
        self.layout.addWidget(self.viewer_frame)

    def launch_viewer(self):
        # Launch the RealSense Viewer
        self.viewer_proc = subprocess.Popen(["realsense-viewer"])
        time.sleep(2)  # Wait briefly to allow window to spawn

        win_id = get_window_id_by_name("RealSense Viewer")
        if not win_id:
            print("Failed to find RealSense Viewer window.")
            return

        window = QWindow.fromWinId(win_id)
        container = self.viewer_frame.layout().itemAt(0)
        if container:
            container.widget().deleteLater()

        self.container = QWidget.createWindowContainer(window)
        self.viewer_layout.addWidget(self.container)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RealSense Embedded Viewer GUI")
        self.resize(1000, 800)

        tabs = QTabWidget()
        self.setCentralWidget(tabs)

        self.tab1 = RealSenseTab()
        tabs.addTab(self.tab1, "Tab 1")

        # You can add more tabs here if needed
        tabs.addTab(QWidget(), "Tab 2")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
