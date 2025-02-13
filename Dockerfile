# Dockerfile
FROM python:3.13.2-slim

WORKDIR /app

COPY app.py /app

RUN pip install flask

EXPOSE 80

CMD ["python", "app.py"]
