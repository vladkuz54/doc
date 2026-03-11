from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from bll.course_service import CourseService
from ..dependecies import get_course_service
from ..schemas import CourseSchema
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/courses")
templates = Jinja2Templates(directory="presentation/templates")

@router.get("/")
def list_courses(request: Request, service: CourseService = Depends(get_course_service)):
    courses = service.get_all()
    return templates.TemplateResponse("course/courses_list.html", {"request": request, "courses": courses})

@router.get("/add")
def add_course_form(request: Request):
    return templates.TemplateResponse("course/course_form.html", {
        "request": request,
        "action_title": "Add course",
        "action_url": "/courses/add",
        "course": None,
    })

@router.post("/add")
def add_course(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    difficulty: str = Form(...),
    language: str = Form(...),
    service: CourseService = Depends(get_course_service),
):
    data = CourseSchema(title=title, description=description, difficulty=difficulty, language=language)
    service.create(data.model_dump())
    return RedirectResponse(url="/courses", status_code=303)

@router.get("/edit/{course_id}")
def edit_course_form(course_id: int, request: Request, service: CourseService = Depends(get_course_service)):
    course = service.get_by_id(course_id)
    return templates.TemplateResponse("course/course_form.html", {
        "request": request,
        "action_title": "Edit course",
        "action_url": f"/courses/edit/{course_id}",
        "course": course,
    })

@router.post("/edit/{course_id}")
def edit_course(
    course_id: int,
    title: str = Form(...),
    description: str = Form(...),
    difficulty: str = Form(...),
    language: str = Form(...),
    service: CourseService = Depends(get_course_service),
):
    data = CourseSchema(title=title, description=description, difficulty=difficulty, language=language)
    service.update(course_id, data.model_dump())
    return RedirectResponse(url="/courses", status_code=303)

@router.post("/delete/{course_id}")
def delete_course(course_id: int, service: CourseService = Depends(get_course_service)):
    service.delete(course_id)
    return RedirectResponse(url="/courses", status_code=303)
