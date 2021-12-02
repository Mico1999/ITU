from Models.DbEntities import *
from Models.CollectionRepository import *
from Models.CardRepository import *
from Models.LessonRepository import *


def seed():
    lesson_repo = LessonRepository()
    lesson_repo.insert_lesson(Lesson(name="Spanish", study_field="Language"))
    lesson_repo.insert_lesson(Lesson(name="Italian", study_field="Language"))
    lesson_repo.insert_lesson(Lesson(name="English", study_field="Language"))
    lesson_repo.insert_lesson(Lesson(name="Math", study_field="Math"))
    lesson_repo.insert_lesson(Lesson(name="Kosti ruky", study_field="Biology"))

    col_repo = CollectionRepository()
    col_repo.insert_collection(Collection(collection_name="1. lekcia ESP", lesson_id=1))
    col_repo.insert_collection(Collection(collection_name="Zaklady talianciny", lesson_id=2))
    col_repo.insert_collection(Collection(collection_name="1. lekcia ENG", lesson_id=3))
    col_repo.insert_collection(Collection(collection_name="+ do 10", lesson_id=4))
    col_repo.insert_collection(Collection(collection_name="Predlaktie", lesson_id=5))

    card_repo = CardRepository()
    card_repo.insert_card(Card(front_text="Ahoj", back_text="Hola", collection_id=1))
    card_repo.insert_card(Card(front_text="Pes", back_text="Perro", collection_id=2))
    card_repo.insert_card(Card(front_text="Hosani", back_text="Ragazzi", collection_id=3))
    card_repo.insert_card(Card(front_text="Arterie vertebralis", back_text="wtf", collection_id=4))
    card_repo.insert_card(Card(front_text="2+2", back_text="4", collection_id=5))
