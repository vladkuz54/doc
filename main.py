from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from presentation.routers import course_router, module_router, material_router

app = FastAPI()

# Підключення статичних файлів (CSS/JS)
app.mount("/static", StaticFiles(directory="presentation/static"), name="static")

templates = Jinja2Templates(directory="presentation/templates")

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Реєстрація контролерів (роутерів)
app.include_router(course_router.router)
app.include_router(module_router.router)
app.include_router(material_router.router)