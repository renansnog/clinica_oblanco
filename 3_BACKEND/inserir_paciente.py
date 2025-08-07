from conexao import conectar

def inserir_paciente(id_CPF, nome, endereco, telefone, data_de_nascimento, pcd, id_Consulta):
    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            sql = """
                INSERT INTO pacientes (
                    id_CPF, nome, endereco, telefone, data_de_nascimento, pcd, id_Consulta
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            valores = (id_CPF, nome, endereco, telefone, data_de_nascimento, pcd, id_Consulta)
            cursor.execute(sql, valores)
            conexao.commit()
            print("Paciente inserido com sucesso!")

        except Exception as erro:
            print(f"Erro ao inserir paciente: {erro}")

        finally:
            cursor.close()
            conexao.close()
