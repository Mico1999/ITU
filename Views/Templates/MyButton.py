from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Views.Templates.ButtonStyling import HOVER_BUTTON, BUTTON_STYLING


class MyButton(QPushButton):
    leftclicked = pyqtSignal()

    def __init__(self, front_text, back_text):
        super(MyButton, self).__init__(front_text)
        self._front_text = front_text
        self._back_text = back_text
        self.event(QEvent(QtCore.QEvent.HoverMove))

    def mousePressEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            self.leftclicked.emit()
        QPushButton.mousePressEvent(self, ev)

    def enterEvent(self, event):
        super().enterEvent(event)
        self.setStyleSheet(HOVER_BUTTON)
        self.setText(self._back_text)

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setStyleSheet(BUTTON_STYLING)
        self.setText(self._front_text)
