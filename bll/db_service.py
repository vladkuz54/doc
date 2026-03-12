from dal.db_models import DBModels
from dal.db_repository import DBRepository
from bll.interfaces import IDBService


class DBService(IDBService):
    def __init__(self, data):
        self.db_models = DBModels()
        self.db_repository = DBRepository(data)

    def create_tables(self):
        self.db_models.create_tables()

    def paste_all(self):
        self.db_repository.paste_all()
