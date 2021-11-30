

class ModeratorController:
    """ Calls functions of view controllers to dynamically change views on the basis of triggered actions"""
    def __init__(self):
        pass

    def switch_view_to_home(self, main_window_controller):
        """ New rendering of main home view, cause need to dynamically override"""

        # setup home view once again to see changes
        main_window_controller.setup_UI()
