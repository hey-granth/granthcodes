from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import markdown

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    with open("markdown/home.md") as f:
        content = f.read()
    html_content = markdown.markdown(content)
    return templates.TemplateResponse("index.html", {"request": {}, "content": html_content})
@app.get("/about")
async def home():
    with open("markdown/about.md") as f:
        content = f.read()
    html_content = markdown.markdown(content)
    return templates.TemplateResponse("index.html", {"request": {}, "content": html_content})

