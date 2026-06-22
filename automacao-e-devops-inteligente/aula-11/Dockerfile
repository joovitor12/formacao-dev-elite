# Multistage enxuto — base slim, sem apt de debug, COPY seletivo.

FROM python:3.12.13-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN mkdir -p /install && pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12.13-slim AS runtime

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY --from=builder /install /usr/local
COPY --chown=app:app metrics_exporter.py .

ENV PORT=8080
ENV PYTHONUNBUFFERED=1

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import os, urllib.request; p=os.environ.get('PORT', '8080'); r=urllib.request.urlopen(f'http://127.0.0.1:{p}/health', timeout=2); exit(0 if r.read() == b'ok' else 1)"]

CMD ["python", "metrics_exporter.py"]
