from Views.LessonDetailView import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Controllers.LessonDetailController import LessonDetailController
from functools import partial


class MainWindowController:

    def __init__(self, view):
        """Store instances of repositories and  view to controller."""
        self._view = view

        self.collection_repo = CollectionRepository()
        self.lesson_repo = LessonRepository()
        self.card_repo = CardRepository()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("StudyDex")
        self.stacked_widget.addWidget(self._view)
        self.stacked_widget.resize(1000, 600)
        self.stacked_widget.show()

        self.setup_ui()

    def setup_ui(self):
        lessons = self.lesson_repo.get_all_lessons()
        lessonButtons = []
        index = 0
        column_finished = 0
        COLUMNS = 4
        row = 0
        self._view.grid.addWidget(self._view.addButton, 0, 0)
        for i in range(len(lessons)):
            if (i % COLUMNS) == COLUMNS - 1:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            self._view.grid.setColumnStretch(i % COLUMNS, 1)
            self._view.grid.setRowStretch(row, 1)

            lessonButtons.append(QPushButton(lessons[i].name))
            lessonButtons[index].setStyleSheet(self._view.button_style_sheet)
            if row == 0:
                self._view.grid.addWidget(lessonButtons[index], 0, (i + 1) % COLUMNS)
            else:
                self._view.grid.addWidget(lessonButtons[index], row, ((i - (COLUMNS - 1)) % COLUMNS))

            lessonButtons[index].clicked.connect(partial(self.add_lesson_view, lessons[i].name, lessons[i].study_field))
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

        """Connect signals from view to particular slots in controller."""
        self._view.addButton.clicked.connect(partial(self.add_lesson_view, None, None))

    def add_lesson_view(self, lesson_name, study_field):
        self.lessonDetailView = LessonDetailView(lesson_name, study_field)
        LessonDetailController(self.lessonDetailView, lesson_name)
        self.stacked_widget.addWidget(self.lessonDetailView)
        self.stacked_widget.setCurrentIndex(self.stacked_widget.currentIndex()+1)
