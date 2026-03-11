from dal.interfaces import IMaterialRepository
from dal.db_models import Material, Video, Text, Test
from .interfaces import IMaterialService

_BASE_FIELDS = {'title', 'type', 'estimated_time', 'is_mandatory', 'release_date', 'module_id'}

_TYPE_FIELDS: dict[str, set] = {
    'Video': {'url', 'is_watched', 'duration_seconds', 'has_subtitles'},
    'Text':  {'body', 'is_read', 'reading_time_minutes', 'is_downloadable', 'word_count'},
    'Test':  {'score', 'passing_score', 'is_passed', 'attempts_limit', 'time_limit'},
}

_TYPE_MODEL: dict[str, type] = {
    'Video': Video,
    'Text': Text,
    'Test': Test,
}


class MaterialService(IMaterialService):
    def __init__(self, repository: IMaterialRepository) -> None:
        self.repository = repository

    def get_all(self) -> list:
        return self.repository.get_all()

    def get_by_id(self, material_id: int):
        return self.repository.get_by_id(material_id)

    def create(self, data: dict):
        material_type: str = data['type']
        model_class = _TYPE_MODEL.get(material_type)
        if model_class is None:
            raise ValueError(f"Unknown material type: {material_type!r}")

        allowed_fields = _BASE_FIELDS | _TYPE_FIELDS[material_type]
        kwargs = {k: v for k, v in data.items() if k in allowed_fields}
        material = model_class(**kwargs)
        return self.repository.create(material)

    def update(self, material_id: int, data: dict):
        material = self.repository.get_by_id(material_id)
        if not material:
            return None

        material_type: str = material.type
        allowed_fields = _BASE_FIELDS | _TYPE_FIELDS.get(material_type, set())
        for field, value in data.items():
            if field in allowed_fields:
                setattr(material, field, value)
        return self.repository.update(material)

    def delete(self, material_id: int) -> bool:
        return self.repository.delete(material_id)
