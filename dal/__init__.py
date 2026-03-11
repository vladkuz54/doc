from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = "courses.sqlite"
DATABASE_URL = f"sqlite:///{os.path.abspath(DB_NAME)}"

engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()


engine = create_engine(DATABASE_URL, echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()   