# 🏢 Sistema de Análise de Imóveis (Full-Stack Integrado)

Bem-vindo ao repositório do Projeto de Análise de Imóveis! Esta é uma aplicação educacional Full-Stack projetada para estruturar, validar, persistir e exibir dados de forma dinâmica e moderna usando uma arquitetura baseada em microsserviços.

## 🚀 Tecnologias Utilizadas
- **Backend (API):** Python 3, `FastAPI`, `Uvicorn`, `Pydantic`
- **Banco de Dados Relacional:** `SQLAlchemy` e `MySQL` (local) / `PostgreSQL` (na nuvem via Render.com)
- **Frontend / Visualização:** `Streamlit`, `Pandas`
- **Extração de Dados:** `Cloudscraper` (Simulação de coleta) e `Requests`

## ⚙️ Arquitetura
A aplicação é dividida em dois vetores independentes:
1. **Motor API (Cérebro):** Fica responsável por validar se um imóvel cadastrado possui preço em números válidos (Pydantic), atrela os imóveis à Imobiliária e Tipos baseados nas *Foreign Keys* para manter a integridade, e processa Requests (RestAPI).
2. **Dashboard Visual (Streamlit):** Uma aplicação Web totalmente independente (cego ao banco) que consome os dados da API local ou em nuvem para orquestrar gráficos instantâneos através do Pandas.

---

## 🛠️ Como rodar o projeto localmente

Para rodar este projeto na sua máquina, você vai precisar de ter o **Python** e um banco **MySQL** (ex: XAMPP, WAMP) instalados.

### 1. Clonando o Repositório
```bash
git clone https://github.com/nandamundim10/Projeto_DFimoveis.git
cd Projeto_DFimoveis
```

### 2. Instalando Dependências
Criamos um arquivo de dependências padronizado para baixar tudo de uma só vez:
```bash
pip install -r requirements.txt
```

### 3. Configurando o Banco de Dados
Por padrão, o arquivo `main.py` utiliza a biblioteca `os.getenv` para tentar ler variáveis secretas do sistema (se em Nuvem) ou cai para a senha `Lilika10#` base do localhost MySQL. Crie um banco local chamado `dfimoveis_db` para que a conexão SQLAlchemy consiga construir as tabelas automaticamente.

### 4. Rodando o Backend (API)
Inicie o motor do sistema executando o arquivo principal FastAPI:
```bash
uvicorn main:app --reload
```
A API ficará disponível em `http://localhost:8000`. Você pode ver toda a documentação das rotas abrindo e testando os endpoints no link manual em `/docs`.

### 5. Rodando o Frontend (Streamlit)
Deixe o terminal da API em execução e abra um **novo terminal** para rodar a ponta visual:
```bash
streamlit run dashboard.py
```
Uma janela gráfica preta e moderna aparecerá listando os dados cadastrados assim que abrir no seu navegador!

### 6. Como inserir Imóveis de Teste?
A sua tela de gráficos começará vazia! Para injetar imóveis:
1. Abra o arquivo **`postman_collection.json`** e importe ele para dentro do programa *Postman*, e execute testes de envios;
2. OU use nossa rota de automação escrevendo no backend e ativando robôs extraídos da internet. 

---
### 🌐 Deploy Real
Este projeto está modularizado e apto a rodar na infraestrutura "Web Services" do **Render.com**, criando **dois hosts separados na nuvem** (Back vs Front) dialogando entre as redes através da injeção das variáveis de ambiente:
- `DATABASE_URL` (Sua url secreta do PostgreSQL fornecida pela nuvem) 
- `API_URL` (Sua url onde depositou a API).
