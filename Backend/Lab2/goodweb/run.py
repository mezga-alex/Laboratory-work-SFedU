from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import components
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})


@app.get("/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name,
        "service_parts": ["TEST-1", "TEST-2", "TEST-3"]
    }
    return templates.TemplateResponse(f"{page_name}",
                                      {
                                          "request": request,
                                          "id": 1000000,
                                          "service_parts": components.SERVICES_CARDS,
                                          "services_widget": components.SERVICES_WIDGET}
                                      )


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=8000, log_level="info")
