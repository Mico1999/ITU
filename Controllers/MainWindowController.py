##  Controllers/MainWindowController.py module
#   Implements the controller for the main view of app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from Views.MainWindow import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Controllers.LessonDetailViewController import LessonDetailViewController
from Views.MainWindow import MainWindow
from functools import partial
from Controllers.ModeratorController import ModeratorController

from Models.DbEntities import Lesson, Card, Collection

class MainWindowController:

    def __init__(self):
        """Store instances of repositories controller and init stack of widgets."""
        self.collection_repo = CollectionRepository()
        self.lesson_repo = LessonRepository()
        self.card_repo = CardRepository()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("StudyDex")
        self.stacked_widget.resize(1300, 600)

        # Register moderator
        self._moderator = ModeratorController()
        self._moderator.add_main_window_controller(self)

        self.setup_UI()

    def setup_UI(self):
        """Set up home view UI"""

        self._view = MainWindow()

        # add home view on stack
        self.stacked_widget.addWidget(self._view)
        self.stacked_widget.show()

        # add buttons with existing lessons to view grid
        lessons = self.lesson_repo.get_all_lessons()
        lessonButtons = []
        index = 0
        column_finished = 0
        COLUMNS = 4
        row = -1
        for i in range(len(lessons)):
            if (i % COLUMNS) == 0:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            self._view.grid.setColumnStretch(i % COLUMNS, 1)
            self._view.grid.setRowStretch(row, 1)

            lessonButtons.append(QPushButton(lessons[i].name))
            lessonButtons[index].setStyleSheet(self._view.button_style_sheet)
            self._view.grid.addWidget(lessonButtons[index], row, (i % COLUMNS))

            lessonButtons[index].clicked.connect(partial(self.add_lesson_view, lessons[i].name))
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

        # Connect add lesson signal from view to particular slot in controller
        self._view.addButton.clicked.connect(partial(self.add_lesson_view, None))

    def add_lesson_view(self, lesson_name):
        """ Slot triggered when user clicked add lesson button on main home view """

        # render lesson detail view by calling it's controller
        self.lessonDetailViewController = LessonDetailViewController(self._moderator, self.stacked_widget, lesson_name)
