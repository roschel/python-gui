import sys

from PySide6.QtGui import QContextMenuEvent, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def contextMenuEvent(self, event: QContextMenuEvent):
        context = QMenu(self)
        context.addAction(QAction("teste 1", self))
        context.addAction(QAction("teste 2", self))
        context.addAction(QAction("teste 3", self))
        context.exec(event.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
