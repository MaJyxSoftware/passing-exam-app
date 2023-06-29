FROM python:alpine

LABEL version="1.0.0"
LABEL maintainer="Benjamin Schwald"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000
VOLUME [ "/var/www" ]

RUN adduser -S django -G root

USER django
WORKDIR /app

COPY src/requirements.txt /app/

RUN pip install -r requirements.txt

COPY src/ /app/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
