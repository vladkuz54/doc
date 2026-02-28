from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

DB_USER = "root"
DB_PASSWORD = "2077vkuz"
DB_HOST = "localhost"
DB_PORT = 3306 
DB_NAME = "courses_db"

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)

if not database_exists(DATABASE_URL):
    print(f"Database '{DB_NAME}' does not exist. Creating it now...")
    create_database(DATABASE_URL)
else:
    print(f"Database '{DB_NAME}' already exists.")

Session = sessionmaker(bind=engine)
session = Session()