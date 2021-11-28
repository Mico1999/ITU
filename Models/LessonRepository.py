from Database.ConnectDB import DbConnection
from Models.DbEntities import Lesson, Card, Collection

class LessonRepository:
    def __init__(self):
        self.connection = DbConnection()
        self.session = self.connection.get_session()

    def insert_lesson(self, lesson):
        try:
            self.get_lesson_by_name(lesson.name)
        except:
            self.session.add(lesson)
            self.session.commit()
            return

        raise Exception('Lesson name already exists!')


    def delete_lesson(self, lesson):
        try:
            self.get_lesson_by_name(lesson.name)
        except:
            raise Exception('Lesson does not exists!')

        self.session.delete(lesson)
        self.session.commit()

    def get_lesson_by_name(self, lesson_name):
        return self.session.query(Lesson).filter(Lesson.name == lesson_name).one()

    def get_all_lessons(self):
        return self.session.query(Lesson).all()



