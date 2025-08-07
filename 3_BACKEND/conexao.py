import mysql.connector

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",  # Substitua por sua senha real do MySQL
            database="clínica_oblanco"
        )
        print("✅ Conexão com o banco de dados realizada com sucesso!")
        return conexao
    except mysql.connector.Error as erro:
        print(f"❌ Erro ao conectar ao MySQL: {erro}")
        return None
