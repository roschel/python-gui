import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 1000))

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    def mouseMoveEvent(self, event: QMouseEvent):
        self.label.setText("mouseMoveEvent")
        print(event.globalX(), event.globalY(), event.buttons())

    def mousePressEvent(self, event):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, event):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, event):
        self.label.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
