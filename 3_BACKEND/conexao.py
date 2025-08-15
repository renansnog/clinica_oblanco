import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="SUA_SENHA",   # coloque sua senha do MySQL
        database="clinica_oblanco"
    )

