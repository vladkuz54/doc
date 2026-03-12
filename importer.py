import os

from generator.csv_generator import CSVGenerator
from dal.csv_reader import CSVReader
from bll.db_service import DBService

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "courses.csv")

if __name__ == "__main__":

    generator = CSVGenerator(filename=CSV_PATH, num_rows=1000)
    generator.generate_csv()

    reader = CSVReader(CSV_PATH)
    data = reader.read_csv()

    db_service = DBService(data)
    db_service.create_tables()

    db_service.paste_all()