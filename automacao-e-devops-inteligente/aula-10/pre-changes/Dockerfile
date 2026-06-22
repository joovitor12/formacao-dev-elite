# Single-stage inchado — refatorar para multistage (builder + runtime) na aula.

FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc build-essential git curl vim \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY metrics_exporter.py .

ENV PORT=8080

EXPOSE 8080

CMD ["python", "metrics_exporter.py"]
