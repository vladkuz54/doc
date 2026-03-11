from abc import ABC, abstractmethod

class ICourseRepository(ABC):
    @abstractmethod
    def get_by_id(self, course_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, course):
        pass

    @abstractmethod
    def update(self, course):
        pass

    @abstractmethod
    def delete(self, course_id):
        pass

class IModuleRepository(ABC):
    @abstractmethod
    def get_by_id(self, module_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, module):
        pass

    @abstractmethod
    def update(self, module):
        pass

    @abstractmethod
    def delete(self, module_id):
        pass


class IMaterialRepository(ABC):

    @abstractmethod
    def get_by_id(self, material_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, material):
        pass

    @abstractmethod
    def update(self, material):
        pass

    @abstractmethod
    def delete(self, material_id):
        pass
