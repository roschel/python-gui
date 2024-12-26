import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(800, 1000))

        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mousePressEvent LEFT")

        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")

        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif event.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif event.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
