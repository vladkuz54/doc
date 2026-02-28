from .db_models import Course, Module, Material, Video, Text, Test
from .interfaces import IDBRepository

from .__init__ import engine, session

class DBRepository(IDBRepository):
    def __init__(self, engine, data):
        self.engine = engine
        self.data = data
    
    def course_paste(self, row):
        for key, value in row.items():   
            check = session.query(Course).filter_by(title=row["course_title"]).first()
            if not check:
                course = Course(
                    title=row["course_title"],
                    description=row["course_description"],
                    difficulty=row["course_difficulty"],
                    language=row["course_language"]
                )
                session.add(course)
                session.commit()
    
    def module_paste(self, row):
        course = session.query(Course).filter_by(title=row["course_title"]).first()
        if course:
            check = session.query(Module).filter_by(title=row["module_title"], course_id=course.id).first()
            if not check:
                module = Module(
                    title=row["module_title"],
                    order_index=row["module_order_index"],
                    is_locked=row["module_is_locked"],
                    course_id=course.id
                )
                session.add(module)
                session.commit()
    
    def material_paste(self, row):
        course = session.query(Course).filter_by(title=row["course_title"]).first()
        if not course:
            return
        module = session.query(Module).filter_by(title=row["module_title"], course_id=course.id).first()
        if module:
            check = session.query(Material).filter_by(title=row["material_title"], module_id=module.id).first()
            if not check:
                material = Material(
                    title=row["material_title"],
                    type=row["material_type"],
                    estimated_time=row["estimated_time"],
                    is_mandatory=row["is_mandatory"],
                    release_date=row["release_date"],
                    module_id=module.id
                )
                session.add(material)
                session.commit()
    
    def video_paste(self, row):
        course = session.query(Course).filter_by(title=row["course_title"]).first()
        if not course:
            return
        module = session.query(Module).filter_by(title=row["module_title"], course_id=course.id).first()
        if not module:
            return
        material = session.query(Material).filter_by(title=row["material_title"], module_id=module.id).first()
        if material:
            check = session.query(Video).filter_by(url=row["video_url"], material_id=material.id).first()
            if not check:
                video = Video(
                    url=row["video_url"],
                    is_watched=row["video_is_watched"],
                    duration_seconds=row["video_duration_seconds"],
                    has_subtitles=row["video_has_subtitles"],
                    material_id=material.id
                )
                session.add(video)
                session.commit()
    
    def text_paste(self, row):
        course = session.query(Course).filter_by(title=row["course_title"]).first()
        if not course:
            return
        module = session.query(Module).filter_by(title=row["module_title"], course_id=course.id).first()
        if not module:
            return
        material = session.query(Material).filter_by(title=row["material_title"], module_id=module.id).first()
        if material:
            check = session.query(Text).filter_by(body=row["text_body"], material_id=material.id).first()
            if not check:
                text = Text(
                    body=row["text_body"],
                    is_read=row["text_is_read"],
                    reading_time_minutes=row["text_reading_time_min"],
                    is_downloadable=row["text_is_downloadable"],
                    word_count=row["text_word_count"],
                    material_id=material.id
                )
                session.add(text)
                session.commit()

    def test_paste(self, row):
        course = session.query(Course).filter_by(title=row["course_title"]).first()
        if not course:
            return
        module = session.query(Module).filter_by(title=row["module_title"], course_id=course.id).first()
        if not module:
            return
        material = session.query(Material).filter_by(title=row["material_title"], module_id=module.id).first()
        if material:
            check = session.query(Test).filter_by(score=row["test_score"], material_id=material.id).first()
            if not check:
                test = Test(
                    score=row["test_score"],
                    passing_score=row["test_passing_score"],
                    is_passed=row["test_is_passed"],
                    attempts_limit=row["test_attempts_limit"],
                    time_limit=row["test_time_limit"],
                    material_id=material.id
                )
                session.add(test)
                session.commit()
        
    def paste_all(self):
        for row in self.data:
            self.course_paste(row)
            self.module_paste(row)
            self.material_paste(row)
            if row["video_url"]:
                self.video_paste(row)
            if row["text_body"]:
                self.text_paste(row)
            if row["test_score"]:
                self.test_paste(row)


if __name__ == "__main__":
    # Example usage
    data = [
        {
            "course_title": "Python Programming",
            "course_description": "Learn Python from scratch",
            "course_difficulty": "Beginner",
            "course_language": "English",
            "module_title": "Introduction to Python",
            "module_order_index": 1,
            "module_is_locked": False,
            "material_title": "Python Basics",
            "material_type": "Video",
            "estimated_time": 60,
            "is_mandatory": True,
            "release_date": "2024-01-01",
            "video_url": "https://example.com/python_basics.mp4",
            "video_is_watched": False,
            "video_duration_seconds": 3600,
            "video_has_subtitles": True,
            "text_body": "",
            "text_is_read": False,
            "text_reading_time_min": 0,
            "text_is_downloadable": False,
            "text_word_count": 0,
            "test_score": None,
            "test_passing_score": None,
            "test_is_passed": None,
            "test_attempts_limit": None,
            "test_time_limit": None
        }
    ]

    repository = DBRepository(engine, data)
    repository.paste_all()