#   Controllers/LessonDetailViewController.py module
#   Implements the controller for the lesson detail view
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from functools import partial
from Views.Templates.ButtonStyling import BUTTON_STYLING
from Models.DbEntities import Lesson, Collection
from Views.LessonDetailView import LessonDetailView
from Controllers.CollectionDetailViewController import CollectionDetailViewController
from sqlalchemy.exc import NoResultFound


class LessonDetailViewController:

    def __init__(self, moderator, stacked_widget, lesson_name):

        self._stacked_widget = stacked_widget

        # Repositories
        self._lesson_repository = LessonRepository()
        self.collection_repository = CollectionRepository()
        self.card_repository = CardRepository()

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_lesson_detail_controller(self)

        self.collections = []  # All collection in current lesson
        self.collection_buttons = []
        self.lesson = None  # Current lesson
        if lesson_name:
            self.lesson = self._lesson_repository.get_lesson_by_name(lesson_name)
            self.collections = self.collection_repository.get_all_lesson_collections(self.lesson)

        self._view = None

        self.setup_UI()
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

        if self.lesson:
            if lesson_name_string == self.lesson.name and \
                    lesson_field_string == self.lesson.study_field:
                self.redirect_home_action()
                return

        if not lesson_name_string or not lesson_field_string:
            QMessageBox.critical(None, "Error!", "Both fields with lesson name and field must be filled !")
            return

        # new lesson can not be in DB already
        try:
            lesson_exists = self._lesson_repository.get_lesson_by_name(lesson_name_string)
        except NoResultFound:
            if self.lesson:
                # update
                self.lesson.name = lesson_name_string
                self.lesson.study_field = lesson_field_string
                self._lesson_repository.insert_lesson(self.lesson)
            else:  # insert
                new_lesson = Lesson(name=lesson_name_string, study_field=lesson_field_string)
                self._lesson_repository.insert_lesson(new_lesson)  # save new lesson to DB

                # enable adding new collection by clicking on add button without need to render this view once again
                self._view.addButton.show()
                self._view.deleteButton.show()
                # Actualize the currently shown lesson (re-fetch for generated ID after its insert)
                self.lesson = self._lesson_repository.get_lesson_by_name(lesson_name_string)

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
        self._moderator.reduce_widget_stack(self._stacked_widget, 2)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_main_window()

    def setup_UI(self):

        # render lesson detail view
        self._view = LessonDetailView()

        # For proper view rendering
        self.collection_buttons = []
        self.collections = []
        if self.lesson:
            self.collections = self.collection_repository.get_all_lesson_collections(self.lesson)
            self._view.lesson_name_edit.setText(self.lesson.name)
            self._view.lesson_field_edit.setText(self.lesson.study_field)

        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)

        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        # hide delete/add button if there is no lesson in detail view yet
        if not self._view.lesson_name_edit.text():
            self._view.deleteButton.hide()
            self._view.addButton.hide()

        # connect signal for adding new collection to slot
        self._view.addButton.clicked.connect(partial(self.add_collection_view, None))

        index = 0
        column_finished = 0
        COLUMNS = 4
        row = 0
        for i in range(len(self.collections)):
            if (i % COLUMNS) == 0:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            self.collection_buttons.append(QPushButton(str(self.collections[i].collection_name)))
            self.collection_buttons[index].setStyleSheet(BUTTON_STYLING)
            self.collection_buttons[index].setMinimumSize(QSize(200, 100))
            self.collection_buttons[index].setMaximumSize(QSize(600, 100))
            self._view.grid.addWidget(self.collection_buttons[index], row, (i % COLUMNS))

            self.collection_buttons[index].clicked.connect(
                partial(self.add_collection_view, self.collections[index].id))
            index = index + 1

        # Adding invisible buttons, so the has always COLUMNS columns
        empty_buttons = []
        index = 0
        for i in range(COLUMNS - 1, (column_finished % COLUMNS), -1):
            empty_buttons.append(QPushButton())
            policy = empty_buttons[index].sizePolicy()
            policy.setRetainSizeWhenHidden(True)
            empty_buttons[index].setSizePolicy(policy)
            empty_buttons[index].setMinimumSize(QSize(200, 100))
            empty_buttons[index].setMaximumSize(QSize(600, 100))
            self._view.grid.addWidget(empty_buttons[index], row, i)
            empty_buttons[index].hide()
            index = index + 1

    def add_collection_view(self, id_of_collection):
        """ Slots which catches signal for creating new collection """

        # render collection detail view by calling it's controller
        self.collectionDetailViewController = \
            CollectionDetailViewController(
                self._moderator,
                self._stacked_widget,
                id_of_collection,
                self.lesson.id)
