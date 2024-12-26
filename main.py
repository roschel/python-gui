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

        checkbox = QCheckBox("This is a checkbox")
        checkbox.setCheckState(Qt.CheckState.Checked)

        checkbox.stateChanged.connect(self.show_state)

        self.setCentralWidget(checkbox)

    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
