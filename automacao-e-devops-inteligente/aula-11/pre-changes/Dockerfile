# Imagem funcional porém inchada — otimizar tamanho, camadas e contexto na aula.

FROM python:3.12 AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y gcc build-essential git curl vim

COPY . .
RUN pip install -r requirements.txt

FROM python:3.12 AS runtime

WORKDIR /app

RUN apt-get update && apt-get install -y curl vim git netcat-openbsd

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app /app

ENV PORT=8080
ENV PYTHONUNBUFFERED=1
ENV DEBUG=true

EXPOSE 8080

CMD ["python", "metrics_exporter.py"]
