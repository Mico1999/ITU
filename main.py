##  main.py file
#   Enter point of the app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

import sys
from PyQt5.QtWidgets import QApplication
from Controllers.MainWindowController import MainWindowController


def main():

    app = QApplication(sys.argv)


    # create controller for main view, view is rendered in controller
    main_window_controller = MainWindowController()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
