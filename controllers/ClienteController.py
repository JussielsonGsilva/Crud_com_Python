from services.database import criar_conexao, fechar_conexao
import streamlit as st
import time


def inserir_cliente(nome, idade, profissao):
    con = criar_conexao()

    if con is None:
        st.error("Erro: não foi possível conectar ao banco de dados.")
        return False

    try:
        cursor = con.cursor(buffered=True)

        sql_verificar = "SELECT id FROM Cliente WHERE cliNome = %s"
        cursor.execute(sql_verificar, (nome,))
        resultado = cursor.fetchone()

        if resultado:
            msg = st.warning("Cliente já está cadastrado.")
            time.sleep(2)
            msg.empty()
            return False  # ✔️ Apenas retorna

        sql_inserir = """
            INSERT INTO Cliente (cliNome, cliIdade, cliProfissao)
            VALUES (%s, %s, %s)
        """
        valores = (nome, idade, profissao)

        cursor.execute(sql_inserir, valores)
        con.commit()

        return True

    except Exception as e:
        st.error(f"Erro ao inserir cliente: {e}")
        return False

    finally:
        cursor.close()
        fechar_conexao(con)


def SelecionarTodos():
    con = criar_conexao()

    if con is None:
        st.error("Erro: não foi possível conectar ao banco de dados.")
        return []

    try:
        cursor = con.cursor(buffered=True)

        sql_selecionar = """
            SELECT id, cliNome, cliIdade, cliProfissao 
            FROM Cliente
            ORDER BY cliNome ASC
        """
        cursor.execute(sql_selecionar)
        resultados = cursor.fetchall()
        costumerList = []

        for row in resultados:
            costumerList.append({
                "id": row[0],
                "nome": row[1],
                "idade": row[2],
                "profissao": row[3]
            })

        return costumerList

    except Exception as e:
        st.error(f"Erro ao selecionar clientes: {e}")
        return []

    finally:
        cursor.close()
        fechar_conexao(con)


def excluir_cliente(id):
    """
    Remove um cliente pelo seu identificador.

    @param id  Identificador do cliente a ser removido
    @return    True se removeu, False se o banco estiver indisponível ou houver erro
    """
    con = criar_conexao()

    if con is None:
        st.error("Erro: não foi possível conectar ao banco de dados.")
        return False

    cursor = None
    try:
        cursor = con.cursor()

        sql_excluir = "DELETE FROM Cliente WHERE id = %s"
        cursor.execute(sql_excluir, (id,))
        con.commit()

        return True

    except Exception as erro:
        st.error(f"Erro ao excluir cliente: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        fechar_conexao(con)


def SelecionarPorID(id):
    """
    Busca um cliente pelo seu identificador.

    @param id  Identificador do cliente
    @return    Dicionário com os dados do cliente, ou None se não existir,
               se o banco estiver indisponível ou se houver erro
    """
    con = criar_conexao()

    if con is None:
        st.error("Erro: não foi possível conectar ao banco de dados.")
        return None

    cursor = None
    try:
        cursor = con.cursor()

        cursor.execute(
            "SELECT id, cliNome, cliIdade, cliProfissao FROM Cliente WHERE id = %s", (id,))
        row = cursor.fetchone()

        if row:
            return {
                "id": row[0],
                "nome": row[1],
                "idade": row[2],
                "profissao": row[3]
            }

        return None

    except Exception as erro:
        st.error(f"Erro ao buscar cliente: {erro}")
        return None

    finally:
        if cursor:
            cursor.close()
        fechar_conexao(con)


def Atualizar(id, nome, idade, profissao):
    """
    Atualiza os dados de um cliente já cadastrado.

    @param id         Identificador do cliente
    @param nome       Novo nome
    @param idade      Nova idade
    @param profissao  Nova profissão
    @return           True se atualizou, False se o banco estiver
                      indisponível ou houver erro
    """
    con = criar_conexao()

    if con is None:
        st.error("Erro: não foi possível conectar ao banco de dados.")
        return False

    cursor = None
    try:
        cursor = con.cursor()

        sql_alterar = """
            UPDATE Cliente
            SET cliNome = %s, cliIdade = %s, cliProfissao = %s
            WHERE id = %s
        """
        valores = (nome, idade, profissao, id)

        cursor.execute(sql_alterar, valores)
        con.commit()

        return True

    except Exception as erro:
        st.error(f"Erro ao atualizar cliente: {erro}")
        return False

    finally:
        if cursor:
            cursor.close()
        fechar_conexao(con)
