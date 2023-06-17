FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install poetry

RUN poetry install --no-interaction --no-ansi

COPY . /app/
