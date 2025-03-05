from fastapi import APIRouter, Depends

router = APIRouter(
    prefix="/orders",
    tags=["Заказы"],
)


@app.get("/car", response_model=list[CarSchema])
def get_extras():

    return available_extras


@app.get("/engine", response_model=list[Option])
def get_models():
    return available_models


@app.get("/salone-member", response_model=list[Option])
def get_colors():
    return available_colors


@app.get("/salone-option", response_model=list[Option])
def get_engines():
    return available_engines


@app.get("/service", response_model=list[Option])
def get_extras():
    return available_extras


@app.get("/shassi", response_model=list[Option])
def get_extras():
    return available_extras


@app.get("/zip", response_model=list[Option])
def get_extras():
    return available_extras
