from dal.interfaces import ICSVReader, IDBModels, IDBRepository


class CourseService:
    def __init__(self, csv_reader: ICSVReader, db_models: IDBModels, db_repository: IDBRepository):
        self.csv_reader = csv_reader
        self.db_models = db_models
        self.db_repository = db_repository
        
    def setup_database(self):
        self.db_models.create_tables()

    def import_data(self):
        self.db_repository.paste_all()

if __name__ == "__main__":
    
    service = CourseService(ICSVReader, IDBModels, IDBRepository)
    service.setup_database()
    service.import_data()
