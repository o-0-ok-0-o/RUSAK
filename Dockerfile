FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock README.MD ./

RUN pip install poetry \
    && poetry install

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]