from Views.Templates.ButtonStyling import BUTTON_STYLING, WRONG_BUTTON, RIGHT_BUTTON
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore


class TestView(QDialog):

    def __init__(self):
        super(TestView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QHBoxLayout()

        self.buttonLayoutTop = QHBoxLayout()
        self.cancelButton = QPushButton("Cancel test")

        self.label_layout = QVBoxLayout()
        self.front_label = QLabel()
        self.back_label = QLabel()

        self.buttonLayoutBottom = QHBoxLayout()
        self.rightButton = QPushButton("I know it")
        self.wrongButton = QPushButton("I do not know it")
        self.flipButton = QPushButton("Flip card")

        self.setup_UI()

    def setup_UI(self):
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Cancel test button
        self.cancelButton.setFont(button_font)
        self.cancelButton.setStyleSheet(BUTTON_STYLING)
        self.cancelButton.setIcon(QIcon(self.icon_path + 'cancel.png'))
        self.cancelButton.setIconSize(QtCore.QSize(50, 50))

        self.front_label.setFont(button_font)
        self.front_label.setAlignment(QtCore.Qt.AlignCenter)
        self.back_label.setFont(button_font)
        self.back_label.setAlignment(QtCore.Qt.AlignCenter)

        # label should remain size when hidden
        policy =  self.back_label.sizePolicy()
        policy.setRetainSizeWhenHidden(True)
        self.back_label.setSizePolicy(policy)
    
        self.label_layout.addWidget(self.front_label)
        self.label_layout.setSpacing(20)
        self.label_layout.addWidget(self.back_label)
        self.label_layout.setAlignment(Qt.AlignCenter)

        # Wrong button
        self.wrongButton.setFont(button_font)
        self.wrongButton.setStyleSheet(WRONG_BUTTON)
        self.wrongButton.setIcon(QIcon(self.icon_path + 'wrong.png'))
        self.wrongButton.setIconSize(QtCore.QSize(50, 50))

        # Flip button
        self.flipButton.setFont(button_font)
        self.flipButton.setStyleSheet(BUTTON_STYLING)
        self.flipButton.setIcon(QIcon(self.icon_path + 'bulb.png'))
        self.flipButton.setIconSize(QtCore.QSize(50, 50))

        # Right button
        self.rightButton.setFont(button_font)
        self.rightButton.setStyleSheet(RIGHT_BUTTON)
        self.rightButton.setIcon(QIcon(self.icon_path + 'check.png'))
        self.rightButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayoutTop.addWidget(self.cancelButton)
        self.buttonLayoutTop.setAlignment(Qt.AlignRight)

        self.buttonLayoutBottom.addWidget(self.wrongButton)
        self.buttonLayoutBottom.setSpacing(20)
        self.buttonLayoutBottom.addWidget(self.flipButton)
        self.buttonLayoutBottom.setSpacing(20)
        self.buttonLayoutBottom.addWidget(self.rightButton)
        self.buttonLayoutBottom.setAlignment(Qt.AlignVCenter)

        # Adding widgets to layout
        self.layout.addLayout(self.buttonLayoutTop)
        self.layout.addLayout(self.label_layout)
        self.layout.addLayout(self.buttonLayoutBottom)
