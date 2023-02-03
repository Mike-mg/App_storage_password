"""
Entry program
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Storage")
        self.resize(800, 600)


app = QApplication(sys.argv)

window = Window()
window.show()


sys.exit(app.exec())
