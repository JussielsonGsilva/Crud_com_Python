import streamlit as st
import time
import controllers.ClienteController as ClienteController


def Cadastrar():
    params = st.query_params
    idAlteracao = params.get("id")
    ClienteRecuperado = None

    # Verifica se é alteração ou cadastro
    if idAlteracao is not None:
        idAlteracao = int(idAlteracao)
        ClienteRecuperado = ClienteController.SelecionarPorID(idAlteracao)
        st.title("Alterar dados do cliente")
        botao_texto = "Salvar alterações"
    else:
        st.title("Cadastro de Cliente")
        botao_texto = "Cadastrar"

    # Garante que a chave do formulário exista
    if "form_key" not in st.session_state:
        st.session_state.form_key = "form1"

    # Formulário
    with st.form(key=st.session_state.form_key):
        if ClienteRecuperado:
            # Modo alteração: carrega valores do banco
            input_name = st.text_input(
                "Insira o seu nome",
                value=ClienteRecuperado["nome"]
            )
            input_age = st.number_input(
                "Insira a sua idade",
                min_value=0,
                max_value=120,
                format="%d",
                value=ClienteRecuperado["idade"]
            )
            input_occupation = st.selectbox(
                "Selecione sua profissão",
                ["Desenvolvedor(a)", "Engenheiro(a)", "Médico(a)",
                 "Professor(a)", "Outro"],
                index=["Desenvolvedor(a)", "Engenheiro(a)", "Médico(a)",
                       "Professor(a)", "Outro"].index(ClienteRecuperado["profissao"])
            )
        else:
            # Modo cadastro: campos vazios
            input_name = st.text_input("Insira o seu nome", key="input_name")
            input_age = st.number_input(
                "Insira a sua idade",
                min_value=0,
                max_value=120,
                format="%d",
                key="input_age"
            )
            input_occupation = st.selectbox(
                "Selecione sua profissão",
                ["Desenvolvedor(a)", "Engenheiro(a)", "Médico(a)",
                 "Professor(a)", "Outro"],
                key="input_occupation"
            )

        submit_button = st.form_submit_button(botao_texto)

    # Ação ao enviar
    if submit_button:

        # Validações
        if not input_name.strip() or input_age <= 0 or not input_occupation:
            msg = st.warning("Preencha todos os campos do formulário.")
            time.sleep(2)
            msg.empty()
            st.stop()

        if input_age <= 0:
            msg = st.warning("A idade deve ser maior que zero.")
            time.sleep(2)
            msg.empty()
            st.stop()

        # Inserir ou atualizar
        if ClienteRecuperado:
            ClienteController.Atualizar(
                idAlteracao, input_name, input_age, input_occupation
            )
            msg = st.success("Cliente atualizado com sucesso.")
        else:
            resultado = ClienteController.inserir_cliente(
                input_name, input_age, input_occupation
            )

            # 🔥 Se o cliente já existe, limpar formulário e recarregar
            if not resultado:

                # Limpar campos
                for key in ["input_name", "input_age", "input_occupation"]:
                    if key in st.session_state:
                        del st.session_state[key]

                # Forçar recriação do formulário
                st.session_state.form_key = f"form{time.time()}"

                st.rerun()

            # Cadastro bem-sucedido
            msg = st.success("Cliente cadastrado com sucesso.")

            # Limpar campos após cadastro
            for key in ["input_name", "input_age", "input_occupation"]:
                if key in st.session_state:
                    del st.session_state[key]

            # Forçar recriação do formulário
            st.session_state.form_key = f"form{time.time()}"

        time.sleep(2)
        msg.empty()

        # Limpa parâmetros da URL e recarrega
        st.query_params.clear()
        st.rerun()
