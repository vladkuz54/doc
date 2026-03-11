from __init__ import session
from db_models import Module
from interfaces import IModuleRepository

class ModuleRepository(IModuleRepository):

    def get_module_by_id(self, module_id):
        return session.query(Module).filter_by(id=module_id).first()

    def get_all_modules(self):
        return session.query(Module).all()
    
    def add_module(self, module):
        session.add(module)
        session.commit()
        session.refresh(module)
        return module
        
    def update_module(self, module):
        module_to_update = session.merge(module)
        session.commit()
        session.refresh(module_to_update)
        return module_to_update
        

    def delete_module(self, module_id):
        module = self.get_module_by_id(module_id)
        if not module:
            return False
        session.delete(module)
        session.commit()
        

if __name__ == "__main__":
    repository = ModuleRepository()

    module_to_update = repository.get_module_by_id(4)

    module_to_update.title = "Updated Module Title"
    module_to_update.order_index = 2

    repository.update_module(module_to_update)