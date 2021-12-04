from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class MyQLabel(QLabel):
    def __init__(self):
        super(QLabel, self).__init__()
        self.setFont(QFont("Monaco", 20))
