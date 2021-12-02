from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class MyQLabel(QLabel):
    def __init__(self):
        super(QLabel, self).__init__()
        self.setStyleSheet(LABEL_STYLING)
        self.setFont(QFont('Monaco', 20))

LABEL_STYLING="""
    QLabel{
        font: italic
    }
"""