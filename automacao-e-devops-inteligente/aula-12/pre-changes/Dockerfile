# Baseline funcional com falhas de segurança — corrigir na aula.

FROM python:latest

WORKDIR /app

ARG REGISTRY_TOKEN=reg_live_default_insecure
ENV METRICS_API_KEY=pipe_live_8c4f91a0e2bd
ENV DEBUG=true

RUN apt-get update && apt-get install -y curl sudo

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8080 22

CMD python metrics_exporter.py
