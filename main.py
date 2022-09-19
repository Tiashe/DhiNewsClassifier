from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from model import DhivehiNewsClassifier

classifier = DhivehiNewsClassifier()

app = FastAPI(
    title="Dhivehi News Classifier",
    description="Dhivehi News Classifier",
    version="0.0.1",
)

app.mount("/assets", StaticFiles(directory="templates/assets"), name="assets")

templates = Jinja2Templates(directory="templates")


@app.get('/', response_class=HTMLResponse, include_in_schema=False)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/compare/")
async def multi_word(request: Request):
    data = await request.json()
    original_title = data['original']
    comparing_titles = data['comparing']
    result = DhivehiNewsClassifier.compare_titles(original_title, comparing_titles)
    return {
        "result": result
    }
