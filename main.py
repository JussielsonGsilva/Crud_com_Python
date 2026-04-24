import streamlit as st
import pandas as pd
import time
import controllers.ClienteController as ClienteController

# ============================================
# 1️⃣ Inicializa variáveis no session_state
# ============================================
if "input_name" not in st.session_state:
    st.session_state.input_name = ""

if "input_age" not in st.session_state:
    st.session_state.input_age = 0

if "input_occupation" not in st.session_state:
    st.session_state.input_occupation = "Outro"

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False


# ============================================
# 2️⃣ Se o formulário foi enviado, limpar campos
# ============================================
if st.session_state.form_submitted:
    st.session_state.input_name = ""
    st.session_state.input_age = 0
    st.session_state.input_occupation = "Outro"
    st.session_state.form_submitted = False  # reseta a flag


# ============================================
# 3️⃣ Formulário
# ============================================
st.sidebar.title("Menu")
Page_cliente = st.sidebar.selectbox(
    'Cliente', ['Cadastrar', 'Alterar', 'Excluir', 'Consultar'])

if Page_cliente == 'Consultar':
    st.title("Clientes")
    # ============================================
    # Listagem dos clientes
    # ============================================
    constumerList = []

    for item in ClienteController.SelecionarTodos():
        constumerList.append({
            "id": item["id"],
            "nome": item["nome"],
            "idade": item["idade"],
            "profissao": item["profissao"]
        })

    df = pd.DataFrame(constumerList, columns=[
                      "id", "nome", "idade", "profissao"])
    st.table(df)

if Page_cliente == 'Cadastrar':
    st.title("Cadastro de Cliente")
    # ============================================
    # Formulário de cadastro
    # ============================================
    with st.form(key="include_cliente"):
        input_name = st.text_input("Insira o seu nome", key="input_name")
        input_age = st.number_input(
            "Insira a sua idade", min_value=0, max_value=120, format="%d", key="input_age")
        input_occupation = st.selectbox(
            "Selecione sua profissão",
            ["Desenvolvedor", "Engenheiro", "Médico", "Professor", "Outro"],
            key="input_occupation"
        )

        submit_button = st.form_submit_button("Enviar")

    # ============================================
    # 4️⃣ Ação ao enviar
    # ============================================
    if submit_button:

        # 1️⃣ Validação dos campos
        if not input_name.strip():
            msg = st.warning("O nome não pode estar vazio.")
            time.sleep(3)
            msg.empty()
            st.stop()

        if input_age <= 0:
            msg = st.warning("A idade deve ser maior que zero.")
            time.sleep(3)
            msg.empty()
            st.stop()

        # 2️⃣ Se passou na validação, tenta inserir
        if ClienteController.inserir_cliente(input_name, input_age, input_occupation):

            msg = st.success("Cliente Cadastrado com sucesso.")
            time.sleep(3)
            msg.empty()

            st.session_state.form_submitted = True
            st.rerun()
