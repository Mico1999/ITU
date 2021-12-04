#   Controllers/DbConnection.py module
#   Implements connection to DB and creates tables
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from importlib import resources
from Models.DbEntities import Card, Lesson, Collection


class DbConnection:
    def __init__(self):
        with resources.path(
                "Database", "StudyDEX.sqlite"
        ) as sqlite_filepath:
            self.engine = create_engine(f"sqlite:///{sqlite_filepath}", echo=False)
        Session = sessionmaker(bind=self.engine)
        # ^^^^^ function pointer

        # Creating tables
        Lesson.metadata.create_all(self.engine)
        Card.metadata.create_all(self.engine)
        Collection.metadata.create_all(self.engine)

        self.session = Session()

    def get_session(self):
        return self.session
