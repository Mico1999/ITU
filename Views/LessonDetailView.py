#   Views/LessonDetailView.py module
#   Implements static layout of lesson detail
#   @Authors Marek Miček (xmicek08), Peter Rúček (xrucek00)
#   @date 5.11.2021

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING, ADD_BUTTON,\
    WRONG_BUTTON, RIGHT_BUTTON, TOOL_STYLING, SAVE_BUTTON, DELETE_BUTTON
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

        self.lesson_name_edit = MyQLineEdit()
        self.lesson_field_edit = MyQLineEdit()
        self.name_label = MyQLabel()
        self.field_label = MyQLabel()

        self.buttonLayout = QHBoxLayout()
        self.saveButton = QPushButton(" Save")
        self.deleteButton = QPushButton(" Delete lesson")

        self.scroll = QScrollArea()
        self.homeButton = QToolButton()
        
        self.grid = QGridLayout()
        self.add_button_layout = QGridLayout()
        self.addButton = QPushButton(" Add collection")

        self.setup_ui()


    def setup_ui(self):
        """Setup the Add Lesson GUI."""

        self.grid.setContentsMargins(50, 0, 50, 0)
        self.grid.setSpacing(10)
        self.grid.setAlignment(Qt.AlignTop)

        # setting button font
        button_font = QFont()
        button_font.setFamily("Monaco")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Navigate home button
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setStyleSheet(TOOL_STYLING)
        self.homeButton.setIconSize(QtCore.QSize(70, 70))
        self.homeButton.setToolTip('Home')

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
        self.form_layout.setContentsMargins(20, 0, 20, 0)

        # Save lesson button
        self.saveButton.setFont(button_font)
        self.saveButton.setStyleSheet(SAVE_BUTTON)
        self.saveButton.setIcon(QIcon(self.icon_path + 'save.png'))
        self.saveButton.setIconSize(QtCore.QSize(50, 50))

        # Delete lesson button
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(DELETE_BUTTON)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setContentsMargins(20, 0, 20, 0)
        self.buttonLayout.setAlignment(Qt.AlignRight)

        # Adding widgets to global layout
        self.layout.addLayout(self.navigation_layout)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.buttonLayout)

        # Add new collection button
        self.addButton.setStyleSheet(ADD_BUTTON)
        self.addButton.setIcon(QIcon(self.icon_path + 'plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))

        self.add_button_layout.setSpacing(20)
        self.add_button_layout.addWidget(self.addButton, 0, 0)

        empty_buttons = []
        index = 0
        COLUMNS = 4
        for i in range(COLUMNS - 1, 0, -1):
            empty_buttons.append(QPushButton())
            policy = empty_buttons[index].sizePolicy()
            policy.setRetainSizeWhenHidden(True)
            empty_buttons[index].setSizePolicy(policy)
            self.add_button_layout.addWidget(empty_buttons[index], 0, i)
            empty_buttons[index].hide()
            index = index + 1

        self.add_button_layout.setContentsMargins(50, 0, 50, 0)

        self.widget = QWidget()  # Widget that contains the collection of Grid
        self.widget.setLayout(self.grid)
        self.widget.setStyleSheet("QWidget{background-color:  #FBF08A;}")

        # Scroll Area Properties
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.widget)
        self.scroll.setStyleSheet(SCROLL_STYLING)
        self.scroll.setMinimumHeight(330)

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.scroll.setSizePolicy(sizePolicy)

        button_widget = QWidget()
        button_widget.setLayout(self.add_button_layout)
        self.layout.addWidget(button_widget, alignment=Qt.AlignBottom)
        self.layout.addWidget(self.scroll, alignment=Qt.AlignBottom)
