from fastapi import FastAPI
from controller import router

app = FastAPI(
    title="Loja de Roupas API",
    description="API para gerenciar roupas da loja",
    version="1.0.0"
)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
