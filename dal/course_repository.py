from __init__ import session
from db_models import Course

from interfaces import ICourseRepository

class CourseRepository(ICourseRepository):

    def get_course_by_id(self, course_id):
        return session.query(Course).filter_by(id=course_id).first()

    def get_all_courses(self):
        return session.query(Course).all()
    
    def add_course(self, course):
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

    def update_course(self, course):
        course_to_update = session.merge(course)
        session.commit()
        session.refresh(course_to_update)
        return course_to_update

    def delete_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if not course:
            return False
        session.delete(course)
        session.commit()


if __name__ == "__main__":
    repository = CourseRepository()

    # delete
    repository.delete_course(1)    