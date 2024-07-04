from fastapi.responses import JSONResponse
from RS.Get_predicted_value import get_predicted_value
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
# TODO: receiving symptoms from doctor "frontend" to passing them to the mode
async def symptoms(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload")
async def receive_array(array: list):
    text = get_predicted_value(array)  # Pass the array to text_extraction
    return JSONResponse(content=text)


if name == "main":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
