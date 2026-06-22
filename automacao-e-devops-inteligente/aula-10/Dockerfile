# Multistage: builder prepara deps; runtime executa app enxuta.

FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:14.2.0-1 \
    build-essential=12.12 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN mkdir -p /install && pip install --no-cache-dir --prefix=/install -r requirements.txt

FROM python:3.12-slim AS runtime

WORKDIR /app

RUN addgroup --system app && adduser --system --group app

COPY --from=builder /install /usr/local
COPY --chown=app:app metrics_exporter.py .

# App e HEALTHCHECK leem PORT (default 8080; sobrescreva com -e PORT=... no run).
ENV PORT=8080

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import os, urllib.request; p=os.environ.get('PORT', '8080'); r=urllib.request.urlopen(f'http://127.0.0.1:{p}/health', timeout=2); exit(0 if r.read() == b'ok' else 1)"]

CMD ["python", "metrics_exporter.py"]
