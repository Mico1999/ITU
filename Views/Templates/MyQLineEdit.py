from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class MyQLineEdit(QLineEdit):
    def __init__(self):
        super(MyQLineEdit, self).__init__()
        self.setStyleSheet(LINE_EDIT_STYLING)
        self.setFont(QFont("Monaco", 30))
        self.setMaxLength(30)

LINE_EDIT_STYLING="""
    QLineEdit{
        border-style: solid; 
        border-radius: 10px;
        padding: 10px;
        background-color: orange; 
    }
"""