from conexao import conectar
from werkzeug.security import generate_password_hash

def criar_admin(username, senha, nome=None):
    conn = conectar()
    cur = conn.cursor()
    sql = "INSERT INTO administradores (username, password_hash, nome) VALUES (%s, %s, %s)"
    hash_senha = generate_password_hash(senha)  # ex.: pbkdf2:sha256
    cur.execute(sql, (username, hash_senha, nome))
    conn.commit()
    print(f"✅ Admin '{username}' criado.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    criar_admin("admin", "1234", "Administrador")
