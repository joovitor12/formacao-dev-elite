from typing import Dict, Optional


usuarios = [
    {"nome": "Joao", "email": "joao@proway.com", "ativo": True},
    {"nome": "Maria", "email": "maria@gmail.com", "ativo": False},
    {"nome": "Jose", "email": "jose@proway.com", "ativo": True},
]
    

def buscar_usuario(email: str) -> Optional[Dict[str, object]]:
    return next((u for u in usuarios if u["email"] == email), None)

def listar_ativos_empresa() -> list[Dict[str, object]]:
    return [x for x in usuarios if x["ativo"] and "@proway.com" in x["email"]]

def deletar_usuario(email: str) -> bool:
    usuario = buscar_usuario(email)
    if usuario:
        usuarios.remove(usuario)
        return True
    return False

# Exemplos de uso
print(deletar_usuario("joao@proway.com"))
print(listar_ativos_empresa())
