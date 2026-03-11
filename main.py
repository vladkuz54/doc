from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from presentation.routers import course_router, module_router, material_router, api_router

app = FastAPI()
templates = Jinja2Templates(directory="presentation/templates")

@app.get("/", include_in_schema=False)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

app.include_router(course_router.router, include_in_schema=False)
app.include_router(module_router.router, include_in_schema=False)
app.include_router(material_router.router, include_in_schema=False)
app.include_router(api_router.router)
