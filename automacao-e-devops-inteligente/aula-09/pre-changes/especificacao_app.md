# Especificação da app — insumo para gerar o Dockerfile com IA

Use junto com `metrics_exporter.py` e `requirements.txt` nos prompts. **Não** inclui o Dockerfile pronto.

Para outras apps, duplique `especificacao_app.template.md` → `especificacao_app.md` e preencha.

## Runtime

- Python 3.12+
- Entry point: `python metrics_exporter.py` (função `main()` no `__m__`)

## Rede

- Porta padrão: **8080** (sobrescrevível via env `PORT`)
- Host padrão: `0.0.0.0` (env `HOST` opcional)

## Endpoints

| Rota | Resposta |
|------|----------|
| `GET /health` | `200` corpo `ok` |
| `GET /metrics` | `200` text/plain com métricas mínimas |

## Dependências

- Apenas biblioteca padrão — `requirements.txt` sem pacotes pip externos.

## Restrições desejadas na imagem

- Base `python:3.12.x-slim` com **tag fixa** (sem `latest`)
- Usuário **não-root**
- `CMD` em **exec form**
- `HEALTHCHECK` em `/health` (comando disponível na imagem — ex.: `python -c` + urllib)
- `COPY` seletivo — não copiar `example.py` nem arquivos `.md` de documentação
- Segredos **não** em `ENV`/`ARG` do Dockerfile

## Contexto de build

Arquivos relevantes no diretório da aula:

- `metrics_exporter.py`
- `requirements.txt`
- `example.py` (smoke test local — **não** incluir na imagem)
