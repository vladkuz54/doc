from dal.csv_reader import CSVReader
from dal.db_repository import DBRepository
from dal.db_models import DBModels
from dal import engine
from bll.course_service import CourseService
from generator.csv_generator import CSVGenerator

def main():
    print("Available commands:")
    print("1. generate csv - Generate a new CSV file with random data.")
    print("2. create database - Create tables and import data from the CSV file.")
    print("3. exit - Exit the program.")

    while True:
        command = input("\nEnter a command: ").strip().lower()

        if command == "generate csv":
            num_rows = input("Enter the number of rows to generate (default 1000): ").strip()
            if not num_rows.isdigit():
                num_rows = 1000
            else:                
                if int(num_rows) < 1000:
                    print("Minimum number of rows is 1000. Setting to 1000.")
                    num_rows = 1000
            generator = CSVGenerator(filename="courses.csv", num_rows=int(num_rows))
            generator.generate_csv()
            print(f"CSV file generated with {num_rows} rows.")

        elif command == "create database":
            filiname = input("Enter the CSV filename to import (default 'data/courses.csv'): ").strip()
            if not filiname:
                filiname = "data/courses.csv"
            filiname = filiname.strip('"\'')
            csv_reader = CSVReader(filiname)
            data = csv_reader.read_csv()
            db_repository = DBRepository(engine, data)
            db_models = DBModels(engine)

            service = CourseService(csv_reader, db_models, db_repository)
            service.create_tables()
            service.import_data()

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()