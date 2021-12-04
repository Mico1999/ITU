#   Models/CollectionTestResultRepository.py module
#   Implements basic functions to work with the CollectionTestResult table
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection, CollectionTestResult
from sqlalchemy import and_, desc
from sqlalchemy.exc import NoResultFound


class CollectionTestResultRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert(self, test_result):
        self.session.add(test_result)
        self.session.commit()

    def delete(self, test_result):
        try:
            self.get_by_id(test_result.id)
        except NoResultFound:
            raise Exception('Collection test result does not exists!')

        self.session.delete(test_result)
        self.session.commit()

    def get_by_id(self, _id):
        return self.session.query(CollectionTestResult).filter(CollectionTestResult.id == _id).one()

    def get_by_collection(self, collection):
        pass

    def get_latest_by_collection(self, collection):
        return self.session.query(CollectionTestResult) \
            .filter(collection.id == CollectionTestResult.collection_id)\
            .order_by(desc(CollectionTestResult.date)).first()

    def get_all_collection_test_results(self, collection):
        return self.session.query(CollectionTestResult) \
            .filter(collection.id == CollectionTestResult.collection_id).all()

    def get_all(self):
        return self.session.query(CollectionTestResult).all()
