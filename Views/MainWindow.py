##  Views/MainWindow.py module
#   Implements the UI for the main view of app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from ITU.Views.UI_Designer.MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    """Main Window."""

    def __init__(self, model, parent=None):
        """Initializer."""
        super().__init__(parent)
        """
            Príklad použita zkompilovaného .UI súboru z QT designeru
            Vytvoria sa inštancie na triedy v module Views/UI_Designer
            Inštancie sa môžu robiť na celé views alebo len widgety
            No vygenrovany kód je neprehľadný a neefektivny, tak som radšej
            nepužíval tento spôsob...no do budúcna aspoň vieme ako
            
            UI_MainWin = Ui_MainWindow()
            UI_MainWin.setupUi(self)
        """

        self.setWindowTitle("StudyDex")
        self.resize(800, 600)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.MainViewModel = model

        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create the table view widget
        self.table = QTableView()
        self.table.setModel(self.MainViewModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # set font for buttons
        button_font = QFont()
        button_font.setFamily("UnShinmun")
        button_font.setPointSize(15)
        button_font.setBold(False)
        button_font.setWeight(50)

        # Create buttons
        self.addButton = QPushButton("Add lesson")
        self.addButton.setStyleSheet("background-color: #729FCF")
        self.addButton.setFont(button_font)

        self.deleteButton = QPushButton("Delete lesson")
        self.deleteButton.setStyleSheet("background-color: #729FCF")
        self.deleteButton.setFont(button_font)

        self.enterButton = QPushButton("Enter lesson")
        self.enterButton.setStyleSheet("background-color: #729FCF")
        self.enterButton.setFont(button_font)

        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.setStyleSheet("background-color: #729FCF")
        self.clearAllButton.setFont(button_font)

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

        # Lay out buttons of the MainWindow
        button_layout = QVBoxLayout()
        button_layout.addWidget(self.addButton)
        button_layout.addWidget(self.deleteButton)
        button_layout.addWidget(self.enterButton)
        button_layout.addStretch()
        button_layout.addWidget(self.clearAllButton)

        # Lay out table and header of the MainWindow
        table_layout = QVBoxLayout()
        table_layout.addWidget(self.label)
        table_layout.addWidget(self.table)

        # add both layouts to global layout
        self.layout.addLayout(table_layout)
        self.layout.addLayout(button_layout)

class Add_Lesson_DialogGUI(QDialog):
    """"GUI of dialog window for entering new lesson."""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Add new Lesson")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        """Setup the Add Lesson dialog's GUI."""
        # Create line edits for data fields
        self.lesson_name = QLineEdit()
        self.lesson_name.setObjectName("Name")
        self.lesson_field = QLineEdit()
        self.lesson_field.setObjectName("Study field")

        # Lay out the data fields
        layout = QFormLayout()
        layout.addRow("Name:", self.lesson_name)
        layout.addRow("Study field:", self.lesson_field)
        self.layout.addLayout(layout)

        # Add standard buttons to the dialog (Ok/Cancel)
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.layout.addWidget(self.buttonsBox)
