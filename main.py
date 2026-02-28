# main.py
from dal.csv_reader import CSVReader  # Реалізація ICsvRepository
from dal.db_repository import DBRepository # Реалізація ICourseRepository
from dal import engine
from bll.course_service import CourseService

if __name__ == "__main__":
    # 1. Ініціалізація DAL компонентів
    # DAL відповідає за технічні деталі (файл, БД)
    csv_dal = CSVReader("data/courses.csv")
    db_dal = DBRepository(engine, )

    # 2. Впровадження залежностей (Dependency Injection)
    # CourseService всередині має тип-хінти на ІНТЕРФЕЙСИ (ABC), а не на ці класи
    service = CourseService(csv_dal, db_dal)

    # 3. Запуск логіки через BLL
    # BLL керує порядком: спочатку setup, потім import
    service.setup_database() # Викликає DAL для створення таблиць
    service.import_data()    # Викликає DAL для зчитування, потім для збереження