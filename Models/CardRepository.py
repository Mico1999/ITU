from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection


class CardRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert_card(self, card):
        try:
            self.get_card_by_texts(card.front_text, card.back_text)
        except:
            self.session.add(card)

        self.session.commit()

    def delete_card(self, card):
        try:
            self.get_card_by_id(card.id)
        except:
            raise Exception('Card does not exists!')

        self.session.delete(card)
        self.session.commit()

    def get_card_by_id(self, _id):
        return self.session.query(Card).filter(Card.id == _id).one()

    def get_card_by_texts(self, front, back):
        return self.session.query(Card).filter(Card.front_text == front, Card.back_text == back).one()

    def get_all_cards(self):
        return self.session.query(Card).all()

    def get_all_collection_cards(self, collection_id):
        return self.session.query(Card).join(Collection).filter(Collection.id == collection_id).all()



