from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Controllers.ModeratorController import ModeratorController
from Views.CollectionDetailView import CollectionDetailView

class CollectionDetailViewController:

    def __init__(self, main_window_controller, stacked_widget, collection_name):
        # Repositories
        self._lesson_repository = LessonRepository()
        self._collection_repository = CollectionRepository()
        self._card_repository = CardRepository()

        self._main_window_controller = main_window_controller
        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = ModeratorController()
        self.collection_name = collection_name

        self.cards = []  # All cards in current collection
        self.card_buttons = []
        # if collection_name:
            # todo self.cards = self._card_repository.get_all_cards_of_collection()

        self.setup_UI()

    def setup_UI(self):

        self._view = CollectionDetailView()

        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)

        self._view.grid.setContentsMargins(50, 40, 50, 20)

        if self.collection_name:
            self._view.main_header.setText(self.collection_name)
            self._view.collection_name_edit.setText(self.collection_name)

        # hide delete button if there is no lesson in detail view yet
        if not self._view.collection_name_edit.text():
            self._view.deleteButton.hide()
