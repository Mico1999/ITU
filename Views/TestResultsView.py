from Views.Templates.ButtonStyling import BUTTON_STYLING, WRONG_BUTTON, RIGHT_BUTTON, TOOL_STYLING
from Views.Templates.ProgressBarStyling import DEFAULT_STYLE
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Views.Templates.MyQDialog import MyQDialog
from Views.Templates.MyQLabel import MyQLabel


class TestResultsView(MyQDialog):
    def __init__(self):
        super(TestResultsView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Navigation
        self.navigation_layout = QHBoxLayout()
        self.arrow_layout = QHBoxLayout()
        self.buttonLayout = QHBoxLayout()

        self.backArrow = QToolButton()
        self.homeButton = QToolButton()

        # Heading
        self.result_heading = MyQLabel()

        # Test results
        self.test_result_layout = QVBoxLayout()
        self.test_result_correct = QLabel()
        self.test_result_flipped = QLabel()
        self.test_result_incorrect = QLabel()

        # Test result options
        self.retry_test_button = QPushButton("Retry test")

        self.setup_UI()

    def setup_UI(self):
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

        # Result heading text
        self.result_heading.setText("")
        self.result_heading.setAlignment(Qt.AlignCenter)

        # Specific results' labels
        self.test_result_layout.addWidget(self.test_result_correct)
        self.test_result_layout.addWidget(self.test_result_flipped)
        self.test_result_layout.addWidget(self.test_result_incorrect)
        self.test_result_layout.setAlignment(Qt.AlignCenter)

        # Retry test button
        self.retry_test_button.setFont(button_font)
        self.retry_test_button.setStyleSheet(BUTTON_STYLING)
        self.retry_test_button.setIcon(QIcon(self.icon_path + 'test.png'))
        self.retry_test_button.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout.addWidget(self.retry_test_button) # TODO RESIZE BUTON

        # Global layout setup
        self.layout.addLayout(self.navigation_layout)
        self.layout.addWidget(self.result_heading)
        self.layout.addLayout(self.test_result_layout)
        self.layout.addLayout(self.buttonLayout)