from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING
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
        self.arrow_layout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.backArrow = QToolButton()
        self.saveButton = QPushButton("Save")
        self.deleteButton = QPushButton("Delete card")
        self.homeButton = QPushButton("Home")

        self.setup_UI()

    def setup_UI(self):
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
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Save collection buttton
        self.saveButton.setFont(button_font)
        self.saveButton.setStyleSheet(BUTTON_STYLING)
        self.saveButton.setIcon(QIcon(self.icon_path + 'save.png'))
        self.saveButton.setIconSize(QtCore.QSize(50, 50))

        # Delete collection buttton
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(BUTTON_STYLING)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        # Navigate back button
        self.backArrow.setIcon(QIcon(self.icon_path + 'back-arrow.png'))
        self.backArrow.setIconSize(QtCore.QSize(50, 50))
        self.backArrow.setStyleSheet("background-color: blue")
        self.arrow_layout.addWidget(self.backArrow)
        self.arrow_layout.setAlignment(Qt.AlignLeft)

        # Navigate home button
        self.homeButton.setFont(button_font)
        self.homeButton.setStyleSheet(BUTTON_STYLING)
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.homeButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.backArrow)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignRight)

        self.navigation_layout.addLayout(self.arrow_layout)
        self.navigation_layout.addLayout(self.buttonLayout)

        # Adding widgets to layout
        self.layout.addWidget(self.formGroupBox)
        self.layout.addLayout(self.navigation_layout)
