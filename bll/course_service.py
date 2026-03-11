import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'dal'))

from dal.interfaces import ICourseRepository
from dal.db_models import Course
from .interfaces import ICourseService

_COURSE_FIELDS = {'title', 'description', 'difficulty', 'language'}


class CourseService(ICourseService):
    def __init__(self, repository: ICourseRepository) -> None:
        self.repository = repository

    def get_all(self) -> list:
        return self.repository.get_all()

    def get_by_id(self, course_id: int):
        return self.repository.get_by_id(course_id)

    def create(self, data: dict):
        course = Course(
            title=data['title'],
            description=data['description'],
            difficulty=data['difficulty'],
            language=data['language'],
        )
        return self.repository.create(course)

    def update(self, course_id: int, data: dict):
        course = self.repository.get_by_id(course_id)
        if not course:
            return None
        for field, value in data.items():
            if field in _COURSE_FIELDS:
                setattr(course, field, value)
        return self.repository.update(course)

    def delete(self, course_id: int) -> bool:
        return self.repository.delete(course_id)
