# Imagem de produção — segredos via runtime (docker run -e / orchestrator secrets).

FROM python:3.12.9-slim

WORKDIR /app

RUN groupadd --system app \
    && useradd --system --gid app --home /app app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY metrics_exporter.py .

RUN chown -R app:app /app

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2)"]

CMD ["python", "metrics_exporter.py"]
