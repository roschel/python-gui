import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QTimeEdit,
    QSpinBox,
    QSlider,
    QRadioButton,
    QPushButton,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLCDNumber,
    QLabel,
    QLineEdit,
    QProgressBar,
    QWidget
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        combobox = QComboBox()
        combobox.addItems(["One", "Two", "Three"])

        combobox.currentIndexChanged.connect(self.index_changed)
        combobox.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(combobox)

    def index_changed(self, index):
        print(index)

    def text_changed(self, text):
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
