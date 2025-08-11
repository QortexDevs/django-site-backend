FROM python:3.12.6

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    wget \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry==1.8.3

WORKDIR /code/

COPY pyproject.toml .

RUN poetry lock --no-update && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

COPY . /code/

CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8000", "app.wsgi:application"]