from Models.DbEntities import Card
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Views.CardDetailView import CardDetailView


class CardDetailViewController:

    def __init__(self, moderator, stacked_widget, id_of_collection, card_id):
        # Repositories
        self._card_repository = CardRepository()
        self._collection_repository = CollectionRepository()

        self._stacked_widget = stacked_widget

        # init moderator which will be dynamically calling controllers to override views if needed
        self._moderator = moderator
        self._moderator.add_card_detail_controller(self)

        self.collection = self._collection_repository.get_collection_by_id(id_of_collection)
        self.card = None
        if card_id:
            self.card = self._card_repository.get_card_by_id(card_id)

        self.setup_UI()
        self.connect()

    def setup_UI(self):
        self._view = CardDetailView()

        # add lesson detail view on stack
        self._stacked_widget.addWidget(self._view)

        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)


    def connect(self):
        # connect buttons from lesson detail views to slots
        # self._view.saveButton.clicked.connect(self.save_collection)
        # self._view.deleteButton.clicked.connect(self.delete_collection)
        self._view.homeButton.clicked.connect(self.redirect_home_action)
        self._view.backButton.clicked.connect(self.redirect_back_action)

    def redirect_home_action(self):
        """ redirect to home view when user clicked home button """

        # delete three views from stack, cause home view will be rendered again
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_main_window()

    def redirect_back_action(self):
        """ redirect to lesson detail view when user clicked delete button """

        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)
        self._stacked_widget.removeWidget(self._stacked_widget.widget(self._stacked_widget.currentIndex()))
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() - 1)

        # moderator will call lesson detail controller to render view
        self._moderator.switch_view_to_collection_detail_view()