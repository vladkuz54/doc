from fastapi import APIRouter, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from bll.material_service import MaterialService
from dal.module_repository import ModuleRepository
from ..dependecies import get_material_service
from datetime import date

router = APIRouter(prefix="/material")
templates = Jinja2Templates(directory="presentation/templates")


def _modules():
    return ModuleRepository().get_all()


# ── All materials ────────────────────────────────────────────────
@router.get("/")
def list_materials(request: Request, service: MaterialService = Depends(get_material_service)):
    materials = service.get_all()
    return templates.TemplateResponse("material/material_list.html", {"request": request, "materials": materials})


# ── Video ────────────────────────────────────────────────────────
@router.get("/video")
def list_videos(request: Request, service: MaterialService = Depends(get_material_service)):
    videos = [m for m in service.get_all() if m.type == "Video"]
    return templates.TemplateResponse("material/video_list.html", {"request": request, "materials": videos})

@router.get("/video/add")
def add_video_form(request: Request):
    return templates.TemplateResponse("material/video_form.html", {
        "request": request, "action_title": "Додати відео",
        "action_url": "/material/video/add", "material": None, "modules": _modules(),
    })

@router.post("/video/add")
def add_video(
    title: str = Form(...), estimated_time: int = Form(...),
    is_mandatory: bool = Form(False), release_date: date = Form(...),
    module_id: int = Form(...), url: str = Form(...),
    is_watched: bool = Form(False), duration_seconds: int = Form(...),
    has_subtitles: bool = Form(False),
    service: MaterialService = Depends(get_material_service),
):
    service.create({"type": "Video", "title": title, "estimated_time": estimated_time,
                    "is_mandatory": is_mandatory, "release_date": release_date, "module_id": module_id,
                    "url": url, "is_watched": is_watched, "duration_seconds": duration_seconds,
                    "has_subtitles": has_subtitles})
    return RedirectResponse(url="/material/video", status_code=303)

@router.get("/video/edit/{material_id}")
def edit_video_form(material_id: int, request: Request, service: MaterialService = Depends(get_material_service)):
    material = service.get_by_id(material_id)
    return templates.TemplateResponse("material/video_form.html", {
        "request": request, "action_title": "Редагувати відео",
        "action_url": f"/material/video/edit/{material_id}",
        "material": material, "modules": _modules(),
    })

@router.post("/video/edit/{material_id}")
def edit_video(
    material_id: int,
    title: str = Form(...), estimated_time: int = Form(...),
    is_mandatory: bool = Form(False), release_date: date = Form(...),
    module_id: int = Form(...), url: str = Form(...),
    is_watched: bool = Form(False), duration_seconds: int = Form(...),
    has_subtitles: bool = Form(False),
    service: MaterialService = Depends(get_material_service),
):
    service.update(material_id, {"title": title, "estimated_time": estimated_time,
                                  "is_mandatory": is_mandatory, "release_date": release_date,
                                  "module_id": module_id, "url": url, "is_watched": is_watched,
                                  "duration_seconds": duration_seconds, "has_subtitles": has_subtitles})
    return RedirectResponse(url="/material/video", status_code=303)


# ── Text ─────────────────────────────────────────────────────────
@router.get("/text")
def list_texts(request: Request, service: MaterialService = Depends(get_material_service)):
    texts = [m for m in service.get_all() if m.type == "Text"]
    return templates.TemplateResponse("material/text_list.html", {"request": request, "materials": texts})

@router.get("/text/add")
def add_text_form(request: Request):
    return templates.TemplateResponse("material/text_form.html", {
        "request": request, "action_title": "Додати текст",
        "action_url": "/material/text/add", "material": None, "modules": _modules(),
    })

@router.post("/text/add")
def add_text(
    title: str = Form(...), estimated_time: int = Form(...),
    is_mandatory: bool = Form(False), release_date: date = Form(...),
    module_id: int = Form(...), body: str = Form(...),
    is_read: bool = Form(False), reading_time_minutes: int = Form(...),
    is_downloadable: bool = Form(False), word_count: int = Form(...),
    service: MaterialService = Depends(get_material_service),
):
    service.create({"type": "Text", "title": title, "estimated_time": estimated_time,
                    "is_mandatory": is_mandatory, "release_date": release_date, "module_id": module_id,
                    "body": body, "is_read": is_read, "reading_time_minutes": reading_time_minutes,
                    "is_downloadable": is_downloadable, "word_count": word_count})
    return RedirectResponse(url="/material/text", status_code=303)

