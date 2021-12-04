#   Models/CollectionRepository.py module
#   Implements basic functions to work with the Collection table
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound


class CollectionRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert_collection(self, collection):
        try:
            get = self.get_lesson_collection_by_name(collection)
        except NoResultFound:
            self.session.add(collection)  # if exists update

        # if exists update
        self.session.commit()

    def delete_collection(self, collection):
        try:
            self.get_collection_by_id(collection.id)
        except NoResultFound:
            raise Exception('Collection does not exists!')

        self.session.delete(collection)
        self.session.commit()

    def get_collection_by_id(self, _id):
        return self.session.query(Collection).filter(Collection.id == _id).one()

    def get_lesson_collection_by_name(self, collection):
        return self.session.query(Collection)\
            .filter(and_(Collection.lesson_id == collection.lesson_id,
                    Collection.collection_name == collection.collection_name)).one()

    def get_all_lesson_collections(self, lesson):
        return self.session.query(Collection).filter(Collection.lesson_id == lesson.id)\
                        .group_by(Collection.collection_name).all()

    def get_all_collections(self):
        return self.session.query(Collection).all()

