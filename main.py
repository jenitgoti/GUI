from PySide6.QtWidgets import QApplication
from frontPage import MySideBar
import sys

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)

window = MySideBar()
window.show()

sys.exit(app.exec())


