from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles  # ← ADD THIS IMPORT

from schemas import CurriculumRequest, CurriculumResponse
from ai_engine import generate_curriculum_with_gemini

app = FastAPI()

# 👇 MOUNT STATIC FILES (critical!)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/generate", response_class=HTMLResponse)
def get_generate(request: Request):
    return templates.TemplateResponse("generate.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def get_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
def get_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/generate", response_model=CurriculumResponse)
def generate_curriculum(data: CurriculumRequest):
    input_data = data.dict()
    result_dict = generate_curriculum_with_gemini(input_data)
    return CurriculumResponse(**result_dict)