

class ModeratorController:
    """ Calls functions of view controllers to dynamically change views on the basis of triggered actions"""

    def __init__(self):
        self.main_window_controller = None
        self.lesson_detail_controller = None
        self.collection_detail_controller = None
        self.card_detail_controller = None

    # register this function in constructor of corresponding controller
    def add_main_window_controller(self, main_window_controller):
        self.main_window_controller = main_window_controller

    def add_lesson_detail_controller(self, lesson_detail_controller):
        self.lesson_detail_controller = lesson_detail_controller

    def add_collection_detail_controller(self, collection_detail_controller):
        self.collection_detail_controller = collection_detail_controller

    def add_card_detail_controller(self, card_detail_controller):
        self.card_detail_controller = card_detail_controller

    # to switch view just call this functions
    def switch_view_to_main_window(self):
        """ New rendering of main home view, cause need to dynamically override"""

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