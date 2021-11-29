from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Models.LessonRepository import LessonRepository
from Models.DbEntities import Lesson

class LessonDetailViewController:

    def __init__(self, view, stacked_widget):
        self._view = view
        self._stacked_widget = stacked_widget
        self._lesson_repository = LessonRepository()
        self._view.saveButton.clicked.connect(self.save_lesson)
        self._view.deleteButton.clicked.connect(self.delete_lesson)
        self._view.homeButton.clicked.connect(self.redirect_home_action)

        # hide delete button if there is no lesson in detail view yet
        if not self._view.lesson_name.text():
            self._view.deleteButton.hide()


    def save_lesson(self):
        self.lesson_name = self._view.lesson_name.text()
        self.lesson_field = self._view.lesson_field.text()

        if not self.lesson_name or not self.lesson_field:
            QMessageBox.critical(None, "Error!", "Both fields with lesson name and field must be filled !")
            return

        # new lesson can not be in DB already
        try:
            lesson_exists = self._lesson_repository.get_lesson_by_name(self.lesson_name)
        except:
            new_lesson = Lesson(name=self.lesson_name, study_field=self.lesson_field)
            self._lesson_repository.insert_lesson(new_lesson)    # save new lesson to DB
            self._view.main_header.setText(self.lesson_name)     # set main header of detail view as lesson name
            return

        # lesson already exists
        QMessageBox.critical(None, "Error!", "Can not add lesson which already exists !")

    def delete_lesson(self):

        warning = QMessageBox.warning(None, "Warning!", "Do you want to delete this lesson completely ?\n"
                                                        "This action can not be restored !",
                                      QMessageBox.Ok | QMessageBox.Cancel)

        if warning == QMessageBox.Ok:
            lesson_to_delete = self._lesson_repository.get_lesson_by_name(self._view.lesson_name.text())
            self._lesson_repository.delete_lesson(lesson_to_delete)
            self.redirect_home_action()

    def redirect_home_action(self):
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)


