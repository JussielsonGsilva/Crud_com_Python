# CRUD de Clientes — Python + Streamlit + MySQL

Aplicação web de cadastro de clientes com as quatro operações de um CRUD:
criar, listar, alterar e excluir. Interface em Streamlit, dados em MySQL.

---

## Funcionalidades

- **Cadastrar** cliente (nome, idade e profissão), com validação de campos
  obrigatórios e bloqueio de nome duplicado
- **Listar** todos os clientes em tabela, ordenados por nome
- **Alterar** os dados de um cliente já cadastrado
- **Excluir** um cliente

---

## Hooks do Git

O repositório traz um hook de `pre-commit` em `.githooks/` que aborta o commit se
`.env` ou arquivos de backup (`.bak`, `.old`, `.orig`, `~`) entrarem no stage.

Ative uma vez após clonar:

```bash
git config core.hooksPath .githooks
```

A configuração é local a cada clone — o Git não permite que um repositório ative
hooks sozinho, justamente para que baixar um projeto não execute código na sua
máquina sem você pedir.

O `.gitignore` já evita o acidente comum, mas não protege contra um `git add -f`
distraído. E vale lembrar que ele **não** deixa de rastrear arquivo que já foi
commitado antes de constar na lista: para isso é preciso `git rm --cached`.

---

## Tecnologias

- **Python 3.13**
- **Streamlit** — interface web
- **MySQL** — banco de dados
- **mysql-connector-python** — driver de conexão
- **python-dotenv** — leitura das credenciais a partir do `.env`

---

## Pré-requisitos

- Python 3.10 ou superior
- **MySQL instalado e em execução** (a aplicação não funciona sem ele)
- Um usuário MySQL com permissão sobre o banco do projeto

---

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/JussielsonGsilva/Crud_com_Python.git
cd Crud_com_Python
```

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

```bash
mysql -u root -p < database.sql
```

O script cria o banco `crud_python` e a tabela `Cliente`. Pode ser executado
mais de uma vez sem erro — não apaga dados existentes.

### 5. Configurar as credenciais

```bash
cp .env.example .env
chmod 600 .env
```

Abra o `.env` e preencha com os dados do seu MySQL:

```env
DB_HOST=localhost
DB_NOME=crud_python
DB_USUARIO=seu_usuario_mysql
DB_SENHA=sua_senha_mysql
```

> O `.env` não é versionado. As credenciais nunca ficam no código.

---

## Executando

```bash
streamlit run main.py
```

A aplicação abre em `http://localhost:8501`. Use o menu lateral para
alternar entre **Cadastrar** e **Listar**.

---

## Testes

```bash
python -m unittest discover -s testes -v
```

Os testes verificam que a conexão lê as credenciais do ambiente e que
nenhuma credencial voltou a ser escrita no código.

---

## Estrutura do Projeto

```
.
├── main.py                     # ponto de entrada e menu lateral
├── database.sql                # estrutura do banco de dados
├── requirements.txt            # dependências do projeto
├── .env.example                # modelo de configuração das credenciais
│
├── Pages/
│   └── Cliente/
│       ├── cadastrar.py        # formulário de cadastro e alteração
│       └── listar.py           # tabela de clientes com ações
│
├── controllers/
│   └── ClienteController.py    # operações de banco (insert, select, update, delete)
│
├── services/
│   └── database.py             # conexão com o MySQL
│
└── testes/
    └── teste_database.py       # testes da camada de conexão
```

---

## Licença

Projeto livre para estudo, modificação e evolução.

## Autor

**Jussielson G. Silva** — Analista e Desenvolvedor de Sistemas
