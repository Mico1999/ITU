#   Views/TestView.py module
#   Implements static layout of test view
#   @Authors Peter Rúček (xrucek00), Marej Jurík (xjurik12)
#   @date 2.12.2021

from Views.Templates.ButtonStyling import TEST_VIEW_BUTTONS, WRONG_BUTTON, RIGHT_BUTTON
from Views.Templates.ProgressBarStyling import DEFAULT_STYLE
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLabel import MyQLabel


class TestView(MyQDialog):

    def __init__(self):
        super(TestView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.buttonLayoutTop = QHBoxLayout()
        self.progress = QProgressBar()
        self.cancelButton = QPushButton(" Cancel test")

        self.label_layout = QVBoxLayout()
        self.front_label = MyQLabel()
        self.back_label = MyQLabel()

        self.buttonLayoutBottom = QHBoxLayout()
        self.rightButton = QPushButton(" I know it")
        self.wrongButton = QPushButton(" I do not know it")
        self.flipButton = QPushButton(" Flip card")

        self.setup_UI()

    def setup_UI(self):
        button_font = QFont()
        button_font.setFamily("Monaco")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        self.progress.setGeometry(200, 80, 250, 20)
        self.progress.setStyleSheet(DEFAULT_STYLE)

        # Cancel test button
        self.cancelButton.setFont(button_font)
        self.cancelButton.setStyleSheet(TEST_VIEW_BUTTONS)
        self.cancelButton.setIcon(QIcon(self.icon_path + 'cancel.png'))
        self.cancelButton.setIconSize(QtCore.QSize(50, 50))

        self.front_label.setFont(QFont("Monaco", 40))
        self.front_label.setAlignment(QtCore.Qt.AlignCenter)
        self.back_label.setFont(QFont("Monaco", 40))
        self.back_label.setAlignment(QtCore.Qt.AlignCenter)

        # label should remain size when hidden
        policy = self.back_label.sizePolicy()
        policy.setRetainSizeWhenHidden(True)
        self.back_label.setSizePolicy(policy)
    
        self.label_layout.addWidget(self.front_label)
        self.label_layout.setSpacing(40)
        self.label_layout.addWidget(self.back_label)
        self.label_layout.setAlignment(Qt.AlignCenter)

        # Wrong button
        self.wrongButton.setFont(button_font)
        self.wrongButton.setStyleSheet(WRONG_BUTTON)
        self.wrongButton.setIcon(QIcon(self.icon_path + 'wrong.png'))
        self.wrongButton.setIconSize(QtCore.QSize(50, 50))

        # Flip button
        self.flipButton.setFont(button_font)
        self.flipButton.setStyleSheet(TEST_VIEW_BUTTONS)
        self.flipButton.setIcon(QIcon(self.icon_path + 'bulb.png'))
        self.flipButton.setIconSize(QtCore.QSize(50, 50))

        # Right button
        self.rightButton.setFont(button_font)
        self.rightButton.setStyleSheet(RIGHT_BUTTON)
        self.rightButton.setIcon(QIcon(self.icon_path + 'check.png'))
        self.rightButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayoutTop.addWidget(self.progress)
        self.buttonLayoutTop.setSpacing(20)
        self.buttonLayoutTop.addWidget(self.cancelButton)
        self.buttonLayoutTop.setAlignment(Qt.AlignCenter)

        self.buttonLayoutBottom.addWidget(self.wrongButton)
        self.buttonLayoutBottom.setSpacing(20)
        self.buttonLayoutBottom.addWidget(self.flipButton)
        self.buttonLayoutBottom.setSpacing(20)
        self.buttonLayoutBottom.addWidget(self.rightButton)
        self.buttonLayoutBottom.setAlignment(Qt.AlignVCenter)

        # Adding widgets to global layout
        self.layout.addLayout(self.buttonLayoutTop)
        self.layout.addLayout(self.label_layout)
        self.layout.addLayout(self.buttonLayoutBottom)

