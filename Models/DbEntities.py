from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


""" 
Lesson mapping:
    Lesson -> one-to-many <- Collection
"""
class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    study_field = Column(String)

    def __repr__(self):
        return "<Lesson(name='%s', study_field='%s')>" % (
            self.name, self.study_field)


""" 
Collection mapping:
    Collection -> many-to-one <- Lesson
    Collection -> one-to-many <- Card
"""
class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    collection_name = Column(String)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))

    def __repr__(self):
        return "<Collection(collection_name='%s')>" % (
            self.collection_name)


"""
Card mapping:
    Card -> many-to-one <- Collection
"""
class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    front_text = Column(String)
    back_text = Column(String)
    collection_id = Column(Integer, ForeignKey("collection.id"))

    def __repr__(self):
        return "<Card(front_text='%s', back_text='%s')>" % (
            self.front_text, self.back_text)

