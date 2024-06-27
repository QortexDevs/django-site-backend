FROM python:3.12.4

RUN apt-get update && apt-get upgrade -y && apt-get install -y wget

WORKDIR /
ENV PYTHONUNBUFFERED=1
COPY pyproject.toml /code/

WORKDIR /code

RUN pip install poetry
RUN poetry install

COPY . /code/

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
