from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Views.Templates.ButtonStyling import BUTTON_STYLING


class LessonDetailView(QDialog):

    def __init__(self, lesson_name, study_field):
        super(LessonDetailView, self).__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.form_layout = QFormLayout()
        self.formGroupBox = QGroupBox("Lesson")
        self.lesson_name = QLineEdit()
        self.lesson_field = QLineEdit()
        self.addButton = QPushButton("Add")
        self.grid = QGridLayout()

        self.setup_ui(lesson_name, study_field)

    def setup_ui(self, lesson_name, study_field):
        """Setup the Add Lesson GUI."""

        # Create line edits for data fields
        self.lesson_name.setText(lesson_name)
        self.lesson_name.setObjectName("lesson_name")

        self.lesson_field.setText(study_field)
        self.lesson_field.setObjectName("study_field")

        # Lay out the data fields
        self.form_layout.addRow("Name:", self.lesson_name)
        self.form_layout.addRow("Study field:", self.lesson_field)
        self.formGroupBox.setLayout(self.form_layout)

        self.layout.addWidget(self.formGroupBox)

        self.addButton.setStyleSheet(BUTTON_STYLING)
        self.addButton.setIcon(QIcon(r'Views\Assets\plus.png'))
        self.addButton.setIconSize(QtCore.QSize(50, 50))

        self.layout.addLayout(self.grid)
