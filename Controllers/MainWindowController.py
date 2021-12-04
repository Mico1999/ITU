#   Controllers/MainWindowController.py module
#   Implements the controller for the main view of app
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

from Views.MainWindow import *
from Models.LessonRepository import LessonRepository
from Models.CardRepository import CardRepository
from Models.CollectionRepository import CollectionRepository
from Controllers.LessonDetailViewController import LessonDetailViewController
from Views.MainWindow import MainWindow
from functools import partial
from Controllers.ModeratorController import ModeratorController


class MainWindowController:

    def __init__(self):
        """Store instances of repositories controller and init stack of widgets."""
        self.collection_repo = CollectionRepository()
        self.lesson_repo = LessonRepository()
        self.card_repo = CardRepository()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("StudyDex")
        self.icon_path = 'Views/Assets/' if sys.platform.startswith('linux') else 'Views\\Assets\\'
        self.stacked_widget.setWindowIcon(QIcon(self.icon_path + 'hat.png'))
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
        row = 0
        for i in range(len(lessons)):
            if (i % COLUMNS) == 0:
                row = row + 1
                column_finished = 0
            else:
                column_finished = i

            lessonButtons.append(QPushButton(lessons[i].name))
            lessonButtons[index].setStyleSheet(self._view.button_style_sheet)
            lessonButtons[index].setMinimumSize(QSize(200, 100))
            lessonButtons[index].setMaximumSize(QSize(600, 100))

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
            empty_buttons[index].setMinimumSize(QSize(200, 100))
            empty_buttons[index].setMaximumSize(QSize(600, 100))
            self._view.grid.addWidget(empty_buttons[index], row, i)
            empty_buttons[index].hide()
            index = index + 1

        # Connect add lesson signal from view to particular slot in controller
        self._view.addButton.clicked.connect(partial(self.add_lesson_view, None))

    def add_lesson_view(self, lesson_name):
        """ Slot triggered when user clicked add lesson button on main home view """

        # render lesson detail view by calling it's controller
        self.lessonDetailViewController = LessonDetailViewController(self._moderator, self.stacked_widget, lesson_name)
