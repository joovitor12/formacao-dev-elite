# metrics-exporter — imagem de produção (refinada conforme especificacao_app.md).

# --- builder: resolve dependências Python fora do runtime ---
FROM python:3.12.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN mkdir -p /install \
    && pip install --no-cache-dir --prefix=/install -r requirements.txt

# --- runtime: só artefatos necessários para servir HTTP ---
FROM python:3.12.9-slim AS runtime

WORKDIR /app

RUN groupadd --system app \
    && useradd --system --gid app --home /app app

COPY --from=builder /install /usr/local
COPY metrics_exporter.py .

RUN chown -R app:app /app

USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=2)"]

CMD ["python", "metrics_exporter.py"]
