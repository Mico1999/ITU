
#   Models/DbEntities.py module
#   Declaration of DB Tables/ Entities
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Lesson(Base):
    """
    Lesson mapping:
        Lesson -> one-to-many <- Collection
    """
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    study_field = Column(String)

    def __repr__(self):
        return "<Lesson(name='%s', study_field='%s')>" % (
            self.name, self.study_field)


class Collection(Base):
    """
    Collection mapping:
        Collection -> many-to-one <- Lesson
        Collection -> one-to-many <- Card

        Collection -> one-to-many <- CollectionTestResult
    """
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    collection_name = Column(String)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))

    def __repr__(self):
        return "<Collection(collection_name='%s')>" % (
            self.collection_name)


class CollectionTestResult(Base):
    """
    CollectionTestResult mapping:
        CollectionTestResult -> many-to-one <- Collection
    """
    __tablename__ = 'collection_test_result'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.now)
    cards = Column(Integer)
    correct_answers = Column(Integer)
    times_flipped = Column(Integer)
    collection_id = Column(Integer, ForeignKey("collection.id"))

    def __repr__(self):
        return f"<CollectionTestResult("\
                   f"date={self.date}, "\
                   f"cards={self.cards}, " \
                   f"correct_answers={self.correct_answers}, " \
                   f"times_flipped={self.times_flipped}" \
               f")>"


class Card(Base):
    """
    Card mapping:
        Card -> many-to-one <- Collection
    """
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    front_text = Column(String)
    back_text = Column(String)
    remembered = Column(Boolean, default=False)
    collection_id = Column(Integer, ForeignKey("collection.id"))

    def __repr__(self):
        return "<Card(front_text='%s', back_text='%s')>" % (
            self.front_text, self.back_text)
