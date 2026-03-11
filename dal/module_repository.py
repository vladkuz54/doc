from .__init__ import session
from .db_models import Module
from .interfaces import IModuleRepository

class ModuleRepository(IModuleRepository):

    def get_by_id(self, module_id):
        return session.query(Module).filter_by(id=module_id).first()

    def get_all(self):
        return session.query(Module).all()
    
    def create(self, module):
        session.add(module)
        session.commit()
        session.refresh(module)
        return module
        
    def update(self, module):
        module_to_update = session.merge(module)
        session.commit()
        session.refresh(module_to_update)
        return module_to_update
        

    def delete(self, module_id):
        module = self.get_by_id(module_id)
        if not module:
            return False
        session.delete(module)
        session.commit()
        