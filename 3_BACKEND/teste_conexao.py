from conexao import conectar

conexao = conectar()

if conexao:
    conexao.close()
    print("🔒 Conexão encerrada.")
