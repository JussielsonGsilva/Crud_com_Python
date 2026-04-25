import streamlit as st
import pandas as pd
import time
import controllers.ClienteController as ClienteController
import Pages.Cliente.cadastrar as PageCadastrarCliente
import Pages.Cliente.listar as PageListarCliente

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


st.sidebar.title("Menu")
Page_cliente = st.sidebar.selectbox(
    'Cliente', ['Cadastrar', 'Listar'])

if Page_cliente == 'Listar':
    PageListarCliente.Listar()

if Page_cliente == 'Cadastrar':
    PageCadastrarCliente.Cadastrar()
