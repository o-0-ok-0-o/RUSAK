from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/orders",
    tags=["Заказы"],
)


@app.get("/models/", response_model=List[Option])
def get_models():
    return available_models


@app.get("/colors/", response_model=List[Option])
def get_colors():
    return available_colors


@app.get("/engines/", response_model=List[Option])
def get_engines():
    return available_engines


@app.get("/extras/", response_model=List[Option])
def get_extras():
    return available_extras
