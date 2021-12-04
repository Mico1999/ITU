#   Views/CardDetailView.py module
#   Implements static layout of card detail
#   @Authors Marek Miček (xmicek08), Peter Rúček (xrucek00), Marej Jurík (xjurik12)
#   @date 1.12.2021

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING, RIGHT_BUTTON, WRONG_BUTTON, TOOL_STYLING
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLineEdit import MyQLineEdit
from Views.Templates.MyQLabel import MyQLabel


class CardDetailView(MyQDialog):

    def __init__(self):
        super(CardDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QHBoxLayout()

        self.formGroupBox = QGroupBox()
        self.card_front_edit = MyQLineEdit()
        self.card_back_edit = MyQLineEdit()
        self.front_label = MyQLabel()
        self.back_label = MyQLabel()

        self.navigation_layout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.backArrow = QToolButton()
        self.homeButton = QToolButton()
        self.saveButton = QPushButton(" Save")
        self.deleteButton = QPushButton(" Delete card")

        self.setup_UI()

    def setup_UI(self):

        # Navigate back button
        self.backArrow.setIcon(QIcon(self.icon_path + 'back-arrow.png'))
        self.backArrow.setIconSize(QtCore.QSize(70, 70))
        self.backArrow.setStyleSheet(TOOL_STYLING)
        self.backArrow.setToolTip('Back')

        # Navigate home button
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setStyleSheet(TOOL_STYLING)
        self.homeButton.setIconSize(QtCore.QSize(70, 70))
        self.homeButton.setToolTip('Home')

        self.navigation_layout.addWidget(self.backArrow)
        self.navigation_layout.addWidget(self.homeButton)
        self.navigation_layout.addStretch(0)
        self.navigation_layout.setContentsMargins(0, 0, 0, 0)
        self.navigation_layout.setSpacing(25)

        # Form labels and edits
        self.front_label.setText("Card front text:")
        self.card_front_edit.setObjectName("card_front_edit")

        self.back_label.setText("Card back text:")
        self.card_back_edit.setObjectName("card_back_edit")

        # Lay out the data fields
        self.form_layout.addWidget(self.front_label)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.card_front_edit)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.back_label)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.card_back_edit)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.saveButton)

        # set style of formGroupBox
        self.form_layout.setAlignment(Qt.AlignTop)
        self.formGroupBox.setLayout(self.form_layout)
        self.formGroupBox.setStyleSheet("QGroupBox{border-style: none;}")

        # setting home and delete button
        button_font = QFont()
        button_font.setFamily("Monaco")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Save collection button
        self.saveButton.setFont(button_font)
        self.saveButton.setStyleSheet(RIGHT_BUTTON)
        self.saveButton.setIcon(QIcon(self.icon_path + 'save.png'))
        self.saveButton.setIconSize(QtCore.QSize(50, 50))

        # Delete collection button
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(WRONG_BUTTON)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignCenter)

        # Adding widgets to global layout
        self.layout.addLayout(self.navigation_layout)
        self.layout.addWidget(self.formGroupBox)
        self.layout.addLayout(self.buttonLayout)