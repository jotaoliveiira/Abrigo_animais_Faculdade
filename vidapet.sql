CREATE DATABASE vidapet;

USE vidapet;

CREATE TABLE tbl_adotante (
    id_adotante INT AUTO_INCREMENT PRIMARY KEY,
    nome_adotante VARCHAR(100) NOT NULL,
    telefone_adotante VARCHAR(20),
    cpf_adotante VARCHAR(14),
    email_adotante VARCHAR(100),
    cep_adotante VARCHAR(9),
    logradouro_adotante VARCHAR(100),
    complemento_adotante VARCHAR(100)
);

CREATE TABLE tbl_doador (
    id_doador INT AUTO_INCREMENT PRIMARY KEY,
    nome_doador VARCHAR(100) NOT NULL,
    telefone_doador VARCHAR(20),
    email_doador VARCHAR(100),
    cpf_doador VARCHAR(14),
    cep_doador VARCHAR(9),
    logradouro_doador VARCHAR(100),
    complemento_doador VARCHAR(100),
    motivo_doador VARCHAR(200),
    descricao_doador VARCHAR(200)
);

CREATE TABLE tbl_animal (
    id_animal INT AUTO_INCREMENT PRIMARY KEY,
    nome_animal VARCHAR(100) NOT NULL,
    especie_animal ENUM('Cachorro', 'Gato') NOT NULL,
    raca_animal VARCHAR(100),
    data_nascimento DATE,
    sexo_animal ENUM('Macho', 'Fêmea') NOT NULL,
    porte_animal ENUM('Pequeno', 'Médio', 'Grande'),
    status_animal BOOL NOT NULL,
    id_doador INT,
    id_adotante INT,
    FOREIGN KEY (id_doador) REFERENCES tbl_doador(id_doador),
    FOREIGN KEY (id_adotante) REFERENCES tbl_adotante(id_adotante)
);

CREATE TABLE tbl_atendimento (
    id_atendimento INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT NOT NULL,
    data_atendimento DATE NOT NULL,
    descricao_atendimento VARCHAR(100) NOT NULL,
    diagnostico_atendimento VARCHAR(100),
    tratamento_atendimento VARCHAR(200),
    FOREIGN KEY (id_animal) REFERENCES tbl_animal(id_animal)
);

CREATE TABLE tbl_vacina (
    id_vacina INT AUTO_INCREMENT PRIMARY KEY,
    id_animal INT NOT NULL,
    nome_vacina VARCHAR(100) NOT NULL,
    data_vacina DATE NOT NULL,
    descricao_vacina VARCHAR(100),
    FOREIGN KEY (id_animal) REFERENCES tbl_animal(id_animal)
);

SELECT
    nome_animal,
    data_nascimento,
    TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) AS anos,
    TIMESTAMPDIFF(MONTH, data_nascimento, CURDATE()) % 12 AS meses
FROM tbl_animal;