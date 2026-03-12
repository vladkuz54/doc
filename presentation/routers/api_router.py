from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from bll.course_service import CourseService
from bll.module_service import ModuleService
from bll.material_service import MaterialService
from ..dependecies import get_course_service, get_module_service, get_material_service
from ..schemas import CourseSchema, ModuleSchema, VideoSchema, TextSchema, TestSchema

router = APIRouter(prefix="/api", tags=["API"])


# ── Courses ──────────────────────────────────────────────────────

@router.get("/courses", summary="Get all courses")
def api_list_courses(service: CourseService = Depends(get_course_service)):
    courses = service.get_all()
    return [{"id": c.id, "title": c.title, "description": c.description, "difficulty": c.difficulty, "language": c.language} for c in courses]

@router.get("/courses/{course_id}", summary="Get course by ID")
def api_get_course(course_id: int, service: CourseService = Depends(get_course_service)):
    course = service.get_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"id": course.id, "title": course.title, "description": course.description, "difficulty": course.difficulty, "language": course.language}

@router.post("/courses", summary="Create course", status_code=201)
def api_create_course(data: CourseSchema, service: CourseService = Depends(get_course_service)):
    service.create(data.model_dump())
    return JSONResponse(status_code=201, content={"detail": "Course created"})

@router.put("/courses/{course_id}", summary="Update course")
def api_update_course(course_id: int, data: CourseSchema, service: CourseService = Depends(get_course_service)):
    course = service.get_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    service.update(course_id, data.model_dump())
    return {"detail": "Course updated"}

@router.delete("/courses/{course_id}", summary="Delete course")
def api_delete_course(course_id: int, service: CourseService = Depends(get_course_service)):
    course = service.get_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    service.delete(course_id)
    return {"detail": "Course deleted"}


# ── Modules ──────────────────────────────────────────────────────

@router.get("/modules", summary="Get all modules")
def api_list_modules(service: ModuleService = Depends(get_module_service)):
    modules = service.get_all()
    return [{"id": m.id, "title": m.title, "order_index": m.order_index, "is_locked": m.is_locked, "course_id": m.course_id} for m in modules]

@router.get("/modules/{module_id}", summary="Get module by ID")
def api_get_module(module_id: int, service: ModuleService = Depends(get_module_service)):
    module = service.get_by_id(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    return {"id": module.id, "title": module.title, "order_index": module.order_index, "is_locked": module.is_locked, "course_id": module.course_id}

@router.post("/modules", summary="Create module", status_code=201)
def api_create_module(data: ModuleSchema, service: ModuleService = Depends(get_module_service)):
    service.create(data.model_dump())
    return JSONResponse(status_code=201, content={"detail": "Module created"})

@router.put("/modules/{module_id}", summary="Update module")
def api_update_module(module_id: int, data: ModuleSchema, service: ModuleService = Depends(get_module_service)):
    module = service.get_by_id(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    service.update(module_id, data.model_dump())
    return {"detail": "Module updated"}

@router.delete("/modules/{module_id}", summary="Delete module")
def api_delete_module(module_id: int, service: ModuleService = Depends(get_module_service)):
    module = service.get_by_id(module_id)
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    service.delete(module_id)
    return {"detail": "Module deleted"}


# ── Materials ────────────────────────────────────────────────────

@router.get("/materials", summary="Get all materials")
def api_list_materials(service: MaterialService = Depends(get_material_service)):
    result = []
    for m in service.get_all():
        result.append({"id": m.id, "title": m.title, "type": m.type, "estimated_time": m.estimated_time,
                        "is_mandatory": m.is_mandatory, "release_date": str(m.release_date), "module_id": m.module_id})
    return result

@router.get("/materials/{material_id}", summary="Get material by ID")
def api_get_material(material_id: int, service: MaterialService = Depends(get_material_service)):
    m = service.get_by_id(material_id)
    if not m:
        raise HTTPException(status_code=404, detail="Material not found")
    return {"id": m.id, "title": m.title, "type": m.type, "estimated_time": m.estimated_time,
            "is_mandatory": m.is_mandatory, "release_date": str(m.release_date), "module_id": m.module_id}

@router.post("/materials/video", summary="Create video material", status_code=201)
def api_create_video(data: VideoSchema, service: MaterialService = Depends(get_material_service)):
    service.create({"type": "Video", **data.model_dump()})
    return JSONResponse(status_code=201, content={"detail": "Video created"})

@router.post("/materials/text", summary="Create text material", status_code=201)
def api_create_text(data: TextSchema, service: MaterialService = Depends(get_material_service)):
    service.create({"type": "Text", **data.model_dump()})
    return JSONResponse(status_code=201, content={"detail": "Text created"})

@router.post("/materials/test", summary="Create test material", status_code=201)
def api_create_test(data: TestSchema, service: MaterialService = Depends(get_material_service)):
    service.create({"type": "Test", **data.model_dump()})
    return JSONResponse(status_code=201, content={"detail": "Test created"})

@router.delete("/materials/{material_id}", summary="Delete material")
def api_delete_material(material_id: int, service: MaterialService = Depends(get_material_service)):
    m = service.get_by_id(material_id)
    if not m:
        raise HTTPException(status_code=404, detail="Material not found")
    service.delete(material_id)
    return {"detail": "Material deleted"}
