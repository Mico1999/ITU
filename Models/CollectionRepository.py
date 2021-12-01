from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection
from sqlalchemy import and_


class CollectionRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert_collection(self, collection):
        try:
            get = self.get_collection_by_lesson_card_collection_name(collection)
        except:
            self.session.add(collection)  # if exists update

        # if exists update
        self.session.commit()

    def delete_collection(self, collection):
        try:
            self.get_collection_by_id(collection.id)
        except:
            raise Exception('Collection does not exists!')

        self.session.delete(collection)
        self.session.commit()

    def get_collection_by_id(self, _id):
        return self.session.query(Collection).filter(Collection.id == _id).one()

    def get_collection_by_lesson_card_collection_name(self, collection):
        return self.session.query(Collection)\
            .filter(and_(Collection.lesson_id == collection.lesson_id,
                    Collection.card_id == collection.card_id,
                    Collection.collection_name == collection.collection_name)).one()

    def get_all_lesson_collections(self, lesson):
        return self.session.query(Collection).filter(Collection.lesson_id == lesson.id)\
                        .group_by(Collection.collection_name).all()

    def get_all_collections(self):
        return self.session.query(Collection).all()

