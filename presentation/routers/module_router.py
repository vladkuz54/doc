from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from bll.module_service import ModuleService
from dal.course_repository import CourseRepository
from ..dependecies import get_module_service
from ..schemas import ModuleSchema

router = APIRouter(prefix="/module")
templates = Jinja2Templates(directory="presentation/templates")


@router.get("/")
def list_modules(request: Request, service: ModuleService = Depends(get_module_service)):
    modules = service.get_all()
    return templates.TemplateResponse("module/module_list.html", {"request": request, "modules": modules})


@router.get("/add")
def add_module_form(request: Request):
    courses = CourseRepository().get_all()
    return templates.TemplateResponse("module/module_form.html", {
        "request": request,
        "action_title": "Add module",
        "action_url": "/module/add",
        "module": None,
        "courses": courses,
    })


@router.post("/add")
def add_module(
    title: str = Form(...),
    order_index: int = Form(...),
    is_locked: bool = Form(False),
    course_id: int = Form(...),
    service: ModuleService = Depends(get_module_service),
):
    data = ModuleSchema(title=title, order_index=order_index, is_locked=is_locked, course_id=course_id)
    service.create(data.model_dump())
    return RedirectResponse(url="/module", status_code=303)


@router.get("/edit/{module_id}")
def edit_module_form(module_id: int, request: Request, service: ModuleService = Depends(get_module_service)):
    module = service.get_by_id(module_id)
    courses = CourseRepository().get_all()
    return templates.TemplateResponse("module/module_form.html", {
        "request": request,
        "action_title": "Edit module",
        "action_url": f"/module/edit/{module_id}",
        "module": module,
        "courses": courses,
    })


@router.post("/edit/{module_id}")
def edit_module(
    module_id: int,
    title: str = Form(...),
    order_index: int = Form(...),
    is_locked: bool = Form(False),
    course_id: int = Form(...),
    service: ModuleService = Depends(get_module_service),
):
    data = ModuleSchema(title=title, order_index=order_index, is_locked=is_locked, course_id=course_id)
    service.update(module_id, data.model_dump())
    return RedirectResponse(url="/module", status_code=303)


@router.post("/delete/{module_id}")
def delete_module(module_id: int, service: ModuleService = Depends(get_module_service)):
    service.delete(module_id)
    return RedirectResponse(url="/module", status_code=303)
