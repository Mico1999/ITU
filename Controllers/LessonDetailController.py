from Views.LessonDetailView import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from functools import partial
from Views.Templates.ButtonStyling import BUTTON_STYLING

from Models.DbEntities import Collection


class LessonDetailController:

    def __init__(self, view, lesson_name):
        """Store instances of repositories and  view to controller."""
        self._view = view
        self.collection_repo = CollectionRepository()
        self.lesson_repo = LessonRepository()
        self.card_repo = CardRepository()

        self.collections = []
        if lesson_name:
            lesson = self.lesson_repo.get_lesson_by_name(lesson_name)
            self.collections = self.collection_repo.get_all_lesson_collections(lesson)

        self.collection_buttons = []

        self.setup_ui()

    def setup_ui(self):
        self._view.grid.setContentsMargins(50, 40, 50, 20)

        index = 0
        column_finished = 0
        row = 0
        COLUMNS = 4
        self._view.grid.addWidget(self._view.addButton, 0, 0)
        for i in range(len(self.collections)):
            if (i % COLUMNS) == COLUMNS - 1:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            self.collection_buttons.append(QPushButton(str(self.collections[i].collection_name)))
            self.collection_buttons[index].setStyleSheet(BUTTON_STYLING)
            if row == 0:
                self._view.grid.addWidget(self.collection_buttons[index], 0, (i + 1) % COLUMNS)
            else:
                self._view.grid.addWidget(self.collection_buttons[index], row,  ((i - (COLUMNS - 1)) % COLUMNS))

            # TODO self.collection_buttons[index].clicked.connect()
            index = index + 1


        # Adding invisible buttons, so the has always COLUMNS columns
        empty_buttons = []
        index = 0
        for i in range(COLUMNS - 1, (column_finished % COLUMNS), -1):
            empty_buttons.append(QPushButton())
            policy = empty_buttons[index].sizePolicy()
            policy.setRetainSizeWhenHidden(True)
            empty_buttons[index].setSizePolicy(policy)
            self._view.grid.addWidget(empty_buttons[index], row, i)
            empty_buttons[index].hide()
            index = index + 1
