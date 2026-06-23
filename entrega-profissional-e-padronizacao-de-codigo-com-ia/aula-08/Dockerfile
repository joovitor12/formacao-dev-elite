# MVP Chatbot — Parlant sandbox (:8800)
# Segredos via runtime: docker run --env-file .env ...

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    OPENROUTER_MODEL=openrouter/owl-alpha \
    OPENROUTER_MAX_TOKENS=128000 \
    PARLANT_HOME=/app/parlant-data

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ ./server/
COPY visao_geral_projeto.md .

RUN useradd --create-home --uid 1000 app \
    && mkdir -p /app/parlant-data \
    && chown -R app:app /app

USER app

EXPOSE 8800

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8800/')"]

CMD ["python", "-m", "server.main"]
