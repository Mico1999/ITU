from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class MyQDialog(QDialog):
    def __init__(self):
        super(MyQDialog, self).__init__()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            pass
        event.accept()
