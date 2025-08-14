from flask import Flask, jsonify
from conexao import conectar

app = Flask(__name__)

@app.route("/pacientes")
def listar_pacientes():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return jsonify(pacientes)
    else:
        return jsonify({"erro": "Não foi possível conectar ao banco"}), 500

if __name__ == "__main__":
    app.run(debug=True)
