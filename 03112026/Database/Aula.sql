-- Comandos abaixo foram utilizados como exemplo na aula do dia 03/11

CREATE DATABASE vendas; -- Referência 1

USE DATABASE vendas; -- Referência 2

CREATE TABLE cliente ( -- Referência 3
    id_cliente INT PRIMARY KEY, -- Referência 4
    nome VARCHAR(100), -- Referência 5
    cidade VARCHAR(50), -- Referência 6
    idade INT
);

ALTER TABLE cliente -- Referência 7
ADD exemplo INT AUTO_INCREMENT AFTER nome; -- Referência 8

ALTER TABLE cliente -- Referência 9
RENAME COLUMN nome TO nome_cliente; -- Referência 10

ALTER TABLE cliente -- Referência 11
MODIFY cidade VARCHAR(75) NOT NULL; -- Referência 12

ALTER TABLE cliente -- Referência 13
DROP COLUMN exemplo; -- Referência 14

CREATE TABLE IF NOT EXISTS Store_information ( -- Referência 15
    Store_Name VARCHAR(50) NOT NULL, -- Referência 16
    Sales INT NOT NULL, -- Referência 17
    Txn_Date DATE NOT NULL -- Referência 18
);

DROP TABLE Store_information; -- Referência 19

CREATE TABLE IF NOT EXISTS funcionario ( -- Referência 20
    id_funcionario INT AUTO_INCREMENT, -- Referência 21
    nome VARCHAR(100) NOT NULL, -- Referência 22
    cpf CHAR(11) UNIQUE, -- Referência 23
    salario DECIMAL(10,2), -- Referência 24
    data_admissao DATE, -- Referência 25
    ativo BOOLEAN DEFAULT TRUE, -- Referência 26
    PRIMARY KEY (id_funcionario) --  Referência 27
);