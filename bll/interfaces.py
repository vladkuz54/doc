from abc import ABC, abstractmethod
from typing import Optional


class ICourseService(ABC):
    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def get_by_id(self, course_id: int):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, course_id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, course_id: int) -> bool:
        pass


class IModuleService(ABC):
    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def get_by_id(self, module_id: int):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, module_id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, module_id: int) -> bool:
        pass


class IMaterialService(ABC):
    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def get_by_id(self, material_id: int):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, material_id: int, data: dict):
        pass

    @abstractmethod
    def delete(self, material_id: int) -> bool:
        pass
