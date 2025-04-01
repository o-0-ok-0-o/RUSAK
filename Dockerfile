FROM python:3.12-alpine

WORKDIR /app

# После WORKDIR /app добавьте:
ENV PYTHONPATH="/app:/app/backend"

# Устанавливаем системные зависимости
RUN apk add --no-cache curl

# Ставим Poetry (без виртуальных окружений)
RUN curl -sSL https://install.python-poetry.org | python - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    poetry config virtualenvs.create false

# 1. Копируем ТОЛЬКО файлы зависимостей
COPY pyproject.toml poetry.lock ./

# 2. Устанавливаем зависимости (но не текущий проект)
RUN poetry install --no-root --no-interaction --no-ansi

# 3. Копируем ВЕСЬ код проекта
COPY . .

# Запуск FastAPI (Uvicorn)
CMD ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]