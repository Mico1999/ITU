from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection
from sqlalchemy import and_

class CollectionRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert_collection(self, collection):
        try:
            get = self.get_collection_by_lesson_card_collection_id(collection)
        except:
            self.session.add(collection)
            self.session.commit()
            return

        raise Exception('Collection already exists!')

    def delete_collection(self, collection):
        try:
            self.get_collection_by_id(collection.id)
        except:
            raise Exception('Collection does not exists!')

        self.session.delete(collection)
        self.session.commit()

    def get_collection_by_id(self, _id):
        return self.session.query(Collection).filter(Collection.id == _id).one()

    def get_collection_by_lesson_card_collection_id(self, collection):
        return self.session.query(Collection)\
            .filter(and_(Collection.lesson_id == collection.lesson_id,
                    Collection.card_id == collection.card_id,
                    Collection.collection_id == collection.collection_id)).one()

    def get_all_lesson_collections(self, lesson):
        return self.session.query(Collection).filter(Collection.lesson_id == lesson.id).all()

    def get_all_collections(self):
        return self.session.query(Collection).all()



