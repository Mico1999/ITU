##  main.py file
#   Enter point of the app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

import sys
from PyQt5.QtWidgets import QApplication
from Controllers.MainWindowController import MainWindowController
from Views.MainWindow import MainWindow


def main():

    app = QApplication(sys.argv)

    # create main view of app
    main_view = MainWindow()

    # create controller for main view
    main_window_controller = MainWindowController(view=main_view)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
