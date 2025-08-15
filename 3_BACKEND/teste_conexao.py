from conexao import conectar

conexao = conectar()

if conexao:
    conexao.close()
    print("🔒 Conexão encerrada.")
from conexao import conectar

try:
    conn = conectar()
    print("✅ Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print("❌ Erro ao conectar:", e)
