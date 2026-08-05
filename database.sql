-- ============================================================
-- Estrutura do banco de dados do projeto CRUD
--
-- Como executar (a partir da raiz do projeto):
--     mysql -u root -p < database.sql
--
-- O script é idempotente: pode ser executado mais de uma vez
-- sem erro e sem apagar dados já existentes.
-- ============================================================

CREATE DATABASE IF NOT EXISTS crud_python
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;

-- Seleciona o banco recém-criado. Sem esta linha, o CREATE TABLE
-- abaixo falha com "No database selected".
USE crud_python;

-- Tabela Cliente
CREATE TABLE IF NOT EXISTS Cliente (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    cliNome      VARCHAR(100) NOT NULL,
    cliIdade     INT          NOT NULL,
    cliProfissao VARCHAR(100) NOT NULL
);
