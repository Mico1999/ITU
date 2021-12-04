#   Controllers/Seed.py module
#   Implements creation of data in tables
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from Models.CollectionRepository import *
from Models.CardRepository import *
from Models.LessonRepository import *
from Models.CollectionTestResultRepository import *


def seed():
    lesson_repo = LessonRepository()
    lesson_repo.insert_lesson(Lesson(name="Spanish", study_field="Language"))
    lesson_repo.insert_lesson(Lesson(name="Italian", study_field="Language"))
    lesson_repo.insert_lesson(Lesson(name="English", study_field="Language"))
    lesson_repo.insert_lesson(Lesson(name="Math", study_field="Math"))
    lesson_repo.insert_lesson(Lesson(name="Kosti ruky", study_field="Biology"))

    col_repo = CollectionRepository()
    col_repo.insert_collection(Collection(collection_name="1. lekcia", lesson_id=1))
    col_repo.insert_collection(Collection(collection_name="Číslovky", lesson_id=1))

    col_repo.insert_collection(Collection(collection_name="Basics", lesson_id=2))

    col_repo.insert_collection(Collection(collection_name="1. lekcia", lesson_id=3))

    col_repo.insert_collection(Collection(collection_name="Základne počty", lesson_id=4))

    col_repo.insert_collection(Collection(collection_name="Zápestné kosti", lesson_id=5))
    col_repo.insert_collection(Collection(collection_name="Kostra dlane", lesson_id=5))
    col_repo.insert_collection(Collection(collection_name="Články prstov", lesson_id=5))

    card_repo = CardRepository()
    card_repo.insert_card(Card(front_text="Ahoj", back_text="Hola", collection_id=1, remembered=True))
    card_repo.insert_card(Card(front_text="Dobry den", back_text="Buenos dias", collection_id=1, remembered=True))
    card_repo.insert_card(Card(front_text="Dobry noc", back_text="Buenas noches", collection_id=1, remembered=False))

    card_repo.insert_card(Card(front_text="1", back_text="Uno", collection_id=2, remembered=True))
    card_repo.insert_card(Card(front_text="2", back_text="Dos", collection_id=2, remembered=True))
    card_repo.insert_card(Card(front_text="3", back_text="Tres", collection_id=2, remembered=True))

    card_repo.insert_card(Card(front_text="Chalani", back_text="Ragazzi", collection_id=3, remembered=False))
    card_repo.insert_card(Card(front_text="Pizza", back_text="Pizza", collection_id=3, remembered=False))
    card_repo.insert_card(Card(front_text="Ahoj", back_text="Cao", collection_id=3, remembered=False))

    card_repo.insert_card(Card(front_text="2+2", back_text="4", collection_id=5, remembered=True))
    card_repo.insert_card(Card(front_text="6-3", back_text="3", collection_id=5, remembered=False))
    card_repo.insert_card(Card(front_text="5+3", back_text="8", collection_id=5, remembered=True))
    card_repo.insert_card(Card(front_text="2+3-5", back_text="0", collection_id=5, remembered=True))
    card_repo.insert_card(Card(front_text="3*2", back_text="6", collection_id=5, remembered=True))

    card_repo.insert_card(Card(front_text="Hrášková kosť", back_text="Os pisiforme", collection_id=6, remembered=True))
    card_repo.insert_card(Card(front_text="Trojhranná kosť", back_text="Os triquetrum", collection_id=6, remembered=True))
    card_repo.insert_card(Card(front_text="Mesiačková kosť", back_text="Os triquetrum", collection_id=6, remembered=True))
    card_repo.insert_card(Card(front_text="Člnkovitá kosť", back_text="Os scaphoideum", collection_id=6, remembered=True))

    card_repo.insert_card(Card(front_text="Báza článkov", back_text="Basis Phalangis", collection_id=8, remembered=False))
    card_repo.insert_card(Card(front_text="Telo článkov", back_text="Corpus Phalangis", collection_id=8, remembered=True))
    card_repo.insert_card(Card(front_text="Hlavice", back_text="Caput Phalangis", collection_id=8, remembered=True))

    collection_test_result_repo = CollectionTestResultRepository()
    collection_test_result_repo.insert(CollectionTestResult(
        cards=3, correct_answers=2, times_flipped=1, collection_id=1))
    collection_test_result_repo.insert(CollectionTestResult(
        cards=3, correct_answers=3, times_flipped=0, collection_id=2))
    collection_test_result_repo.insert(CollectionTestResult(
        cards=3, correct_answers=0, times_flipped=3, collection_id=3))
    collection_test_result_repo.insert(CollectionTestResult(
        cards=5, correct_answers=4, times_flipped=2, collection_id=5))
    collection_test_result_repo.insert(CollectionTestResult(
        cards=4, correct_answers=4, times_flipped=4, collection_id=6))
    collection_test_result_repo.insert(CollectionTestResult(
        cards=3, correct_answers=2, times_flipped=0, collection_id=8))
