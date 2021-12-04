#   Controllers/TestViewController.py module
#   Implements the controller for test view
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

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
            "correct": [],
            "flipped": [],
            "incorrect": []
        }

        self.current_testing_card = None

        self.setup_UI()
        self.connect()

    def setup_UI(self):
        self._view = TestView()

        # add test view on stack
        self._stacked_widget.addWidget(self._view)
        # increase index of stack to see test view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        self.cards = self._card_repository.get_all_collection_cards(self.collection.id)
        random.shuffle(self.cards)
        self.all_cards_count = len(self.cards)

        # Reset test results
        self.testResults["correct"] = []
        self.testResults["flipped"] = []
        self.testResults["incorrect"] = []

        self.current_testing_card = self.cards.pop() # should not fail
        self.update_test_state()

    def connect(self):
        self._view.cancelButton.clicked.connect(self.redirect_back_action)
        self._view.rightButton.clicked.connect(self.correct_answer)
        self._view.wrongButton.clicked.connect(self.wrong_answer)
        self._view.flipButton.clicked.connect(self.flipped_before_answer)

    def redirect_back_action(self):
        """ redirect to collection detail view when user clicked delete button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 2)
        # moderator will call collection detail controller to render view
        self._moderator.switch_view_to_collection_detail_view()

    def correct_answer(self):
        if self.current_testing_card:
            self.testResults["correct"].append(self.current_testing_card)

        self.next_card()

    def wrong_answer(self):
        if self.current_testing_card:
            self.testResults["incorrect"].append(self.current_testing_card)

        self.next_card()

    def flipped_before_answer(self):
        if self.current_testing_card and self._view.back_label.isHidden():
            self.testResults["flipped"].append(self.current_testing_card)

        self.flip_card()

    def update_test_state(self):
        # Update UI
        self._view.front_label.setText(self.current_testing_card.front_text)
        self._view.back_label.setText(self.current_testing_card.back_text)
        self._view.back_label.setHidden(True)
        fraction = (len(self.cards) + 1) / self.all_cards_count
        self._view.progress.setValue(100 - fraction * 100)
        self._view.progress.setFormat(
            str(self.all_cards_count - 1 - len(self.cards)) + "/" + str(self.all_cards_count)
        )

    def next_card(self):
        """
        Update test state if not out of cards, else conclude test
        """

        # Select next testing card
        self.current_testing_card = self.cards.pop() if self.cards else None

        if self.current_testing_card:
            self.update_test_state()
        else:
            self.conclude_test()

    def flip_card(self):
        self._view.back_label.setHidden(False)

    def conclude_test(self):
        # Save test results
        test_results_data = CollectionTestResult(
            cards=self.all_cards_count,
            correct_answers=len(self.testResults["correct"]),
            times_flipped=len(self.testResults["flipped"]),
            collection_id=self.collection.id)
        self._collection_test_result_repository.insert(test_results_data)

        # Update card remembered state
        for unknown_card in self.testResults["incorrect"]:
            unknown_card.remembered = False
            self._card_repository.update_card(unknown_card)

        for remembered_card in self.testResults["correct"]:
            remembered_card.remembered = True
            self._card_repository.update_card(remembered_card)

        # Render test results view
        self.test_results_controller = TestResultsViewController(
            self._moderator,
            self._stacked_widget,
            self.collection.collection_name,
            self.testResults)
