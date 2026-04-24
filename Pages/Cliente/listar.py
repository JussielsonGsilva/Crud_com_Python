import streamlit as st
import controllers.ClienteController as ClienteController

# ============================================
# Listagem dos clientes
# ============================================


def Listar():
    colms = st.columns((2, 2, 2, 2, 2, 2))
    campos = ["Id", "Nome", "Idade", "Profissão", "Excluir", "Alterar"]
    for col, campo_name in zip(colms, campos):
        col.write(campo_name)

    for item in ClienteController.SelecionarTodos():
        col1, col2, col3, col4, col5, col6 = st.columns((2, 2, 2, 2, 2, 2))
        col1.write(item["id"])
        col2.write(item["nome"])
        col3.write(item["idade"])
        col4.write(item["profissao"])
        button_space_excluir = col5.empty()
        button_space_alterar = col6.empty()
        on_click_excluir = button_space_excluir.button(
            "Excluir", "btnExcluir" + str(item["id"]))
        on_click_alterar = button_space_alterar.button(
            "Alterar", "btnAlterar" + str(item["id"]))

# Vamos criar na pasta controllers a função para excluir o item.
        if on_click_excluir:
            ClienteController.excluir_cliente(item["id"])
            st.rerun()
