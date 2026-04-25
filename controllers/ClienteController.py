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
            time.sleep(3)
            msg.empty()
            return False

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
    con = criar_conexao()
    cursor = con.cursor()

    sql_excluir = "DELETE FROM Cliente WHERE id = %s"
    cursor.execute(sql_excluir, (id,))

    con.commit()
    cursor.close()
    fechar_conexao(con)

    return True


def SelecionarPorID(id):
    con = criar_conexao()
    cursor = con.cursor()

    cursor.execute(
        "SELECT id, cliNome, cliIdade, cliProfissao FROM Cliente WHERE id = %s", (id,))
    row = cursor.fetchone()

    cursor.close()
    fechar_conexao(con)

    if row:
        return {
            "id": row[0],
            "nome": row[1],
            "idade": row[2],
            "profissao": row[3]
        }
    else:
        return None


def Atualizar(id, nome, idade, profissao):
    con = criar_conexao()
    cursor = con.cursor()

    sql_alterar = """
        UPDATE Cliente 
        SET cliNome = %s, cliIdade = %s, cliProfissao = %s
        WHERE id = %s
    """
    valores = (nome, idade, profissao, id)

    cursor.execute(sql_alterar, valores)
    con.commit()
    cursor.close()
    fechar_conexao(con)

    return True
