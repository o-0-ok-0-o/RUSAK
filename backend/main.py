from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from api_v1.routers import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


app.include_router(router)


@app.get("/")
async def root():
    return {
        "site": "Rusak",
    }


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