@router.get("/text/edit/{material_id}")
def edit_text_form(material_id: int, request: Request, service: MaterialService = Depends(get_material_service)):
    material = service.get_by_id(material_id)
    return templates.TemplateResponse("material/text_form.html", {
        "request": request, "action_title": "Редагувати текст",
        "action_url": f"/material/text/edit/{material_id}",
        "material": material, "modules": _modules(),
    })

@router.post("/text/edit/{material_id}")
def edit_text(
    material_id: int,
    title: str = Form(...), estimated_time: int = Form(...),
    is_mandatory: bool = Form(False), release_date: date = Form(...),
    module_id: int = Form(...), body: str = Form(...),
    is_read: bool = Form(False), reading_time_minutes: int = Form(...),
    is_downloadable: bool = Form(False), word_count: int = Form(...),
    service: MaterialService = Depends(get_material_service),
):
    service.update(material_id, {"title": title, "estimated_time": estimated_time,
                                  "is_mandatory": is_mandatory, "release_date": release_date,
                                  "module_id": module_id, "body": body, "is_read": is_read,
                                  "reading_time_minutes": reading_time_minutes,
                                  "is_downloadable": is_downloadable, "word_count": word_count})
    return RedirectResponse(url="/material/text", status_code=303)


# ── Test ─────────────────────────────────────────────────────────
@router.get("/test")
def list_tests(request: Request, service: MaterialService = Depends(get_material_service)):
    tests = [m for m in service.get_all() if m.type == "Test"]
    return templates.TemplateResponse("material/test_list.html", {"request": request, "materials": tests})

@router.get("/test/add")
def add_test_form(request: Request):
    return templates.TemplateResponse("material/test_form.html", {
        "request": request, "action_title": "Додати тест",
        "action_url": "/material/test/add", "material": None, "modules": _modules(),
    })

@router.post("/test/add")
def add_test(
    title: str = Form(...), estimated_time: int = Form(...),
    is_mandatory: bool = Form(False), release_date: date = Form(...),
    module_id: int = Form(...), score: int = Form(...),
    passing_score: int = Form(...), is_passed: bool = Form(False),
    attempts_limit: int = Form(...), time_limit: int = Form(...),
    service: MaterialService = Depends(get_material_service),
):
    service.create({"type": "Test", "title": title, "estimated_time": estimated_time,
                    "is_mandatory": is_mandatory, "release_date": release_date, "module_id": module_id,
                    "score": score, "passing_score": passing_score, "is_passed": is_passed,
                    "attempts_limit": attempts_limit, "time_limit": time_limit})
    return RedirectResponse(url="/material/test", status_code=303)

@router.get("/test/edit/{material_id}")
def edit_test_form(material_id: int, request: Request, service: MaterialService = Depends(get_material_service)):
    material = service.get_by_id(material_id)
    return templates.TemplateResponse("material/test_form.html", {
        "request": request, "action_title": "Редагувати тест",
        "action_url": f"/material/test/edit/{material_id}",
        "material": material, "modules": _modules(),
    })

@router.post("/test/edit/{material_id}")
def edit_test(
    material_id: int,
    title: str = Form(...), estimated_time: int = Form(...),
    is_mandatory: bool = Form(False), release_date: date = Form(...),
    module_id: int = Form(...), score: int = Form(...),
    passing_score: int = Form(...), is_passed: bool = Form(False),
    attempts_limit: int = Form(...), time_limit: int = Form(...),
    service: MaterialService = Depends(get_material_service),
):
    service.update(material_id, {"title": title, "estimated_time": estimated_time,
                                  "is_mandatory": is_mandatory, "release_date": release_date,
                                  "module_id": module_id, "score": score, "passing_score": passing_score,
                                  "is_passed": is_passed, "attempts_limit": attempts_limit,
                                  "time_limit": time_limit})
    return RedirectResponse(url="/material/test", status_code=303)


# ── Delete (shared) ──────────────────────────────────────────────
@router.post("/delete/{material_id}")
def delete_material(material_id: int, service: MaterialService = Depends(get_material_service)):
    service.delete(material_id)
    return RedirectResponse(url="/material", status_code=303)
