FROM python:3.9.14-alpine

RUN apk add --no-cache libpq

RUN apk add --no-cache tzdata
ENV TZ=Europe/Kiev

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
