import mysql.connector
from mysql.connector import Error


def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="crud_user",          # seu usuário MySQL
            password="senha123",  # coloque sua senha aqui
            database="crud_python"
        )

        if conexao.is_connected():
            return conexao

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def fechar_conexao(conexao):
    if conexao and conexao.is_connected():
        conexao.close()
