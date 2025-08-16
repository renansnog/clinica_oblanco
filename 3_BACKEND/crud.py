from conexao import conectar

# Inserir paciente
def inserir_paciente(id_CPF, nome, endereco, telefone, data_nasc, pcd):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO pacientes (id_CPF, nome, endereco, telefone, data_de_nascimento, pcd)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (id_CPF, nome, endereco, telefone, data_nasc, pcd)
    cursor.execute(sql, valores)
    conn.commit()
    print(f"✅ Paciente {nome} inserido com sucesso!")
    conn.close()

# Buscar pacientes
def listar_pacientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pacientes")
    resultados = cursor.fetchall()
    for paciente in resultados:
        print(paciente)
    conn.close()

# Inserir consulta
def inserir_consulta(data_consulta, horario, descricao):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO consultas (data_consulta, horario, descricao)
        VALUES (%s, %s, %s)
    """
    valores = (data_consulta, horario, descricao)
    cursor.execute(sql, valores)
    conn.commit()
    print("✅ Consulta inserida com sucesso!")
    conn.close()

# Buscar consultas
def listar_consultas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM consultas")
    resultados = cursor.fetchall()
    for consulta in resultados:
        print(consulta)
    conn.close()
