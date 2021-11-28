from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("StudyDex")
        self.resize(800, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()
        self.centralWidget.setLayout(self.layout)

        self.setup_ui()

    def setup_ui(self):

        self.grid.setContentsMargins(50, 40, 50, 20)

        # set font for buttons
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)
        self.button_style_sheet = \
            "QPushButton {" \
            "background-color:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 white, stop: 0.8 orange, stop:1 white);" \
            "border-style: outset;" \
            "border-width: 2px;" \
            "border-radius: 10px;" \
            "border-color: gray;" \
            "font: bold 14px;" \
            "min-width: 10em;" \
            "padding: 50px 20px; " \
            "}" \
            "QPushButton:pressed { " \
            "border-style: inset;" \
            "}" \
            "QPushButton:hover { " \
            "background-color: orange;" \
            "}"

        # Create buttons
        self.addButton = QPushButton("Add lesson")
        self.addButton.setFont(button_font)
        self.addButton.setStyleSheet(self.button_style_sheet)
        self.addButton.setIcon(QIcon(r'Views\Assets\plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))

        # set font for header
        header_font = QFont()
        header_font.setFamily("UnPilgia")
        header_font.setPointSize(35)
        header_font.setBold(True)
        header_font.setWeight(50)

        # MainWindow header
        self.label = QLabel()
        self.label.setText("StudyDex")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(header_font)

        self.layout.addWidget(self.label)
        self.layout.addLayout(self.grid)
