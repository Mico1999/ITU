#   Views/CollectionDetailView.py module
#   Implements static layout of collection detail
#   @Authors Marek Miček (xmicek08), Peter Rúček (xrucek00), Marej Jurík (xjurik12)
#   @date 28.11.2021

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import sys
from Views.Templates.ButtonStyling import ADD_BUTTON, WRONG_BUTTON, \
    RIGHT_BUTTON, TOOL_STYLING, TEST_BUTTON, DELETE_BUTTON, SAVE_BUTTON
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLineEdit import MyQLineEdit
from Views.Templates.MyQLabel import MyQLabel
from Views.Templates.ScrollStyling import SCROLL_STYLING
from Views.Templates.CircularProgressBar import QRoundProgressBar


class CollectionDetailView(MyQDialog):

    def __init__(self):
        super(CollectionDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QHBoxLayout()

        self.collection_name_edit = MyQLineEdit()
        self.name_label = MyQLabel()

        self.navigation_layout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.backArrow = QToolButton()
        self.homeButton = QToolButton()
        self.saveButton = QPushButton(" Save")
        self.deleteButton = QPushButton(" Delete collection")
        self.testButton = QPushButton(" Test")

        self.scroll = QScrollArea()
        self.grid = QGridLayout()
        self.add_button_layout = QGridLayout()
        self.addButton = QPushButton(" Add card")

        self.result_layout = QHBoxLayout()
        self.bar = QRoundProgressBar()
        self.last_results_label = MyQLabel()
        self.result_label = MyQLabel()

        self.setup_UI()

    def setup_UI(self):
        self.grid.setContentsMargins(50, 0, 50, 0)
        self.grid.setSpacing(10)
        self.grid.setAlignment(Qt.AlignTop)

        # setting home and delete button
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
        self.form_layout.setContentsMargins(20, 0, 20, 0)

        # Save collection button
        self.saveButton.setFont(button_font)
        self.saveButton.setStyleSheet(SAVE_BUTTON)
        self.saveButton.setIcon(QIcon(self.icon_path + 'save.png'))
        self.saveButton.setIconSize(QtCore.QSize(50, 50))

        # Delete collection button
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(DELETE_BUTTON)
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
        self.buttonLayout.setContentsMargins(20, 0, 20, 0)
        self.buttonLayout.setAlignment(Qt.AlignRight)

        # Adding widgets to global layout
        self.layout.addLayout(self.navigation_layout)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.buttonLayout)

        # Add new card button
        self.addButton.setStyleSheet(ADD_BUTTON)
        self.addButton.setIcon(QIcon(self.icon_path + 'plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))
        self.add_button_layout.setSpacing(20)

        # Last results label
        self.last_results_label.setHidden(True)
        self.result_label.setHidden(True)

        # circular progress bar
        self.bar.setFixedSize(150, 150)
        self.bar.setDataPenWidth(3)
        self.bar.setOutlinePenWidth(3)
        self.bar.setDonutThicknessRatio(0.85)
        self.bar.setDecimals(0)
        self.bar.setFormat('%v / %m')
        self.bar.setNullPosition(90)
        self.bar.setBarStyle(QRoundProgressBar.StyleDonut)
        self.bar.setStyleSheet("QWidget{background-color: #FBF08A;"
                               "    color: orange;}")
        self.bar.setDataColors([(0., QtGui.QColor.fromRgb(255, 165, 0))])
        self.bar.setHidden(True)

        self.result_layout.setAlignment(Qt.AlignCenter)
        self.result_layout.setContentsMargins(20, 20, 0, 20)
        self.result_layout.addWidget(self.result_label, alignment=Qt.AlignRight)
        self.result_layout.addWidget(self.bar)
        self.result_layout.addWidget(self.last_results_label)
        self.layout.addLayout(self.result_layout)

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

        widget = QWidget()  # Widget that contains the collection of Grid
        widget.setLayout(self.grid)
        widget.setStyleSheet("QWidget{background-color:  #FBF08A;}")

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(widget)
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
