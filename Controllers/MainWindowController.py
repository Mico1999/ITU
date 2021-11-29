##  Controllers/MainWindowController.py module
#   Implements the controller for the main view of app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from Views.MainWindow import *
from Views.LessonDetailView import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Controllers.LessonDetailViewController import LessonDetailViewController
from functools import partial

from Models.DbEntities import Lesson, Card, Collection

class MainWindowController:

    def __init__(self, view):
        """Store instances of repositories and  view to controller."""
        self._view = view
        self.collection_repo = CollectionRepository()
        self.lesson_repo = LessonRepository()
        self.card_repo = CardRepository()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self._view)
        self.stacked_widget.show()

        # card1 = Card(front_text="Heloo", back_text="Ahoj")
        # card2 = Card(front_text="House", back_text="Dom")
        # card3 = Card(front_text="Gato", back_text="Mačka")
        # card4 = Card(front_text="Perro", back_text="Pes")
        #
        # collection1 = Collection(collection_id=1, lesson_id=1, card_id=1)
        # collection2 = Collection(collection_id=1, lesson_id=1, card_id=2)
        # collection3 = Collection(collection_id=2, lesson_id=2, card_id=3)
        # collection4 = Collection(collection_id=2, lesson_id=2, card_id=4)

        # self.card_repo.insert_card(card1)
        # self.card_repo.insert_card(card2)
        # self.card_repo.insert_card(card3)
        # self.card_repo.insert_card(card4)
        #
        # self.collection_repo.insert_collection(collection1)
        # self.collection_repo.insert_collection(collection2)
        # self.collection_repo.insert_collection(collection3)
        # self.collection_repo.insert_collection(collection4)

        # all_cards = self.card_repo.get_all_cards()
        # all_colls = self.collection_repo.get_all_collections()
        #
        # for card in all_cards:
        #     print(card.front_text, card.back_text)
        #
        # for cols in all_colls:
        #     print(cols.collection_id, cols.lesson_id, cols.card_id)
        #
        # exit()

        lessons = self.lesson_repo.get_all_lessons()
        lessonButtons = []
        index = 0

        self._view.grid.addWidget(self._view.addButton, 0, 0)
        for i in range(len(lessons)):
            r = int((4 % (i + 1)) / 4)
            self._view.grid.setColumnStretch(i % 4, 1)
            self._view.grid.setRowStretch(r, 1)
            lessonButtons.append(QPushButton(lessons[i].name))
            lessonButtons[index].setStyleSheet(self._view.button_style_sheet)
            if r == 0:
                self._view.grid.addWidget(lessonButtons[index], 0, i + 1)
            else:
                self._view.grid.addWidget(lessonButtons[index], r, i % 4)

            lessonButtons[index].clicked.connect(partial(self.add_lesson_view, lessons[i].name, lessons[i].study_field))
            index = index + 1

        """Connect signals from view to particular slots in controller."""
        self._view.addButton.clicked.connect(partial(self.add_lesson_view, None, None))

    def add_lesson_view(self, lesson_name, study_field):
        self.lessonDetailView = LessonDetailView(lesson_name, study_field)
        self.lessonDetailViewController = LessonDetailViewController(self.lessonDetailView, self.stacked_widget)

        self.stacked_widget.addWidget(self.lessonDetailView)

        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex()+1)
