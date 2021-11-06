##  Controllers/MainWindowController.py module
#   Implements the controller for the main view of app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from ITU.Views.MainWindow import *


class MainWindowController:

    def __init__(self, model, view):
        """Store instances of MainWindow model and view to controller."""
        self._model = model
        self._view = view
        self.add_dialog = None

        """Connect signals from view to particular slots in controller."""
        self._view.addButton.clicked.connect(self.Add_Lesson_Dialog)

    def Add_Lesson_Dialog(self):
        """Create instance of dialog window for adding new lessons."""
        self.add_dialog = Add_Lesson_DialogGUI(self._view)

        """Connect "OK" and "Cancel" signals from dialog window to slots."""
        self.add_dialog.buttonsBox.accepted.connect(self.Accept_Lesson)
        self.add_dialog.buttonsBox.rejected.connect(self.add_dialog.reject)   # rejection is made implicitly by QT
        self.add_dialog.exec()

    def Accept_Lesson(self):
        """Accpets data provided through form in dialog window."""
        self.add_dialog.data = []
        for form_field in (self.add_dialog.lesson_name, self.add_dialog.lesson_field):
            if not form_field.text():   # check if all fields of form are filled
                QMessageBox.critical(
                    self.add_dialog,
                    "Error!",
                    f"You must provide a lesson's {form_field.objectName()}",
                )
                self.add_dialog.data = None     # clear data in case of error
                return

            """Store text fields from dialog."""
            self.add_dialog.data.append(form_field.text())

        self.add_dialog.accept()    # close dialog window after user's form was accepted

        """Store dialog input to main view model and update main view."""
        self._model.AddLesson(self.add_dialog.data)
        self._view.table.resizeColumnsToContents()
