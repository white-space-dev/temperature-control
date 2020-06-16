FROM python:3.9.0b3-alpine3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN apk --update --upgrade --no-cache add \
    cairo-dev pango-dev gdk-pixbuf gcc musl-dev jpeg-dev zlib-dev libffi-dev fontconfig ttf-dejavu

COPY ./requirement.txt /app/requirement.txt

RUN pip install -r requirement.txt

COPY . /app