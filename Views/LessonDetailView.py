from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

class LessonDetailView(QDialog):

    def __init__(self, lesson_name, study_field):
        super(LessonDetailView, self).__init__()
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'
        self.setup_ui(lesson_name, study_field)

    def setup_ui(self, lesson_name, study_field):
        """Setup the Add Lesson GUI."""

        self.formGroupBox = QGroupBox()

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        form_layout = QHBoxLayout()

        # Create line edits for data fields
        self.name_label = QLabel()
        self.name_label.setText("Lesson Name:")
        self.lesson_name = QLineEdit()
        self.lesson_name.setText(lesson_name)
        self.lesson_name.setObjectName("lesson_name")

        self.field_label = QLabel()
        self.field_label.setText("Lesson Field:")
        self.lesson_field = QLineEdit()
        self.lesson_field.setText(study_field)
        self.lesson_field.setObjectName("study_field")

        self.saveButton = QPushButton("Save")

        # Lay out the data fields
        form_layout.addWidget(self.name_label)
        form_layout.setSpacing(20)
        form_layout.addWidget(self.lesson_name)
        form_layout.setSpacing(20)
        form_layout.addWidget(self.field_label)
        form_layout.setSpacing(20)
        form_layout.addWidget(self.lesson_field)
        form_layout.setSpacing(20)
        form_layout.addWidget(self.saveButton)

        # set style of formGroupBox
        form_layout.setAlignment(Qt.AlignTop)
        self.formGroupBox.setLayout(form_layout)

        # setting home and delete button
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
            "padding: 30px 15px; " \
            "}" \
            "QPushButton:pressed { " \
            "border-style: inset;" \
            "}" \
            "QPushButton:hover { " \
            "background-color: orange;" \
            "}"

        self.deleteButton = QPushButton("Delete lesson")
        self.deleteButton.setFont(button_font)
        self.deleteButton.setStyleSheet(self.button_style_sheet)
        self.deleteButton.setIcon(QIcon(self.icon_path + 'delete.png'))
        self.deleteButton.setIconSize(QtCore.QSize(50, 50))

        self.homeButton = QPushButton("Home")
        self.homeButton.setFont(button_font)
        self.homeButton.setStyleSheet(self.button_style_sheet)
        self.homeButton.setIcon(QIcon(self.icon_path + 'home.png'))
        self.homeButton.setIconSize(QtCore.QSize(50, 50))

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.homeButton)
        self.buttonLayout.setSpacing(20)
        self.buttonLayout.addWidget(self.deleteButton)
        self.buttonLayout.setAlignment(Qt.AlignRight)

        # set font for header
        header_font = QFont()
        header_font.setFamily("UnPilgia")
        header_font.setPointSize(35)
        header_font.setBold(True)
        header_font.setWeight(50)

        self.main_header = QLabel()
        self.main_header.setText(self.lesson_name.text())
        self.main_header.setFont(header_font)
        self.main_header.setAlignment(Qt.AlignCenter)

        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addLayout(self.buttonLayout)
        mainLayout.addWidget(self.main_header)

