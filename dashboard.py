import os
import streamlit as st
import requests
import pandas as pd


st.title("Sistema de Análise de Imóveis - DF")

API_URL = os.getenv("API_URL", "http://localhost:8000")

try:
    response = requests.get(f"{API_URL}/imoveis", timeout=5)
    dados = response.json()

    if dados:
        df = pd.DataFrame(dados)

        st.write("### Lista de Imóveis Cadastrados")
        st.dataframe(df)

        st.write("### Comparativo de Preços")
        st.bar_chart(data=df, x="endereco", y="preco")

    else:
        st.info("Nenhum imóvel encontrado. Cadastre um no Postman!")
        
except Exception as e:
    st.error(f"Erro ao conectar com a API: {e}")