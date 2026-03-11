from .__init__ import session
from .db_models import Material

from .interfaces import IMaterialRepository

class MaterialRepository(IMaterialRepository):

    def get_by_id(self, material_id):
        return session.query(Material).filter_by(id=material_id).first()

    def get_all(self):
        return session.query(Material).all()
    
    def create(self, material):
        session.add(material)
        session.commit()
        session.refresh(material)
        return material

    def update(self, material):
        material_to_update = session.merge(material)
        session.commit()
        session.refresh(material_to_update)
        return material_to_update

    def delete(self, material_id):
        material = self.get_by_id(material_id)
        if not material:
            return False
        session.delete(material)
        session.commit()
