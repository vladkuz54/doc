from abc import ABC, abstractmethod

class ICSVReader(ABC):
    @abstractmethod
    def read_csv(self):
        pass 

class IDBModels(ABC):
    @abstractmethod
    def create_tables(self):
        pass

class IDBRepository(ABC):
    @abstractmethod
    def paste_all(self):
        pass
