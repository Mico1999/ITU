##  main.py file
#   Enter point of the app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

import sys
from PyQt5.QtWidgets import QApplication
from Views.MainWindow import MainWindow
from Database.ConnectDB import CreateConnection
from Models.MainWindowModel import MainWindowModel
from Controllers.MainWindowController import MainWindowController

def main():
    app = QApplication(sys.argv)

    # connect to DB
    if not CreateConnection("StudyDEX.sqlite"):
        sys.exit(1)

    # create model for main view
    main_view_model = MainWindowModel()

    # create main view of app
    main_view = MainWindow(main_view_model)
    main_view.show()

    # create controller for main view
    main_window_controller = MainWindowController(model=main_view_model, view=main_view)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

