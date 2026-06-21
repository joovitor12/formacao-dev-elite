# Dockerfile reorganizado por blocos — WORKDIR único alinha COPY e CMD.

# --- Base ---
FROM python:3.12-slim

# --- Workspace ---
WORKDIR /app

# --- Dependências ---
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Código da app ---
COPY metrics_exporter.py .

# --- Identidade ---
RUN useradd --create-home --uid 1000 app \
    && chown -R app:app /app
USER app

# --- Rede ---
EXPOSE 8080

# --- Saúde ---
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD ["python", "-c", "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')"]

# --- Entrada ---
CMD ["python", "metrics_exporter.py"]
