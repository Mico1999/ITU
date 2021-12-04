#   main.py module
#   Starting point of the program
#   @Authors Marek Miček (xmicek08), Matej Jurík (xjurik12), Peter Rúček (xrucek00)
#   @date 4.12.2021

import sys
from PyQt5.QtWidgets import QApplication
from Controllers.MainWindowController import MainWindowController
from Database.Seed import seed


def main():

    app = QApplication(sys.argv)

    # Seed initial data, if called once, should be commented, because throws exception
    seed()

    # create controller for main view, view is rendered in controller
    MainWindowController()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
