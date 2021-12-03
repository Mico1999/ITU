from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys
from Views.Templates.ButtonStyling import BUTTON_STYLING, ADD_BUTTON
from Views.Templates.ScrollStyling import SCROLL_STYLING
from Views.Templates.MyQLabel import MyQLabel


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.scroll = QScrollArea()
        self.grid = QGridLayout()
        self.centralWidget.setLayout(self.layout)
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'
        self.setMinimumWidth(1300)
        self.setMinimumHeight(800)
        self.add_button_layout = QGridLayout()
        self.addButton = QPushButton("Add lesson")
        self.label = QLabel()
        self.setStyleSheet("QMainWindow{background-color:  #FBF08A;}")

        self.setup_ui()

    def setup_ui(self):

        self.grid.setContentsMargins(50, 0, 50, 0)
        self.grid.setSpacing(10)
        self.grid.setAlignment(Qt.AlignTop)

        # set font for buttons
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)
        self.button_style_sheet = BUTTON_STYLING

        # Create buttons
        self.addButton.setFont(button_font)
        self.addButton.setStyleSheet(ADD_BUTTON)
        self.addButton.setIcon(QIcon(self.icon_path + 'plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))

        self.add_button_layout.setSpacing(20)
        self.add_button_layout.addWidget(self.addButton,0,0)

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

        self.add_button_layout.setContentsMargins(50, 0, 50, 20)

        # set font for header
        header_font = QFont()
        header_font.setFamily("Footlight MT Light")
        header_font.setPointSize(60)
        header_font.setBold(True)
        header_font.setWeight(50)

        # MainWindow header
        self.label.setText("StudyDex")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(header_font)
        self.label.setMargin(100)

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

        self.layout.addWidget(self.label)
        self.layout.addLayout(self.add_button_layout)
        self.layout.addWidget(self.scroll)
