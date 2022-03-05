FROM python:3.9

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV ALLOWED_HOSTS *

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /code/


RUN python manage.py collectstatic --noinput