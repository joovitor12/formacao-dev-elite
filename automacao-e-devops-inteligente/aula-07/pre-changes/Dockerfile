# Dockerfile com achados intencionais — mesmo baseline da raiz e de pre-changes/.

FROM python:latest

WORKDIR /app

ENV METRICS_API_KEY=pipe_live_8c4f91a0e2bd

RUN apt-get update && apt-get install -y curl vim

COPY . .

EXPOSE 8080

CMD python metrics_exporter.py
