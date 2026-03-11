from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# DB_NAME = "courses.sqlite"
# DATABASE_URL = f"sqlite:///{os.path.abspath(DB_NAME)}"

# engine = create_engine(DATABASE_URL, echo=False)

# Session = sessionmaker(bind=engine)
# session = Session()


DB_USER = "root"
DB_PASSWORD = "2077vkuz"
DB_HOST = "localhost"
DB_PORT = 3306 
DB_NAME = "courses_db"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()   