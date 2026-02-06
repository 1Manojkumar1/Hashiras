from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from schemas import CurriculumRequest, CurriculumResponse
from ai_engine import generate_curriculum_with_gemini
from chatbot import get_chat_response

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")


# Chat request model
class ChatRequest(BaseModel):
    message: str

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


@app.post("/chat")
def chat(data: ChatRequest):
    """Handle chatbot messages."""
    response = get_chat_response(data.message)
    return {"response": response}