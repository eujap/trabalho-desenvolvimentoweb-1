import streamlit as st
import httpx


st.set_page_config(page_title="Vamos Conversar", page_icon="🤖")

st.title("💬 Chat com Gemini")
pergunta = st.text_input("Faça uma pergunta:")

if st.button("Enviar"):
    if pergunta:
        with st.spinner("Consultando IA..."):
            try:
                response = httpx.post("http://127.0.0.1:8000/chat/", json={"pergunta": pergunta})
                response.raise_for_status()
                resposta = response.json()["resposta"]
                st.success(resposta)
            except httpx.HTTPStatusError as e:
                st.error(f"Erro HTTP: {e.response.status_code} - {e.response.text}")
            except Exception as e:
                st.error(f"Erro geral: {str(e)}")