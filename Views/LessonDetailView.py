from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING, ADD_BUTTON, WRONG_BUTTON, RIGHT_BUTTON
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLineEdit import MyQLineEdit
from Views.Templates.MyQLabel import MyQLabel
from Views.Templates.ScrollStyling import SCROLL_STYLING


class LessonDetailView(MyQDialog):

    def __init__(self):
        super(LessonDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.navigation_layout = QHBoxLayout()
        self.form_layout = QHBoxLayout()

        self.formGroupBox = QGroupBox()
        self.lesson_name_edit = MyQLineEdit()
        self.lesson_field_edit = MyQLineEdit()
        self.name_label = MyQLabel()
        self.field_label = MyQLabel()

        self.buttonLayout = QHBoxLayout()
        self.saveButton = QPushButton("Save")
        self.deleteButton = QPushButton("Delete lesson")
        self.homeButton = QPushButton("Home")

        self.scroll = QScrollArea()
        self.homeButton = QToolButton()
        
        self.grid = QGridLayout()
        self.add_button_layout = QHBoxLayout()
        self.addButton = QPushButton("Add collection")

        self.setup_ui()


    def setup_ui(self):
        """Setup the Add Lesson GUI."""

        self.grid.setContentsMargins(50, 0, 50, 0)
        self.grid.setSpacing(10)
        # setting button font
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Navigate home button
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setStyleSheet("background-color: grey")
        self.homeButton.setIconSize(QtCore.QSize(50, 50))

        self.navigation_layout.addWidget(self.homeButton)
        self.navigation_layout.setAlignment(Qt.AlignLeft)

        # Form labels and edits
        self.name_label.setText("Lesson Name:")
        self.lesson_name_edit.setObjectName("lesson_name_edit")
        self.field_label.setText("Lesson Field:")
        self.lesson_field_edit.setObjectName("study_field")

        # Lay out the data fields
        self.form_layout.addWidget(self.name_label)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.lesson_name_edit)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.field_label)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.lesson_field_edit)

        # set style of formGroupBox
        self.form_layout.setAlignment(Qt.AlignTop)
        self.formGroupBox.setLayout(self.form_layout)
        self.formGroupBox.setStyleSheet("QGroupBox{border-style: none;}")

        # Save lesson button
        self.saveButton.setFont(button_font)
        self.saveButton.setStyleSheet(RIGHT_BUTTON)
        self.saveButton.setIcon(QIcon(self.icon_path + 'save.png'))
        self.saveButton.setIconSize(QtCore.QSize(50, 50))

        # Delete lesson button
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(WRONG_BUTTON)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignCenter)

        # Adding widgets to layout
        self.layout.addLayout(self.navigation_layout)
        self.layout.setSpacing(30)
        self.layout.addWidget(self.formGroupBox)
        self.layout.setSpacing(30)
        self.layout.addLayout(self.buttonLayout)
        self.layout.setSpacing(30)

        # Add new collection button
        self.addButton.setStyleSheet(ADD_BUTTON)
        self.addButton.setIcon(QIcon(self.icon_path + 'plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))

        self.add_button_layout.addWidget(self.addButton)
        self.add_button_layout.setContentsMargins(50, 0, 0, 0)
        self.add_button_layout.setAlignment(Qt.AlignLeft)

        self.layout.addLayout(self.add_button_layout)

        self.widget = QWidget()  # Widget that contains the collection of Grid
        self.widget.setLayout(self.grid)
        self.widget.setStyleSheet("QWidget{background-color:  #FBF08A;}")

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.setStyleSheet(SCROLL_STYLING)

        self.layout.addWidget(self.scroll)
