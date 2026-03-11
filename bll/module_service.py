from dal.interfaces import IModuleRepository
from dal.db_models import Module
from .interfaces import IModuleService

_MODULE_FIELDS = {'title', 'order_index', 'is_locked', 'course_id'}


class ModuleService(IModuleService):
    def __init__(self, repository: IModuleRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, module_id: int):
        return self.repository.get_by_id(module_id)

    def create(self, data: dict):
        module = Module(
            title=data['title'],
            order_index=data['order_index'],
            is_locked=data['is_locked'],
            course_id=data['course_id'],
        )
        return self.repository.create(module)

    def update(self, module_id: int, data: dict):
        module = self.repository.get_by_id(module_id)
        if not module:
            return None
        for field, value in data.items():
            if field in _MODULE_FIELDS:
                setattr(module, field, value)
        return self.repository.update(module)

    def delete(self, module_id: int):
        return self.repository.delete(module_id)
