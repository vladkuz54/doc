from abc import ABC, abstractmethod

class ICourseRepository(ABC):
    @abstractmethod
    def get_course_by_id(self, course_id):
        pass

    @abstractmethod
    def get_all_courses(self):
        pass

    @abstractmethod
    def add_course(self, course):
        pass

    @abstractmethod
    def update_course(self, course):
        pass

    @abstractmethod
    def delete_course(self, course_id):
        pass

class IModuleRepository(ABC):
    @abstractmethod
    def get_module_by_id(self, module_id):
        pass

    @abstractmethod
    def get_all_modules(self):
        pass

    @abstractmethod
    def add_module(self, module):
        pass

    @abstractmethod
    def update_module(self, module):
        pass

    @abstractmethod
    def delete_module(self, module_id):
        pass


class IMaterialRepository(ABC):

    @abstractmethod
    def get_material_by_id(self, material_id):
        pass

    @abstractmethod
    def get_all_materials(self):
        pass

    @abstractmethod
    def add_material(self, material):
        pass

    @abstractmethod
    def update_material(self, material):
        pass

    @abstractmethod
    def delete_material(self, material_id):
        pass
