FROM python:3.9.14-alpine

RUN apk add --no-cache libpq

RUN apk add --no-cache tzdata
ENV TZ=Europe/Kiev

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 80

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
