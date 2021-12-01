from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING


class CardDetailView(QDialog):

    def __init__(self):
        super(CardDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QHBoxLayout()

        self.formGroupBox = QGroupBox()
        self.card_front_edit = QLineEdit()
        self.card_back_edit = QLineEdit()
        self.front_label = QLabel()
        self.back_label = QLabel()

        self.buttonLayout = QHBoxLayout()
        self.saveButton = QPushButton("Save")
        self.deleteButton = QPushButton("Delete card")
        self.homeButton = QPushButton("Home")
        self.backButton = QPushButton("Back")

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

        # setting home and delete button
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Delete collection buttton
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(BUTTON_STYLING)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        # Navigate back button
        self.backButton.setFont(button_font)
        self.backButton.setStyleSheet(BUTTON_STYLING)
        self.backButton.setIcon(QIcon(self.icon_path + 'back-arrow.png'))
        self.backButton.setIconSize(QtCore.QSize(50, 50))

        # Navigate home button
        self.homeButton.setFont(button_font)
        self.homeButton.setStyleSheet(BUTTON_STYLING)
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.homeButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignRight)

        # Adding widgets to layout
        self.layout.addWidget(self.formGroupBox)
        self.layout.addLayout(self.buttonLayout)
