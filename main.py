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

    # create main view of app
    main_view = MainWindow()
    main_view.show()

    # create model for main view and set it's controller
    main_window_model = MainWindowModel()
    MainWindowController(model=main_window_model, view=main_view)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

