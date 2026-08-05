"""
Testes da camada de conexão com o banco.

Garantem que as credenciais venham do ambiente (.env) e que nenhuma delas
volte a ser escrita direto no código — este repositório é público.

Como rodar (a partir da raiz do projeto):
    python -m unittest discover -s testes -v
"""
import os
import sys
import unittest
from pathlib import Path
from unittest import mock

# Permite importar os módulos do projeto ao rodar os testes da raiz
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import services.database as database  # noqa: E402

ARQUIVO_DATABASE = Path(__file__).resolve().parent.parent / "services" / "database.py"


class TesteCredenciaisVemDoAmbiente(unittest.TestCase):
    """A conexão precisa ser montada com o que está no ambiente, não no código."""

    def teste_conexao_usa_os_valores_das_variaveis_de_ambiente(self):
        ambiente = {
            "DB_HOST": "host-de-teste",
            "DB_NOME": "banco-de-teste",
            "DB_USUARIO": "usuario-de-teste",
            "DB_SENHA": "senha-de-teste",
        }

        with mock.patch.dict(os.environ, ambiente, clear=False):
            with mock.patch("mysql.connector.connect") as conectar_falso:
                conectar_falso.return_value.is_connected.return_value = True
                database.criar_conexao()

        parametros = conectar_falso.call_args.kwargs
        self.assertEqual(parametros["host"], "host-de-teste")
        self.assertEqual(parametros["database"], "banco-de-teste")
        self.assertEqual(parametros["user"], "usuario-de-teste")
        self.assertEqual(parametros["password"], "senha-de-teste")


class TesteAusenciaDeCredenciaisNoCodigo(unittest.TestCase):
    """
    Guarda de regressão: impede que alguém volte a colar usuário e senha
    no arquivo. O repositório é público — isso não pode reaparecer.
    """

    def teste_arquivo_nao_contem_credenciais_escritas_no_codigo(self):
        # As credenciais são lidas do ambiente, e não escritas aqui: este
        # arquivo de teste também é versionado num repositório público.
        credenciais = [
            os.getenv("DB_USUARIO"),
            os.getenv("DB_SENHA"),
        ]
        credenciais = [c for c in credenciais if c]

        self.assertTrue(
            credenciais,
            "nenhuma credencial no ambiente — configure o .env antes de rodar os testes"
        )

        codigo = ARQUIVO_DATABASE.read_text(encoding="utf-8")
        for credencial in credenciais:
            self.assertNotIn(
                credencial, codigo,
                "credencial do .env encontrada escrita em services/database.py"
            )


if __name__ == "__main__":
    unittest.main()
