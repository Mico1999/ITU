from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import sys
from Views.Templates.ButtonStyling import ADD_BUTTON, WRONG_BUTTON, RIGHT_BUTTON, TOOL_STYLING, TEST_BUTTON
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLineEdit import MyQLineEdit
from Views.Templates.MyQLabel import MyQLabel
from Views.Templates.ScrollStyling import SCROLL_STYLING


class CollectionDetailView(MyQDialog):

    def __init__(self):
        super(CollectionDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QHBoxLayout()

        # self.formGroupBox = QGroupBox()
        self.collection_name_edit = MyQLineEdit()
        self.name_label = MyQLabel()

        self.main_header = MyQLabel()

        self.navigation_layout = QHBoxLayout()
        self.arrow_layout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.backArrow = QToolButton()
        self.homeButton = QToolButton()
        self.saveButton = QPushButton("Save")
        self.deleteButton = QPushButton("Delete collection")
        self.testButton = QPushButton("Test")

        self.scroll = QScrollArea()
        self.grid = QGridLayout()
        self.add_button_layout = QGridLayout()
        self.addButton = QPushButton("Add card")

        self.setup_UI()

    def setup_UI(self):
        self.grid.setContentsMargins(50, 0, 50, 0)
        self.grid.setSpacing(10)
        self.grid.setAlignment(Qt.AlignTop)

        # setting home and delete button
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Navigate home button
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setStyleSheet(TOOL_STYLING)
        self.homeButton.setIconSize(QtCore.QSize(70, 70))
        self.homeButton.setToolTip('Home')

        # Navigate back button
        self.backArrow.setIcon(QIcon(self.icon_path + 'back-arrow.png'))
        self.backArrow.setIconSize(QtCore.QSize(70, 70))
        self.backArrow.setStyleSheet(TOOL_STYLING)
        self.backArrow.setToolTip('Back')

        self.navigation_layout.addWidget(self.backArrow)
        self.navigation_layout.addWidget(self.homeButton)
        self.navigation_layout.addStretch(0)
        self.navigation_layout.setContentsMargins(0, 0, 0, 0)
        self.navigation_layout.setSpacing(25)

        # Form labels and edits
        self.name_label.setText("Collection Name:")
        self.collection_name_edit.setObjectName("collection_name_edit")

        # Lay out the data fields
        self.form_layout.addWidget(self.name_label)
        self.form_layout.setSpacing(20)
        self.form_layout.addWidget(self.collection_name_edit)
        self.form_layout.setContentsMargins(0,0,0,0)
        self.form_layout.setAlignment(Qt.AlignBottom)
        # self.form_layout.setSpacing(20)
        # self.form_layout.setSpacing(20)
        # self.form_layout.addWidget(self.saveButton)

        # set style of formGroupBox
        self.form_layout.setAlignment(Qt.AlignTop)
        # self.formGroupBox.setLayout(self.form_layout)
        # self.formGroupBox.setStyleSheet("QGroupBox::title { "
        #                           "border: 0px ; "
        #                           "border-radius: 0px; "
        #                           "padding: 0px 0px 0px 0px;"
        #                           " margin = 0px 0px 0px 0px } "
        #                           "QGroupBox { "
        #                           "border: 0px ; "
        #                           "border-radius: 0px; "
        #                           "padding: 0px 0px 0px 0px;} ")
        # self.formGroupBox.setContentsMargins(0,0,0,0)

        # Save collection buttton
        self.saveButton.setFont(button_font)
        self.saveButton.setStyleSheet(RIGHT_BUTTON)
        self.saveButton.setIcon(QIcon(self.icon_path + 'save.png'))
        self.saveButton.setIconSize(QtCore.QSize(50, 50))

        # Delete collection buttton
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(WRONG_BUTTON)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        # Test button
        self.testButton.setFont(button_font)
        self.testButton.setStyleSheet(TEST_BUTTON)
        self.testButton.setIcon(QIcon(self.icon_path + 'test.png'))
        self.testButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.testButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.saveButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignRight)
        self.buttonLayout.setContentsMargins(0,0,0,0)

        # Adding widgets to layout
        self.layout.addLayout(self.navigation_layout)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.buttonLayout)

        # Add new card button
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
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.scroll.setStyleSheet(SCROLL_STYLING)

        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.scroll.setSizePolicy(sizePolicy)

        self.layout.addLayout(self.add_button_layout)
        self.layout.addWidget(self.scroll)
