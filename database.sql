CREATE DATABASE IF NOT EXISTS crud_python;

tabela Cliente
CREATE TABLE Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliNome VARCHAR(100) NOT NULL,
    cliIdade INT NOT NULL,
    cliProfissao VARCHAR(100) NOT NULL
);
