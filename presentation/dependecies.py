from dal.course_repository import CourseRepository
from dal.module_repository import ModuleRepository
from dal.material_repository import MaterialRepository
from bll.course_service import CourseService
from bll.module_service import ModuleService
from bll.material_service import MaterialService


def get_course_service():
    repo = CourseRepository()
    return CourseService(repo)


def get_module_service():
    repo = ModuleRepository()
    return ModuleService(repo)

def get_material_service():
    repo = MaterialRepository()
    return MaterialService(repo)
