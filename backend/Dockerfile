FROM python:3.11.4-slim-bullseye
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./pyproject.toml /code/
COPY ./poetry.lock /code/

RUN pip install poetry
RUN poetry install --no-interaction --no-ansi

COPY . /code/
# CMD [ "poetry", "run", "python", "-m", "main" ]
