import os
from pathlib import Path

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Carrega o .env da raiz do projeto.
# O caminho é montado a partir deste arquivo (e não do diretório atual) para
# que a conexão funcione independentemente de onde o app foi iniciado.
CAMINHO_ENV = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(CAMINHO_ENV)


def criar_conexao():
    """
    Abre uma conexão com o banco MySQL usando as credenciais do ambiente.

    As credenciais nunca ficam no código: vêm do arquivo .env, que não é
    versionado. O .env.example documenta quais variáveis são esperadas.

    @return  Objeto de conexão do mysql.connector, ou None se a conexão falhar
    """
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USUARIO"),
            password=os.getenv("DB_SENHA"),
            database=os.getenv("DB_NOME"),
        )

        if conexao.is_connected():
            return conexao

    except Error as erro:
        # A mensagem técnica vai para o terminal de quem administra a aplicação.
        # A tela do usuário recebe apenas o aviso genérico tratado no controller.
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None


def fechar_conexao(conexao):
    """
    Fecha a conexão com o banco, se ela estiver aberta.

    @param conexao  Objeto de conexão devolvido por criar_conexao()
    """
    if conexao and conexao.is_connected():
        conexao.close()
