from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Views.CollectionDetailView import CollectionDetailView
from PyQt5.QtWidgets import QMessageBox
from Models.DbEntities import Collection
from functools import partial
from Views.Templates.ButtonStyling import BUTTON_STYLING
from PyQt5.QtWidgets import *
from Controllers.CardDetailViewController import CardDetailViewController
from Views.Templates.MyButton import MyButton
from sqlalchemy.exc import NoResultFound


class CollectionDetailViewController:

    def __init__(self, moderator, stacked_widget, id_of_collection, lesson_id):
        # Repositories
        self._lesson_repository = LessonRepository()
        self._collection_repository = CollectionRepository()
        self._card_repository = CardRepository()

        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_collection_detail_controller(self)

        self.cards = []  # All cards in current collection
        self.card_buttons = []
        self.collection = None
        self.lesson = None
        if id_of_collection:
            self.collection = self._collection_repository.get_collection_by_id(id_of_collection)
            self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
        if lesson_id: # self.lesson cannot stay None
            self.lesson = self._lesson_repository.get_lesson_by_id(lesson_id)

        self.setup_UI()
        self.connect()

    def setup_UI(self):

        self._view = CollectionDetailView()

        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)

        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        self._view.grid.setContentsMargins(50, 40, 50, 20)

        if self.collection:
            self._view.main_header.setText(self.collection.collection_name)
            self._view.collection_name_edit.setText(self.collection.collection_name)

        self.card_buttons = []
        self.cards = []
        if self.collection:
            self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
            self._view.addButton.clicked.connect(partial(self.add_card_view, self.collection.id, None))

        # hide delete/add button if there is no collection in detail view yet
        if not self._view.collection_name_edit.text():
            self._view.deleteButton.hide()
            self._view.addButton.hide()

        # self._view.addButton.clicked.connect(partial(self.add_card_view, self.collection.id, None))
        index = 0
        column_finished = 0
        row = 0
        COLUMNS = 4
        self._view.grid.addWidget(self._view.addButton, 0, 0)
        for i in range(len(self.cards)):
            if (i % COLUMNS) == COLUMNS - 1:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            button = MyButton(self.cards[i].front_text, self.cards[i].back_text)
            self.card_buttons.append(button)

            self.card_buttons[index].setStyleSheet(BUTTON_STYLING)
            if row == 0:
                self._view.grid.addWidget(self.card_buttons[index], 0, (i + 1) % COLUMNS)
            else:
                self._view.grid.addWidget(self.card_buttons[index], row, ((i - (COLUMNS - 1)) % COLUMNS))

            self.card_buttons[index].clicked.connect(
                partial(self.add_card_view, self.collection.id, self.cards[index].id))
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

    def add_card_view(self, collection_id, card_id):
        CardDetailViewController(self._moderator, self._stacked_widget, collection_id, card_id)

    def connect(self):
        """ Connect view with click in separate function"""

        # connect buttons from lesson detail views to slots
        self._view.saveButton.clicked.connect(self.save_collection)
        self._view.deleteButton.clicked.connect(self.delete_collection)
        self._view.homeButton.clicked.connect(self.redirect_home_action)
        self._view.backButton.clicked.connect(self.redirect_back_action)

    def redirect_home_action(self):
        """ redirect to home view when user clicked home button """

        # delete three views from stack, cause home view will be rendered again
        self._moderator.reduce_widget_stack(self._stacked_widget, 3)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_main_window()

    def redirect_back_action(self):
        """ redirect to lesson detail view when user clicked delete button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 2)

        # moderator will call lesson detail controller to render view
        self._moderator.switch_view_to_lesson_detail_view()

    def save_collection(self):
        """ Stores new lesson user wants to create """
        # Lesson data from input
        collection_name_string = self._view.collection_name_edit.text()

        if not collection_name_string:
            QMessageBox.critical(None, "Error!", "Collection name must be filled !")
            return

        # new collection can not be in DB already
        new_collection = Collection(collection_name=collection_name_string, lesson_id=self.lesson.id)
        try:
            collection_exists = self._collection_repository\
                .get_lesson_collection_by_name(new_collection)
        except NoResultFound:  # Insert it
            self._view.main_header.setText(collection_name_string)  # set main header of detail view as collection name
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
