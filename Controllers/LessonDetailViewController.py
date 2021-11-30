from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Models.DbEntities import Lesson, Collection
from functools import partial
from Views.Templates.ButtonStyling import BUTTON_STYLING
from Models.DbEntities import Lesson
from Controllers.ModeratorController import ModeratorController
from Views.LessonDetailView import LessonDetailView

class LessonDetailViewController:

    def __init__(self, main_window_controller, stacked_widget, lesson_name):

        self._main_window_controller = main_window_controller
        self._stacked_widget = stacked_widget

        # Repositories
        self._lesson_repository = LessonRepository()
        self.collection_repository = CollectionRepository()
        self.card_repository = CardRepository()

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = ModeratorController()

        self.collections = [] # All collection in current lesson
        self.collection_buttons = []
        self.lesson = None # Current lesson
        if lesson_name:
            self.lesson = self._lesson_repository.get_lesson_by_name(lesson_name)
            self.collections = self.collection_repository.get_all_lesson_collections(self.lesson)

        self.setup_ui()
        self.connect()


    def connect(self):
        """ Connect view with click in separate function"""

        # connect buttons from lesson detail views to slots
        self._view.saveButton.clicked.connect(self.save_lesson)
        self._view.deleteButton.clicked.connect(self.delete_lesson)
        self._view.homeButton.clicked.connect(self.redirect_home_action)

    def save_lesson(self):
        """ Stores new lesson user wants to create """
        # Lesson data from input
        lesson_name_string = self._view.lesson_name_edit.text()
        lesson_field_string = self._view.lesson_field_edit.text()

        if not lesson_name_string or not lesson_field_string:
            QMessageBox.critical(None, "Error!", "Both fields with lesson name and field must be filled !")
            return

        # new lesson can not be in DB already
        try:
            lesson_exists = self._lesson_repository.get_lesson_by_name(lesson_name_string)
        except:
            new_lesson = Lesson(name=lesson_name_string, study_field=lesson_field_string)
            self._lesson_repository.insert_lesson(new_lesson)    # save new lesson to DB
            self._view.main_header.setText(lesson_name_string)     # set main header of detail view as lesson name
            return

        # lesson already exists
        QMessageBox.critical(None, "Error!", "Can not add lesson which already exists !")

    def delete_lesson(self):
        """ Deletes lesson on the user demand """
        # if lesson is not set, we can not delete
        if not self.lesson:
            return

        warning = QMessageBox.warning(None, "Warning!", "Do you want to delete this lesson completely ?\n"
                                                        "This action can not be restored !",
                                      QMessageBox.Ok | QMessageBox.Cancel)

        if warning == QMessageBox.Ok:
            lesson_to_delete = self._lesson_repository.get_lesson_by_name(self.lesson.name)
            self._lesson_repository.delete_lesson(lesson_to_delete)
            self.redirect_home_action()

    def redirect_home_action(self):
        """ redirect to home view when user clicked home button """

        # delete two views from stack => detail and home, cause home view will be rendered again
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_home(self._main_window_controller)

    def setup_ui(self):

        # render lesson detail view
        self._view = LessonDetailView()

        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)

        self._view.grid.setContentsMargins(50, 40, 50, 20)

        if self.lesson:
            self._view.main_header.setText(self.lesson.name)
            self._view.lesson_name_edit.setText(self.lesson.name)
            self._view.lesson_field_edit.setText(self.lesson.study_field)

        # hide delete button if there is no lesson in detail view yet
        if not self._view.lesson_name_edit.text():
            self._view.deleteButton.hide()

        index = 0
        column_finished = 0
        row = 0
        COLUMNS = 4
        self._view.grid.addWidget(self._view.addButton, 0, 0)
        for i in range(len(self.collections)):
            if (i % COLUMNS) == COLUMNS - 1:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            self.collection_buttons.append(QPushButton(str(self.collections[i].collection_name)))
            self.collection_buttons[index].setStyleSheet(BUTTON_STYLING)
            if row == 0:
                self._view.grid.addWidget(self.collection_buttons[index], 0, (i + 1) % COLUMNS)
            else:
                self._view.grid.addWidget(self.collection_buttons[index], row,  ((i - (COLUMNS - 1)) % COLUMNS))

            # TODO self.collection_buttons[index].clicked.connect()
            index = index + 1

        # Adding invisible buttons, so the has always COLUMNS columns
        empty_buttons = []
        index = 0
        for i in range(COLUMNS - 1, (column_finished % COLUMNS), -1):
            empty_buttons.append(QPushButton())
            policy = empty_buttons[index].sizePolicy()
            policy.setRetainSizeWhenHidden(True)
            empty_buttons[index].setSizePolicy(policy)
            self._view.grid.addWidget(empty_buttons[index], row, i)
            empty_buttons[index].hide()
            index = index + 1
