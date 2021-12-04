#   Controllers/CollectionDetailViewController.py module
#   Implements the controller for the collection detail view
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from PyQt5 import QtGui
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Models.CollectionTestResultRepository import CollectionTestResultRepository
from Views.CollectionDetailView import CollectionDetailView
from PyQt5.QtWidgets import QMessageBox
from Models.DbEntities import Collection
from functools import partial
from Views.Templates.ButtonStyling import BUTTON_STYLING
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Controllers.CardDetailViewController import CardDetailViewController
from Views.Templates.MyButton import MyButton
from sqlalchemy.exc import NoResultFound
from Controllers.TestViewController import TestViewController


class CollectionDetailViewController:

    def __init__(self, moderator, stacked_widget, id_of_collection, lesson_id):
        # Repositories
        self._lesson_repository = LessonRepository()
        self._collection_repository = CollectionRepository()
        self._card_repository = CardRepository()
        self._collection_test_result_repository = CollectionTestResultRepository()

        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_collection_detail_controller(self)

        self._view = None

        self.cards = []  # All cards in current collection
        self.card_buttons = []
        self.collection = None
        self.lesson = None
        if id_of_collection:
            self.collection = self._collection_repository.get_collection_by_id(id_of_collection)
            self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
        if lesson_id:
            self.lesson = self._lesson_repository.get_lesson_by_id(lesson_id)

        self.test_controller = None
        self.latest_test_results = None

        self.setup_UI()
        self.connect()

    def setup_UI(self):

        self._view = CollectionDetailView()

        # add collection detail view on stack
        self._stacked_widget.addWidget(self._view)

        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        self.card_buttons = []
        self.cards = []
        if self.collection:
            self._view.collection_name_edit.setText(self.collection.collection_name)
            self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
            self._view.addButton.clicked.connect(partial(self.add_card_view, self.collection.id, None))

            # Show latest taken test's results
            self.latest_test_results = \
                self._collection_test_result_repository.get_latest_by_collection(self.collection) or None
            if self.latest_test_results:
                self._view.bar.setRange(0, self.latest_test_results.cards)
                self._view.bar.setValue(self.latest_test_results.correct_answers)
                self._view.bar.setHidden(False)
                self._view.result_label.setText("Last test result:")
                self._view.result_label.setHidden(False)
                self._view.last_results_label.setText(
                    f" Cards flipped {self.latest_test_results.times_flipped} times"
                )
                self._view.last_results_label.setHidden(False)

        # hide delete/add button if there is no collection in detail view yet
        if not self._view.collection_name_edit.text():
            self._view.deleteButton.hide()
            self._view.addButton.hide()

        # hide test button if there is no collection nor cards in detail view yet
        if not self.collection or not self.cards:
            self._view.testButton.hide()

        index = 0
        column_finished = 0
        row = 0
        COLUMNS = 4
        for i in range(len(self.cards)):
            if (i % COLUMNS) == 0:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            button = MyButton(self.cards[i].front_text, self.cards[i].back_text)
            self.card_buttons.append(button)
            self.card_buttons[index].setStyleSheet(BUTTON_STYLING)
            self.card_buttons[index].setMinimumSize(QSize(200, 100))
            self.card_buttons[index].setMaximumSize(QSize(600, 100))

            if not self.cards[index].remembered:
                shadow_effect = QGraphicsDropShadowEffect()
                shadow_effect.setColor(QtGui.QColor(255, 0, 0))
                shadow_effect.setOffset(2)
                shadow_effect.setBlurRadius(25)
                self.card_buttons[index].setGraphicsEffect(shadow_effect)

            self._view.grid.addWidget(self.card_buttons[index], row, (i % COLUMNS))

            self.card_buttons[index].clicked.connect(
                partial(self.add_card_view, self.collection.id, self.cards[index].id))
            index = index + 1

        # Adding invisible buttons, so the grid has always COLUMNS columns
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

    def add_card_view(self, collection_id, card_id):
        CardDetailViewController(self._moderator, self._stacked_widget, collection_id, card_id)

    def connect(self):
        """ Connect view with click in separate function"""

        # connect buttons from collection detail views to slots
        self._view.saveButton.clicked.connect(self.save_collection)
        self._view.deleteButton.clicked.connect(self.delete_collection)
        self._view.homeButton.clicked.connect(self.redirect_home_action)
        self._view.backArrow.clicked.connect(self.redirect_back_action)
        self._view.testButton.clicked.connect(self.test_action)

    def redirect_home_action(self):
        """ redirect to home view when user clicked home button """

        # delete three views from stack, cause home view will be rendered again
        self._moderator.reduce_widget_stack(self._stacked_widget, 3)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_main_window()

    def redirect_back_action(self):
        """ redirect to lesson detail view when user clicked delete/back button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 2)

        # moderator will call lesson detail controller to render view
        self._moderator.switch_view_to_lesson_detail_view()

    def save_collection(self):
        """ Stores new lesson user wants to create """
        # Lesson data from input
        collection_name_string = self._view.collection_name_edit.text()

        if self.collection:
            if collection_name_string == self.collection.collection_name:
                self.redirect_back_action()
                return

        if not collection_name_string:
            QMessageBox.critical(None, "Error!", "Collection name must be filled !")
            return

        # new collection can not be in DB already
        new_collection = Collection(collection_name=collection_name_string, lesson_id=self.lesson.id)
        try:
            collection_exists = self._collection_repository\
                .get_lesson_collection_by_name(new_collection)
        except NoResultFound:  # Insert it
            if self.collection:
                self.collection.collection_name = collection_name_string
                self._collection_repository.insert_collection(self.collection)
            else:
                self._collection_repository.insert_collection(new_collection)    # save new collection to DB

                # enable adding new card by clicking on add button without need to render this view once again
                self._view.addButton.show()
                self._view.deleteButton.show()
                self.actualize_current_working_collection(new_collection)

            self._view.addButton.clicked.connect(partial(self.add_card_view, self.collection.id, None))
            return

        # lesson already exists
        QMessageBox.critical(None, "Error!", "Can not add collection which already exists !")

    def delete_collection(self):
        """ Deletes collection on the user demand """
        # if collection is not set, we can not delete
        if not self.collection:
            return

        warning = QMessageBox.warning(None, "Warning!", "Do you want to delete this collection completely ?\n"
                                                        "This action can not be restored !",
                                      QMessageBox.Ok | QMessageBox.Cancel)

        if warning == QMessageBox.Ok:
            self._collection_repository.delete_collection(self.collection)

            self.redirect_back_action()

    def actualize_current_working_collection(self, new_collection):
        """
        Re-fetch a collection after inserting it to receive its generated ID
        (self.collection is also an indicator of whether the currently shown collection
            is being persisted or transient)
        """
        # store recently created collection
        self.collection = self._collection_repository.get_lesson_collection_by_name(new_collection)

    def test_action(self):
        self.test_controller = TestViewController(self._moderator, self._stacked_widget, self.collection.id)
