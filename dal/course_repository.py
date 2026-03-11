from .__init__ import session
from .db_models import Course
from .interfaces import ICourseRepository


class CourseRepository(ICourseRepository):

    def get_by_id(self, course_id):
        return session.query(Course).filter_by(id=course_id).first()

    def get_all(self):
        return session.query(Course).all()
    
    def create(self, course):
        session.add(course)
        session.commit()
        session.refresh(course)
        return course

    def update(self, course):
        course_to_update = session.merge(course)
        session.commit()
        session.refresh(course_to_update)
        return course_to_update

    def delete(self, course_id):
        course = self.get_by_id(course_id)
        if not course:
            return False
        session.delete(course)
        session.commit()
        