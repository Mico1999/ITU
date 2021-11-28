from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore


class LessonDetailView(QDialog):

    def __init__(self, lesson_name, study_field):
        super(LessonDetailView, self).__init__()
        self.setup_ui(lesson_name, study_field)

    def setup_ui(self, lesson_name, study_field):
        """Setup the Add Lesson GUI."""

        self.formGroupBox = QGroupBox("Form 1")

        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        form_layout = QFormLayout()
        # Create line edits for data fields
        self.lesson_name = QLineEdit()
        self.lesson_name.setText(lesson_name)
        self.lesson_name.setObjectName("lesson_name")
        self.lesson_field = QLineEdit()
        self.lesson_field.setText(study_field)
        self.lesson_field.setObjectName("study_field")

        # Lay out the data fields
        form_layout.addRow("Name:", self.lesson_name)
        form_layout.addRow("Study field:", self.lesson_field)
        self.formGroupBox.setLayout(form_layout)

        #Add standard buttons to the dialog (Ok/Cancel)
        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(self.buttonsBox)

