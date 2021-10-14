FROM python:3.9.7-bullseye
RUN apt-get update

RUN mkdir -p /applications/lunar_phases
WORKDIR /applications/lunar_phases

COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN DJANGO_SUPERUSER_PASSWORD=admin123 python manage.py createsuperuser --no-input --email=admin@example.com

CMD python manage.py runserver 0.0.0.0:8000