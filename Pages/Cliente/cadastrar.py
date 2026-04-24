import streamlit as st
import time
import controllers.ClienteController as ClienteController

# ============================================
# Formulário de cadastro
# ============================================


def Cadastrar():
    st.title("Cadastro de Cliente")
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
