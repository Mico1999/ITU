#   Controllers/TestResultsViewController.py module
#   Implements the controller for test results
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from Models.CollectionRepository import CollectionRepository
from Models.CardRepository import CardRepository
from Views.TestResultsView import TestResultsView


class TestResultsViewController:

    def __init__(self, moderator, stacked_widget, collection_name, results):
        # Repositories
        self._collection_repository = CollectionRepository()
        self._card_repository = CardRepository()

        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_test_results_view_controller(self)

        # Controlled view
        self._view = None

        # View data mapping fields
        self.collection_name = collection_name
        self._results = results

        self.setupUI()
        self.connect()

    def setupUI(self):
        self._view = TestResultsView()

        # add TestResultsView on stack
        self._stacked_widget.addWidget(self._view)
        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        # Current test results heading
        self._view.result_heading.setText(f"{self.collection_name}: Test Results")

        # Current test results result-data mapping
        self._view.test_result_correct.setText(f"Correct: {len(self._results.get('correct'))}")
        self._view.test_result_flipped.setText(f"Times flipped: {len(self._results.get('flipped'))}")
        self._view.test_result_incorrect.setText(f"Incorrect: {len(self._results.get('incorrect'))}")

    def connect(self):
        self._view.homeButton.clicked.connect(self.redirect_home_action)
        self._view.finish_test_button.clicked.connect(self.redirect_back_action)
        self._view.retry_test_button.clicked.connect(self.retry_test_action)

    def redirect_back_action(self):
        """ redirect to collection detail view when user clicked back button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 3)
        # moderator will call collection detail controller to render view
        self._moderator.switch_view_to_collection_detail_view()

    def redirect_home_action(self):
        """ redirect to home view when user clicked home button """

        # delete three views from stack, cause home view will be rendered again
        self._moderator.reduce_widget_stack(self._stacked_widget, 5)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_main_window()

    def retry_test_action(self):
        """ redirect to the test the results are being shown for """

        # Delete this view from stack
        self._moderator.reduce_widget_stack(self._stacked_widget, 2)

        # Call test controller to re-render it
        self._moderator.switch_view_to_test_view()


