import os
from fastapi import FastAPI
import uvicorn
from db.models import router
from db.database import sqlite_file_name, engine
from sqlmodel import SQLModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


app.include_router(router)


@app.get("/")
async def root():
    return {
        "site": "Rusak",
    }


if __name__ == "__main__":
    if not os.path.exists(sqlite_file_name):
        print("Database file not found. Creating an empty database file...")
        with open(sqlite_file_name, "w") as f:
            pass

        print("Database file created. Now creating tables...")
        SQLModel.metadata.create_all(engine)
        print("Database tables created.")
    else:
        print("Database file found. Skipping database and table creation.")
        SQLModel.metadata.create_all(engine)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
