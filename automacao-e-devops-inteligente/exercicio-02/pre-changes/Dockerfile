# Baseline integrador — Dockerfile problemático (revisar e endurecer no exercício).

FROM python:latest

ENV METRICS_API_KEY=pipe_live_integrador_9f2a
ENV DEBUG=true

COPY metrics_exporter.py .
COPY requirements.txt .

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential git curl vim sudo

RUN pip install -r requirements.txt

EXPOSE 8080 22

CMD python metrics_exporter.py
