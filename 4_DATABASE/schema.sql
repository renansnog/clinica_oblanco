CREATE DATABASE IF NOT EXISTS clinica_oblanco;
USE clinica_oblanco;

-- Tabela de Consultas
CREATE TABLE IF NOT EXISTS consultas (
    id_Consulta INT AUTO_INCREMENT PRIMARY KEY,
    data_consulta DATE NOT NULL,
    horario TIME NOT NULL,
    descricao TEXT
);

-- Tabela de Pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    id_CPF VARCHAR(11) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    data_de_nascimento DATE,
    pcd ENUM('Sim', 'Não') DEFAULT 'Não',
    id_Consulta INT NULL,
    FOREIGN KEY (id_Consulta) REFERENCES consultas(id_Consulta)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Inserir consultas de teste
INSERT INTO consultas (data_consulta, horario, descricao) VALUES
('2025-08-10', '14:00:00', 'Consulta de implantodontista'),
('2025-08-12', '09:30:00', 'Consulta de protesista');

-- Inserir pacientes de teste
INSERT INTO pacientes (id_CPF, nome, endereco, telefone, data_de_nascimento, pcd, id_Consulta) VALUES
('12345678901', 'Pedro da Silva', 'Rua A, 123', '(51) 99999-1234', '1985-05-10', 'Não', 1),
('98765432100', 'Maria Oliveira', 'Av. Central, 456', '(51) 98888-5678', '1990-02-20', 'Sim', 2);
