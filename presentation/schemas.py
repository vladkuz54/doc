from datetime import date
from pydantic import BaseModel


class CourseSchema(BaseModel):
    title: str
    description: str
    difficulty: str
    language: str


class ModuleSchema(BaseModel):
    title: str
    order_index: int
    is_locked: bool
    course_id: int


class BaseMaterialSchema(BaseModel):
    title: str
    estimated_time: int
    is_mandatory: bool
    release_date: date
    module_id: int


class VideoSchema(BaseMaterialSchema):
    url: str
    is_watched: bool
    duration_seconds: int
    has_subtitles: bool


class TextSchema(BaseMaterialSchema):
    body: str
    is_read: bool
    reading_time_minutes: int
    is_downloadable: bool
    word_count: int


class TestSchema(BaseMaterialSchema):
    score: int
    passing_score: int
    is_passed: bool
    attempts_limit: int
    time_limit: int
