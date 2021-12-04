from PyQt5.QtCore import QEventLoop
from Models.CollectionRepository import CollectionRepository
from Models.CardRepository import CardRepository
from Models.CollectionTestResultRepository import CollectionTestResultRepository
from Models.DbEntities import CollectionTestResult
from Views.TestView import TestView
from Controllers.TestResultsViewController import TestResultsViewController
import random


class TestViewController:

    def __init__(self, moderator, stacked_widget, id_of_collection):
        # Repositories
        self._collection_repository = CollectionRepository()
        self._card_repository = CardRepository()
        self._collection_test_result_repository = CollectionTestResultRepository()

        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_test_view_controller(self)

        self.cards = []  # All cards in current collection
        self.all_cards_count = 0

        self.collection = None
        if id_of_collection:
            self.collection = self._collection_repository.get_collection_by_id(id_of_collection)
            self.cards = self._card_repository.get_all_collection_cards(self.collection.id)

        self.test_results_controller = None

        self.testResults = {
            "correct": 0,
            "flipped": 0,
            "incorrect": 0
        }

        self.setup_UI()
        self.connect()

    def setup_UI(self):
        self._view = TestView()


        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)
        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
        random.shuffle(self.cards)

        self.all_cards_count = len(self.cards)

        # Reset test results
        self.testResults["correct"] = 0
        self.testResults["flipped"] = 0
        self.testResults["incorrect"] = 0

        self.next_card()

    def connect(self):
        self._view.cancelButton.clicked.connect(self.redirect_back_action)
        self._view.rightButton.clicked.connect(self.correct_answer)
        self._view.wrongButton.clicked.connect(self.wrong_answer)
        self._view.flipButton.clicked.connect(self.flipped_before_answer)

    def redirect_back_action(self):
        """ redirect to lesson detail view when user clicked delete button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 2)
        # moderator will call lesson detail controller to render view
        self._moderator.switch_view_to_collection_detail_view()

    def correct_answer(self):
        self.testResults["correct"] += 1
        self.next_card()

    def wrong_answer(self):
        self.testResults["incorrect"] += 1
        self.next_card()

    def flipped_before_answer(self):
        if self._view.back_label.isHidden():
            self.testResults["flipped"] += 1
        self.flip_card()

    def next_card(self):
        if self.cards:
            card = self.cards.pop()
            self._view.front_label.setText(card.front_text)
            self._view.back_label.setText(card.back_text)
            self._view.back_label.setHidden(True)
            fraction = (len(self.cards) + 1) / self.all_cards_count
            self._view.progress.setValue(100 - fraction*100)
            self._view.progress.setFormat(
                str(self.all_cards_count -1 - len(self.cards)) + "/" + str(self.all_cards_count)
            )
        else:
            self.conclude_test()

    def flip_card(self):
        self._view.back_label.setHidden(False)

    def conclude_test(self):
        # Save test results
        test_results_data = CollectionTestResult(
            cards=self.all_cards_count,
            correct_answers=self.testResults["correct"],
            times_flipped=self.testResults["flipped"],
            collection_id=self.collection.id)
        self._collection_test_result_repository.insert(test_results_data)

        # Render test results view
        self.test_results_controller = TestResultsViewController(
            self._moderator,
            self._stacked_widget,
            self.collection.collection_name,
            self.testResults)
