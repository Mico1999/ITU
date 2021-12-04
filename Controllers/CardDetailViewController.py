#   Controllers/CardDetailViewController.py module
#   Implements the controller for the card detail view
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from PyQt5.QtWidgets import *
from Models.DbEntities import Card, Collection
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Views.CardDetailView import CardDetailView
from sqlalchemy.exc import NoResultFound


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

        # add card detail view on stack
        self._stacked_widget.addWidget(self._view)

        # increase index of stack to see detail view
        self._stacked_widget.setCurrentIndex(self._stacked_widget.currentIndex() + 1)

        # if card exists fill view with card's front and back text
        if self.card:
            self._view.card_front_edit.setText(self.card.front_text)
            self._view.card_back_edit.setText(self.card.back_text)

        # hide delete button if there is no card in detail view yet
        if not self._view.card_front_edit.text() and not self._view.card_back_edit.text():
            self._view.deleteButton.hide()

    def connect(self):
        # connect buttons from card detail views to slots
        self._view.saveButton.clicked.connect(self.save_card)
        self._view.deleteButton.clicked.connect(self.delete_card)
        self._view.homeButton.clicked.connect(self.redirect_home_action)
        self._view.backArrow.clicked.connect(self.redirect_back_action)

    def save_card(self):
        """ Stores new card user wants to create """
        # Card data from input
        card_front_string = self._view.card_front_edit.text()
        card_back_string = self._view.card_back_edit.text()

        if self.card:
            if card_front_string == self.card.front_text and \
                    card_back_string == self.card.back_text:
                self.redirect_back_action()
                return

        if not card_front_string or not card_back_string:
            QMessageBox.critical(None, "Error!", "Both card front and back page must be filled !")
            return

        new_card = Card(front_text=card_front_string, back_text=card_back_string, collection_id=self.collection.id)
        try:
            # Determine whether a card like this already exists for current collection
            # (throws NoResultFound if not)
            self._card_repository.get_collection_card_by_texts(new_card)
        except NoResultFound:
            # Can insert (update existing) to newly created card

            if self.card: # Related card was already pulled from the database and has unique ID assigned - UPDATE
                self.card.front_text = new_card.front_text
                self.card.back_text = new_card.back_text
                self._card_repository.insert_card(self.card)
            else:
                # Insert new (new card does not have an ID field yet)
                self._card_repository.insert_card(new_card)

            self.redirect_back_action()
            return

        # No exception raised - card like this already exists
        QMessageBox.critical(None, "Error!", "Can not add a card which already exists !")

    def delete_card(self):
        """ Deletes card on the user demand """
        # If card is still transient, it cannot be deleted
        if not self.card:
            return

        warning = QMessageBox.warning(
            None,
            "Warning!",
            "Do you want to delete this card completely ?\n \
                It can not be restored !",
            QMessageBox.Ok | QMessageBox.Cancel
        )

        if warning == QMessageBox.Ok:
            self._card_repository.delete_card(self.card)

            self.redirect_back_action()

    def redirect_home_action(self):
        """ redirect to home view when user clicked home button """

        # delete four views from stack, cause home view will be rendered again
        self._moderator.reduce_widget_stack(self._stacked_widget, 4)

        # moderator will call main window controller to render home view once again
        self._moderator.switch_view_to_main_window()

    def redirect_back_action(self):
        """ redirect to collection detail view when user clicked delete/back button """

        self._moderator.reduce_widget_stack(self._stacked_widget, 2)

        # moderator will call collection detail controller to render view
        self._moderator.switch_view_to_collection_detail_view()