#   Controllers/ModeratorController.py module
#   Implements the controller moderator
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

class ModeratorController:
    """ Calls functions of view controllers to dynamically change views on the basis of triggered actions"""

    def __init__(self):
        self.main_window_controller = None
        self.lesson_detail_controller = None
        self.collection_detail_controller = None
        self.card_detail_controller = None
        self.test_view_controller = None
        self.test_view_results_controller = None

    # register this function in constructor of corresponding controller
    def add_main_window_controller(self, main_window_controller):
        self.main_window_controller = main_window_controller

    def add_lesson_detail_controller(self, lesson_detail_controller):
        self.lesson_detail_controller = lesson_detail_controller

    def add_collection_detail_controller(self, collection_detail_controller):
        self.collection_detail_controller = collection_detail_controller

    def add_card_detail_controller(self, card_detail_controller):
        self.card_detail_controller = card_detail_controller

    def add_test_view_controller(self, test_view_controller):
        self.test_view_controller = test_view_controller

    def add_test_results_view_controller(self, test_results_vie_controller):
        self.test_view_results_controller = test_results_vie_controller

    # to switch view just call this functions
    def switch_view_to_main_window(self):
        # setup home view once again to see changes
        self.main_window_controller.setup_UI()

    def switch_view_to_lesson_detail_view(self):
        self.lesson_detail_controller.setup_UI()
        self.lesson_detail_controller.connect()

    def switch_view_to_collection_detail_view(self):
        self.collection_detail_controller.setup_UI()
        self.collection_detail_controller.connect()

    def switch_view_to_card_detail_view(self):
        self.card_detail_controller.setup_UI()
        self.card_detail_controller.connect()

    def switch_view_to_test_view(self):
        self.test_view_controller.setup_UI()
        self.test_view_controller.connect()

    def reduce_widget_stack(self, stacked_widget, reduction_level):
        """ Pops from widget stack to switch among views """

        for i in range(reduction_level):
            stacked_widget.removeWidget(stacked_widget.widget(stacked_widget.currentIndex()))
