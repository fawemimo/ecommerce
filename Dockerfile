FROM python:3.10-alpine

WORKDIR C:/projects/ecommerce

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

# RUN pip install --upgrade pip
# COPY ./requirements.txt C:/projects/ecommerce/requirements.txt
# RUN pip install -r requirements.txt