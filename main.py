import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QLabel, QToolBar, QStatusBar
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your Button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.on_my_toolbar_button_click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def on_my_toolbar_button_click(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec()
