##  Database/ConnectDB.py module
#   Implements connection to DB and creates tables
#   @Authors Marek Miček (xmicek08), ....
#   @date 5.11.2021

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def CreateConnection(dbName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(dbName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "StudyDex",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    CreateLessonTable()
    return True


def CreateLessonTable():
    """Create the contacts table in the database."""
    table_Query = QSqlQuery()
    return table_Query.exec(
        """
        CREATE TABLE IF NOT EXISTS Lesson (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(80) NOT NULL,
            study_field VARCHAR(80) NOT NULL
        }
        """
    )
