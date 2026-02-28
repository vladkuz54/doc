from tqdm import tqdm

from .csv_reader import CSVReader
from .db_models import Course, Module, Material, Video, Text, Test
from .interfaces import IDBRepository
from .__init__ import session

class DBRepository(IDBRepository): 
    def __init__(self, engine, data=None):
        self.engine = engine
        self.data = data or []
    
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
        print("Importing data to database...")
        for row in tqdm(self.data, desc="Processing rows", unit="row"):
            self.course_paste(row)
            self.module_paste(row)
            self.material_paste(row)
            if row["material_type"] == "Video":
                self.video_paste(row)
            if row["material_type"] == "Text":
                self.text_paste(row)
            if row["material_type"] == "Test":
                self.test_paste(row)
        print("Data import completed!")
