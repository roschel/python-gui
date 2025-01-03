import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow, QLabel, QToolBar, QStatusBar, QCheckBox
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)

        button_action = QAction(QIcon('bug.png'), "&Your Button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.on_my_toolbar_button_click)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action_2 = QAction(QIcon('bug.png'), "Your &Button2", self)
        button_action_2.setStatusTip("This is your button2")
        button_action_2.triggered.connect(self.on_my_toolbar_button_click)
        button_action_2.setCheckable(True)
        toolbar.addAction(button_action_2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def on_my_toolbar_button_click(self, s):
        print("click", s)


app = QApplication(sys.argv)

window = MainWindow()
window.showMaximized()

app.exec()
