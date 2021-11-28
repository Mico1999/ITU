##  Controllers/MainWindowController.py module
#   Implements the controller for the main view of app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from Views.MainWindow import *
from Views.LessonDetailView import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from functools import partial


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
        self._view.addButton.clicked.connect(self.add_lesson_view)

    def add_lesson_view(self, lesson_name, study_field):
        self.lessonDetailView = LessonDetailView(lesson_name, study_field)

        self.stacked_widget.addWidget(self.lessonDetailView)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex()+1)
