#   Models/CardRepository.py module
#   Implements basic functions to work with the Card table
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection
from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_


class CardRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert_card(self, card):
        try:
            self.get_card_by_id(card.id)
        except NoResultFound:
            self.session.add(card)

        self.session.commit()

    def update_card(self, card):
        self.session.add(card)
        self.session.commit()

    def delete_card(self, card):
        try:
            self.get_card_by_id(card.id)
        except NoResultFound:
            raise Exception('Card does not exists!')

        self.session.delete(card)
        self.session.commit()

    def get_card_by_id(self, _id):
        return self.session.query(Card).filter(Card.id == _id).one()

    def get_collection_card_by_texts(self, card):
        return self.session.query(Card).filter(
            and_(Card.front_text == card.front_text, Card.back_text == card.back_text),
            Card.collection_id == card.collection_id
        ).one()

    def get_all_cards(self):
        return self.session.query(Card).all()

    def get_all_collection_cards(self, collection_id):
        return self.session.query(Card).join(Collection).filter(Collection.id == collection_id).all()



