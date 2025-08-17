from flask import Flask, request, jsonify
from flask_cors import CORS
from conexao import conectar
from werkzeug.security import check_password_hash

app = Flask(__name__)
# Libera chamadas do front (inclusive Live Server)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"ok": False, "message": "Informe usuário e senha."}), 400

    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id, username, password_hash, nome FROM administradores WHERE username = %s", (username,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        return jsonify({"ok": False, "message": "Usuário ou senha inválidos."}), 401

    admin_id, uname, pw_hash, nome = row
    if not check_password_hash(pw_hash, password):
        return jsonify({"ok": False, "message": "Usuário ou senha inválidos."}), 401

    return jsonify({"ok": True, "admin": {"id": admin_id, "username": uname, "nome": nome}})
    
if __name__ == "__main__":
    app.run(debug=True)
