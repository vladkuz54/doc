from dal.interfaces import ICSVReader, IDBModels, IDBRepository


class CourseService:
    def __init__(self, csv_reader: ICSVReader, db_models: IDBModels, db_repository: IDBRepository):
        self.csv_reader = csv_reader
        self.db_models = db_models
        self.db_repository = db_repository
        
    def create_tables(self):
        self.db_models.create_tables()

    def import_data(self):
        data = self.csv_reader.read_csv()
        self.db_repository.data = data
        self.db_repository.paste_all()
