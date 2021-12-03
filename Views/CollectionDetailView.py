from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLineEdit import MyQLineEdit
from Views.Templates.MyQLabel import MyQLabel


class CollectionDetailView(MyQDialog):

    def __init__(self):
        super(CollectionDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QHBoxLayout()

        self.formGroupBox = QGroupBox()
        self.collection_name_edit = MyQLineEdit()
        self.name_label = MyQLabel()

        self.main_header = MyQLabel()

        self.navigation_layout = QHBoxLayout()
        self.arrow_layout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.backArrow = QToolButton()
        self.saveButton = QPushButton("Save")
        self.deleteButton = QPushButton("Delete collection")
        self.homeButton = QPushButton("Home")
        self.testButton = QPushButton("Test")

        self.grid = QGridLayout()
        self.addButton = QPushButton("Add card")

        self.setup_UI()

    def setup_UI(self):

        # Form labels and edits
        self.name_label.setText("Collection Name:")
        self.collection_name_edit.setObjectName("collection_name_edit")

        # Lay out the data fields
        self.form_layout.addWidget(self.name_label)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.collection_name_edit)
        self.form_layout.setSpacing(20)
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

        # Test button
        self.testButton.setFont(button_font)
        self.testButton.setStyleSheet(BUTTON_STYLING)
        self.testButton.setIcon(QIcon(self.icon_path + 'test.png'))
        self.testButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.testButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.homeButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignRight)

        self.navigation_layout.addLayout(self.arrow_layout)
        self.navigation_layout.addLayout(self.buttonLayout)

        # set font for header
        header_font = QFont()
        header_font.setFamily("UnPilgia")
        header_font.setPointSize(35)
        header_font.setBold(True)
        header_font.setWeight(50)

        # Label with Collection name
        self.main_header.setFont(header_font)
        self.main_header.setAlignment(Qt.AlignCenter)

        # Adding widgets to layout
        self.layout.addWidget(self.formGroupBox)
        self.layout.addLayout(self.navigation_layout)
        self.layout.addWidget(self.main_header)

        # Add new card button
        self.addButton.setStyleSheet(BUTTON_STYLING)
        self.addButton.setIcon(QIcon(self.icon_path + 'plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))

        # Adding grid to layout
        self.layout.addLayout(self.grid)