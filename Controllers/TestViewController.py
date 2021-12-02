from PyQt5.QtCore import QEventLoop
from Models.CollectionRepository import CollectionRepository
from Models.CardRepository import CardRepository
from Views.TestView import TestView
import random


class TestViewController:

    def __init__(self, moderator, stacked_widget, id_of_collection):
        # Repositories
        self._collection_repository = CollectionRepository()
        self._card_repository = CardRepository()

        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_test_view_controller(self)

        self.cards = []  # All cards in current collection
        self.collection = None
        if id_of_collection:
            self.collection = self._collection_repository.get_collection_by_id(id_of_collection)
            self.cards = self._card_repository.get_all_collection_cards(self.collection.id)

        self.setup_UI()
        self.connect()

        self.next_card()

    def setup_UI(self):
        self._view = TestView()


        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)
        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        print("Test: ",len(self._stacked_widget))

        self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
        random.shuffle(self.cards)

    def connect(self):
        self._view.cancelButton.clicked.connect(self.redirect_back_action)
        self._view.rightButton.clicked.connect(self.next_card)
        self._view.wrongButton.clicked.connect(self.next_card)
        self._view.flipButton.clicked.connect(self.flip_card)

    def redirect_back_action(self):
        """ redirect to lesson detail view when user clicked delete button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 3)
        # moderator will call lesson detail controller to render view
        self._moderator.switch_view_to_collection_detail_view()

    def next_card(self):
        if self.cards:
            card = self.cards.pop()
            self._view.front_label.setText(card.front_text)
            self._view.back_label.setText(card.back_text)
            self._view.back_label.setHidden(True)
        else:
           self.redirect_back_action() 

    def flip_card(self):
        self._view.back_label.setHidden(False)
