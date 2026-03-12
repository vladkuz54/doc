from tqdm import tqdm

from .db_models import Course, Module, Material, Video, Text, Test
from . import session
from .interfaces import IDBRepository


class DBRepository(IDBRepository): 

    def __init__(self, data):
        self.data = data


    def course_paste(self, row): 
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
    
    def video_paste(self, row):
        course = session.query(Course).filter_by(title=row["course_title"]).first()
        if not course:
            return
        module = session.query(Module).filter_by(title=row["module_title"], course_id=course.id).first()
        if not module:
            return
        check = session.query(Video).filter(
            Material.title == row["material_title"],
            Material.module_id == module.id
        ).first()
        if not check:
            video = Video(
                title=row["material_title"],
                type=row["material_type"],
                estimated_time=row["estimated_time"],
                is_mandatory=row["is_mandatory"],
                release_date=row["release_date"],
                module_id=module.id,
                url=row["video_url"],
                is_watched=row["video_is_watched"],
                duration_seconds=row["video_duration_seconds"],
                has_subtitles=row["video_has_subtitles"],
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
        check = session.query(Text).filter(
            Material.title == row["material_title"],
            Material.module_id == module.id
        ).first()
        if not check:
            text = Text(
                title=row["material_title"],
                type=row["material_type"],
                estimated_time=row["estimated_time"],
                is_mandatory=row["is_mandatory"],
                release_date=row["release_date"],
                module_id=module.id,
                body=row["text_body"],
                is_read=row["text_is_read"],
                reading_time_minutes=row["text_reading_time_min"],
                is_downloadable=row["text_is_downloadable"],
                word_count=row["text_word_count"],
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
        check = session.query(Test).filter(
            Material.title == row["material_title"],
            Material.module_id == module.id
        ).first()
        if not check:
            test = Test(
                title=row["material_title"],
                type=row["material_type"],
                estimated_time=row["estimated_time"],
                is_mandatory=row["is_mandatory"],
                release_date=row["release_date"],
                module_id=module.id,
                score=row["test_score"],
                passing_score=row["test_passing_score"],
                is_passed=row["test_is_passed"],
                attempts_limit=row["test_attempts_limit"],
                time_limit=row["test_time_limit"],
            )
            session.add(test)
            session.commit()
         
    def paste_all(self):
        print("Importing data to database...")
        for row in tqdm(self.data, desc="Processing rows", unit="row"):
            self.course_paste(row)
            self.module_paste(row)
            if row["material_type"] == "Video":
                self.video_paste(row)
            if row["material_type"] == "Text":
                self.text_paste(row)
            if row["material_type"] == "Test":
                self.test_paste(row)
        print("Data import completed!")
