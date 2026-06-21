# Dockerfile com estrutura desorganizada — mesmo baseline raiz e pre-changes/.

FROM python:3.12-slim

COPY metrics_exporter.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

EXPOSE 8080

CMD python metrics_exporter.py

HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1

USER root
