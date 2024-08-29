from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_quiz(request: Request):
    return templates.TemplateResponse("quiz.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit_quiz(request: Request, answer1: str = Form(...), answer2: str = Form(...)):
    # Example answers
    correct_answers = {"answer1": "option1", "answer2": "option2"}
    score = 0
    
    if answer1 == correct_answers["answer1"]:
        score += 1
    if answer2 == correct_answers["answer2"]:
        score += 1
    
    return templates.TemplateResponse("result.html", {"request": request, "score": score})
