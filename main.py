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
    QWidget, QListWidget, QListWidgetItem
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        list_widget = QListWidget()
        list_widget.addItems(["One", "Two", "Three"])

        list_widget.currentItemChanged.connect(self.item_changed)
        list_widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(list_widget)

    def item_changed(self, item: QListWidgetItem):
        print(item.text())

    def text_changed(self, text):
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
