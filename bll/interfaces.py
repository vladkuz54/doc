from abc import ABC, abstractmethod

class ICourseService(ABC):
    @abstractmethod
    def create_tables(self):
        pass

    @abstractmethod
    def import_data(self):
        pass