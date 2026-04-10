import sqlite3

def buscar_usuario(nome_usuario):
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Executar a consulta para buscar o usuário pelo nome
    cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (nome_usuario,))
    usuario = cursor.fetchone()
    
    # Fechar a conexão com o banco de dados
    conn.close()
    
    return usuario