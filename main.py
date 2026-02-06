from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

from schemas import CurriculumRequest, CurriculumResponse
from ai_engine import generate_curriculum_with_gemini
from chatbot import get_chat_response
from syllabus_generator import generate_syllabus
from gap_analyzer import analyze_gap

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


# Request models
class ChatRequest(BaseModel):
    message: str

class SyllabusRequest(BaseModel):
    course_name: str
    program: str
    domain: str

class GapRequest(BaseModel):
    curriculum_summary: str
    job_description: str


@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/generate", response_class=HTMLResponse)
def get_generate(request: Request):
    return templates.TemplateResponse("generate.html", {"request": request})

@app.get("/gap", response_class=HTMLResponse)
def get_gap(request: Request):
    return templates.TemplateResponse("gap.html", {"request": request})

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


@app.post("/chat")
def chat(data: ChatRequest):
    """Handle chatbot messages."""
    response = get_chat_response(data.message)
    return {"response": response}


@app.post("/generate-syllabus")
def syllabus(data: SyllabusRequest):
    """Generate detailed syllabus for a course."""
    result = generate_syllabus(data.course_name, data.program, data.domain)
    return {"syllabus": result}


@app.post("/analyze-gap")
def gap(data: GapRequest):
    """Analyze gap between curriculum and job requirements."""
    result = analyze_gap(data.curriculum_summary, data.job_description)
    return {"analysis": result}


class ResourceRequest(BaseModel):
    course_name: str
    domain: str = ""


@app.post("/get-resources")
def resources(data: ResourceRequest):
    """Get curated learning resources for a course."""
    from resource_hub import get_course_resources
    result = get_course_resources(data.course_name, data.domain)
    return result