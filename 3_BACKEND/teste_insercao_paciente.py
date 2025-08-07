from inserir_paciente import inserir_paciente

# Exemplo de dados fictícios
inserir_paciente(
    id_CPF="12345678901",
    nome="Pedro da Silva",
    endereco="Rua A, 123",
    telefone="(51) 99999-1234",
    data_de_nascimento="10/05/1985",
    pcd="Não",
    id_Consulta=None  # ou um ID existente na tabela consultas
)
