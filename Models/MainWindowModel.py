##  Models/MainWindowModel.py module
#   Implements the model for the main view of app
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class MainWindowModel:

    def __init__(self):
        self.model = QSqlTableModel()
        self.model.setTable("Lesson")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()
        headers = ("id", "name", "study_field")
        for idx, header in enumerate(headers):      # set headers for QTableview
            self.model.setHeaderData(idx, Qt.Horizontal, header)

    def Add_Lesson(self, data):
        """Add a lesson to the database."""
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column_index, field in enumerate(data):
            self.model.setData(self.model.index(rows, column_index + 1), field)
        self.model.submitAll()  # store changes to DB
        self.model.select()     # reloads data from DB to model

    def Delete_Lesson(self, row):
        """Remove a lesson from the database."""
        self.model.removeRow(row)
        self.model.submitAll()  # store changes to DB
        self.model.select()     # reloads data from DB to model

    def Clear_Lessons(self):
        """Remove all lessons from the database."""
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()  # store changes to DB
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()     # reloads data from DB to model
