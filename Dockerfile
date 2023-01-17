FROM python:3.8-alpine

COPY app.py /app/app.py

RUN apk add --no-cache build-base

RUN pip install --upgrade pip

CMD ["python", "/app/app.py"]