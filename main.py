import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget, QListWidgetItem, QLineEdit
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(10)
        self.line_edit.setPlaceholderText("Enter yout text")

        # widget.setReadOnly(True) # uncomment this to make readonly

        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        self.setCentralWidget(self.line_edit)

    def text_changed(self, text):
        print(f"Text changed to... {text}")

    def return_pressed(self):
        print("return_pressed")
        self.line_edit.setText("BOOM!")

    def selection_changed(self):
        print("selection_changed")
        print(self.line_edit.selectedText())

    def text_edited(self, text):
        print(f"Text edited to... {text}")
        print(text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
