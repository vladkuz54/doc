from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

DB_NAME = "courses.sqlite"
DATABASE_URL = f"sqlite:///{os.path.abspath(DB_NAME)}"

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

print(f"Using SQLite database at '{DB_NAME}'.")
