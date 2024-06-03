FROM python:3.12.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apk update && \
    apk add --no-cache python3-dev \
    postgresql-dev gcc musl-dev \
    postgresql zlib jpeg-dev libjpeg \
    freetype-dev fribidi-dev harfbuzz-dev \
    lcms2-dev openjpeg-dev tcl-dev tiff-dev \
    tk-dev zlib-dev nmap

ADD pyproject.toml /app

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY . /app/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
