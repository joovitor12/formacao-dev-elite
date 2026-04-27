#!/usr/bin/env python3
"""
Script de desenvolvimento para a Loja de Roupas API
"""

import uvicorn
import subprocess
import sys

def start_server():
    """Inicia o servidor de desenvolvimento"""
    print("🚀 Iniciando servidor FastAPI...")
    print("📖 Docs disponíveis em: http://127.0.0.1:8000/docs")
    print("🔧 API em: http://127.0.0.1:8000")
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="info"
    )

def show_help():
    """Mostra comandos disponíveis"""
    print("""
    🛠️  Comandos disponíveis:
    
    python dev.py start    - Inicia o servidor de desenvolvimento
    python dev.py help     - Mostra esta mensagem
    
    📁 Estrutura do projeto:
    ├── main.py           - Aplicação FastAPI principal
    ├── enum_cores.py     - Enumeração das cores
    ├── api.py           - Modelos Pydantic
    └── dev.py           - Script de desenvolvimento
    
    🌐 URLs importantes:
    - API: http://127.0.0.1:8000
    - Docs: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    elif sys.argv[1] == "start":
        start_server()
    elif sys.argv[1] == "help":
        show_help()
    else:
        print(f"❌ Comando desconhecido: {sys.argv[1]}")
        show_help()