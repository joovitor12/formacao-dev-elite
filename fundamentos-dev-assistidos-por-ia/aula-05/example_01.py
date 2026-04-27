usuarios_brutos = [
    "Joao Machado;joao@email.com",
    "Maria Silva;maria@gmail.com",
    "Jose Santos;jose@outlook.com",
    "Ana Oliveira;ana@gmail.com"
]

usuarios = []
for usuario in usuarios_brutos:
    nome, email = usuario.split(';')
    if '@gmail.com' in email:
        usuarios.append({'name': nome, 'email': email})

# usuarios agora contem apenas os dicionarios com emails @gmail

# exemplo de uso
for usuario in usuarios:
    print(f"Nome: {usuario['name']}, Email: {usuario['email']}")


import json
dados = {
    "usuarios": [
        {"name": "Joao Machado", "email": "joao@email.com"},
        {"name": "Maria Silva", "email": "maria@gmail.com"},
        {"name": "Jose Santos", "email": "jose@outlook.com"},
        {"name": "Ana Oliveira", "email": "ana@gmail.com"}
    ]
}

print(json.dumps(dados, indent=4))