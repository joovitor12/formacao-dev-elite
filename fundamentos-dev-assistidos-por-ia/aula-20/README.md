# FastAPI Boilerplate

Boilerplate inicial de uma API com FastAPI.

## Requisitos

- Python 3.10+

## Instalacao

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)
pip install -r requirements.txt
```

## Rodando localmente

```bash
uvicorn app.main:app --reload
```

API disponivel em:

- `http://127.0.0.1:8000`
- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoint inicial

- `GET /api/v1/health`
