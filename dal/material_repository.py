from __init__ import session
from db_models import Material

from interfaces import IMaterialRepository

class MaterialRepository(IMaterialRepository):

    def get_material_by_id(self, material_id):
        return session.query(Material).filter_by(id=material_id).first()

    def get_all_materials(self):
        return session.query(Material).all()
    
    def add_material(self, material):
        session.add(material)
        session.commit()
        session.refresh(material)
        return material

    def update_material(self, material):
        material_to_update = session.merge(material)
        session.commit()
        session.refresh(material_to_update)
        return material_to_update

    def delete_material(self, material_id):
        material = self.get_material_by_id(material_id)
        if not material:
            return False
        session.delete(material)
        session.commit()


if __name__ == "__main__":
    repository = MaterialRepository()

    test_to_update = repository.get_material_by_id(12)

    test_to_update.title = "Updated Material eewsd"
    test_to_update.score = 67
    test_to_update.estimated_time = 100

    repository.update_material(test_to_update)
    
