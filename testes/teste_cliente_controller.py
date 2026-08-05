"""
Testes do ClienteController.

Focam no comportamento quando o banco está indisponível: nenhuma operação
pode estourar exceção na tela do usuário. Todas devem avisar e devolver um
valor previsível, como já faziam inserir_cliente e SelecionarTodos.

Como rodar (a partir da raiz do projeto):
    python -m unittest discover -s testes -v
"""
import sys
import unittest
from pathlib import Path
from unittest import mock

# Permite importar os módulos do projeto ao rodar os testes da raiz
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import controllers.ClienteController as ClienteController  # noqa: E402


class TesteComportamentoComBancoIndisponivel(unittest.TestCase):
    """
    Quando criar_conexao() devolve None — banco fora do ar, credencial errada,
    rede caída — nenhuma função pode deixar a exceção vazar para a interface.
    """

    def setUp(self):
        """Simula o banco indisponível em todas as chamadas do controller."""
        patcher = mock.patch.object(
            ClienteController, "criar_conexao", return_value=None)
        self.conexao_falsa = patcher.start()
        self.addCleanup(patcher.stop)

    def teste_inserir_cliente_devolve_false_sem_quebrar(self):
        self.assertFalse(ClienteController.inserir_cliente("Fulano", 30, "Outro"))

    def teste_selecionar_todos_devolve_lista_vazia_sem_quebrar(self):
        self.assertEqual(ClienteController.SelecionarTodos(), [])

    def teste_excluir_cliente_devolve_false_sem_quebrar(self):
        self.assertFalse(ClienteController.excluir_cliente(1))

    def teste_selecionar_por_id_devolve_none_sem_quebrar(self):
        self.assertIsNone(ClienteController.SelecionarPorID(1))

    def teste_atualizar_devolve_false_sem_quebrar(self):
        self.assertFalse(ClienteController.Atualizar(1, "Fulano", 30, "Outro"))


if __name__ == "__main__":
    unittest.main()
