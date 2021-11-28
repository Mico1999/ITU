from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Lesson(Base):
    __tablename__ = 'lesson'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    study_field = Column(String)
    collections = relationship(
        "Collection", backref=backref("lesson")
    )

    def __repr__(self):
        return "<Lesson(name='%s', study_field='%s')>" % (
            self.name, self.study_field)


class Card(Base):
    __tablename__ = 'card'
    id = Column(Integer, primary_key=True)
    front_text = Column(String)
    back_text = Column(String)
    collections = relationship(
        "Collection", backref=backref("card")
    )

    def __repr__(self):
        return "<Card(front_text='%s', back_text='%s')>" % (
            self.front_text, self.back_text)


class Collection(Base):
    __tablename__ = 'collection'
    id = Column(Integer, primary_key=True)
    collection_id = Column(Integer)
    lesson_id = Column(Integer, ForeignKey("lesson.id"))
    card_id = Column(Integer, ForeignKey("card.id"))
