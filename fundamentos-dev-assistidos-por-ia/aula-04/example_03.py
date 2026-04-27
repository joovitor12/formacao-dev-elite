import hashlib
import os

def gerar_hash_senha(senha: str):
    """Funcao para gerar um hash seguro para a senha passada
    Restritores:
    - Nao usa MD5 ou SHA1, pois sao obsoletos
    - Usa obrigatoriamente o hashlib com SHA256
    - Adicionar um salt fixo de uma variavel de ambiente
    """
    salt = os.getenv("SALT_HASH", "salt_fixo_para_exemplo")
    senha_com_salt = senha + salt
    hash_senha = hashlib.sha256(senha_com_salt.encode()).hexdigest()
    return hash_senha


# Exemplo de uso:
if __name__ == "__main__":
    senha = os.getenv("SENHA_EXEMPLO", "senha123")
    hash_resultado = gerar_hash_senha(senha)
    print(f"Senha original: {senha}")
    print(f"Hash da senha: {hash_resultado}")