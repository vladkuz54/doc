from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from .interfaces import IDBModels

from .__init__ import engine

Base = declarative_base()

class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    difficulty = Column(String(50), nullable=False)
    language = Column(String(50), nullable=False)


class Module(Base):
    __tablename__ = 'module'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    order_index = Column(Integer, nullable=False)
    is_locked = Column(Boolean, nullable=False)
    course_id = Column(Integer, ForeignKey('course.id'), nullable=False)

class Material(Base):
    __tablename__ = 'material'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    estimated_time = Column(Integer, nullable=False)
    is_mandatory = Column(Boolean, nullable=False)
    release_date = Column(Date, nullable=False)
    module_id = Column(Integer, ForeignKey('module.id'), nullable=False)


class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key=True)
    url = Column(String(255), nullable=False)
    is_watched = Column(Boolean, nullable=False)
    duration_seconds = Column(Integer, nullable=False)
    has_subtitles = Column(Boolean, nullable=False)
    material_id = Column(Integer, ForeignKey('material.id'), nullable=False)

class Text(Base):
    __tablename__ = 'text'

    id = Column(Integer, primary_key=True)
    body = Column(String(255), nullable=False)
    is_read = Column(Boolean, nullable=False)
    reading_time_minutes = Column(Integer, nullable=False)
    is_downloadable = Column(Boolean, nullable=False)
    word_count = Column(Integer, nullable=False)
    material_id = Column(Integer, ForeignKey('material.id'), nullable=False)

class Test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, nullable=False)
    passing_score = Column(Integer, nullable=False)
    is_passed = Column(Boolean, nullable=False)
    attempts_limit = Column(Integer, nullable=False)
    time_limit = Column(Integer, nullable=False)
    material_id = Column(Integer, ForeignKey('material.id'), nullable=False)


class DBModels(IDBModels):
    def __init__(self, engine):
        self.engine = engine

    def create_tables(self):
        Base.metadata.create_all(self.engine)
