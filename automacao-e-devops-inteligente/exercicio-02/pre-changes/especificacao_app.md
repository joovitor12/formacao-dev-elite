# Especificação da app — exercício integrador

Use com IA na fase de geração/refino do Dockerfile (`@especificacao_app.md`).

## Identificação

- Nome do serviço: metrics-exporter
- Descrição: HTTP mínimo de health e métricas para o exercício integrador

## Runtime

- Linguagem / versão: Python 3.12+
- Entry point: `python metrics_exporter.py`
- Variáveis de ambiente: `PORT` (default 8080), `HOST` (default 0.0.0.0)

## Rede

- Porta padrão: 8080
- Porta configurável: sim (`PORT`)
- Host de bind: 0.0.0.0
- Protocolo: HTTP

## Endpoints

| Método | Rota | Resposta esperada |
|--------|------|-------------------|
| GET | /health | 200, corpo `ok` |
| GET | /metrics | 200, text/plain |

## Dependências

- Arquivo: `requirements.txt`
- Pacotes: stdlib / nenhum externo
- Instalação: `pip install -r requirements.txt`

## Restrições desejadas na imagem

- Base `python:3.12.x-slim` com tag fixa
- Multistage (build de deps separado do runtime)
- Usuário não-root
- CMD exec form
- HEALTHCHECK em `/health` com comando disponível na imagem
- COPY seletivo; `.dockerignore` robusto
- Sem segredos em ENV/ARG do Dockerfile
- Imagem final sem ferramentas de build (gcc, git, vim, sudo)

## Contexto de build

Incluir na imagem:

- `metrics_exporter.py`
- `requirements.txt`

Excluir:

- `example.py`, `*.md`, `dossie_container_integrado.md`

## Validação esperada

```bash
python example.py
docker build -t metrics-exporter:integrador .
docker run --rm -p 8080:8080 metrics-exporter:integrador
curl http://127.0.0.1:8080/health
```
