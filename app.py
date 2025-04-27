import streamlit as st
import httpx


st.set_page_config(page_title="Vamos Conversar", page_icon="🤖")

st.title("💬 Chat com Gemini")
pergunta = st.text_input("Faça uma pergunta:")

if st.button("Enviar"):
    if pergunta:
        with st.spinner("Consultando IA..."):
            # Aqui você chama o seu próprio FastAPI local
            response = httpx.post("http://127.0.0.1:8000/chat", json={"pergunta": pergunta})

            if response.status_code == 200:
                resposta = response.json()["resposta"]
                st.success(resposta)
            else:
                st.error("Erro ao se comunicar com o servidor FastAPI.")