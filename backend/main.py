from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from src.api.routers.user_router import router as user_router
from src.api.routers.tag_router import router as tag_router
from src.api.routers.category_router import router as category_router
from src.api.routers.article_router import router as article_router
from src.demo_auth.demo_jwt_auth import router as auth_jwt_router


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_router)
app.include_router(tag_router)
app.include_router(category_router)
app.include_router(article_router)
app.include_router(auth_jwt_router)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "journalblog": "website"}
    )


# if __name__ == "__main__":
#     uvicorn.run(app)
