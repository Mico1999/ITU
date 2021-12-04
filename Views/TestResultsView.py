#   Views/TestResultView.py module
#   Implements static layout of view with results from the last test
#   @Authors Peter Rúček (xrucek00), Marej Jurík (xjurik12)
#   @date 2.12.2021

from Views.Templates.ButtonStyling import BUTTON_STYLING, TOOL_STYLING, TEST_BUTTON
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
        self.buttonLayout = QHBoxLayout()

        self.homeButton = QToolButton()

        # Heading
        self.result_heading_layout = QVBoxLayout()
        self.result_heading = MyQLabel()

        # Test results
        self.test_result_layout = QVBoxLayout()
        self.test_result_correct = MyQLabel()
        self.test_result_flipped = MyQLabel()
        self.test_result_incorrect = MyQLabel()

        # Test result options
        self.retry_test_button = QPushButton("Retry test")
        self.finish_test_button = QPushButton("Finish test")

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

        self.navigation_layout.addWidget(self.homeButton)
        self.navigation_layout.setAlignment(Qt.AlignLeft)

        # Result heading text
        self.result_heading.setText("")

        result_heading_font = QFont()
        result_heading_font.setFamily("UnShinmun")
        result_heading_font.setBold(True)
        result_heading_font.setPointSize(36)

        self.result_heading.setFont(result_heading_font)
        self.result_heading.setStyleSheet(
            """
            QLabel {
                padding: 10px 20px;
                border: 2px solid black;
                border-radius: 5px;
            }
            """)

        result_heading_size_policy = QSizePolicy()
        result_heading_size_policy.setHorizontalPolicy(QSizePolicy.Maximum)
        result_heading_size_policy.setVerticalPolicy(QSizePolicy.Maximum)

        self.result_heading.setSizePolicy(result_heading_size_policy)
        self.result_heading.setAlignment(Qt.AlignCenter)

        self.result_heading_layout.addWidget(self.result_heading)
        self.result_heading_layout.setAlignment(Qt.AlignCenter)

        # Specific results' labels
        self.test_result_layout.addWidget(self.test_result_correct)
        self.test_result_layout.addWidget(self.test_result_flipped)
        self.test_result_layout.addWidget(self.test_result_incorrect)
        self.test_result_layout.setAlignment(Qt.AlignCenter)

        # Retry test button
        self.retry_test_button.setFont(button_font)
        self.retry_test_button.setStyleSheet(TEST_BUTTON)
        self.retry_test_button.setIcon(QIcon(self.icon_path + 'test.png'))
        self.retry_test_button.setIconSize(QtCore.QSize(50, 50))
        self.retry_test_button.setMinimumHeight(125)

        # finish button
        self.finish_test_button.setFont(button_font)
        self.finish_test_button.setStyleSheet(TEST_BUTTON)
        self.finish_test_button.setIcon(QIcon(self.icon_path + 'finish.png'))
        self.finish_test_button.setIconSize(QtCore.QSize(50, 50))
        self.finish_test_button.setMinimumHeight(125)

        self.buttonLayout.addWidget(self.retry_test_button)
        self.buttonLayout.setSpacing(25)
        self.buttonLayout.addWidget(self.finish_test_button)
        self.buttonLayout.setContentsMargins(150, 0, 150, 0)

        # Global layout setup
        self.layout.addLayout(self.navigation_layout)
        self.layout.addLayout(self.result_heading_layout)
        self.layout.addLayout(self.test_result_layout)
        self.layout.addLayout(self.buttonLayout)
