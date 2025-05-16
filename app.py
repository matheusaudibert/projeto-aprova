import streamlit as st
from renders import inicio, provas, resumos, exercicios, redacoes, livros, vestibulares, correcao, sidebar, datas, canais

st.set_page_config(
    page_title="Plataforma Aprova",
    initial_sidebar_state="expanded",
    page_icon="assets/aprovadinho/aprovadinho_bot_round.png",
    layout="centered",
)
tab_inicio, tab_vestibulares, tab_resumos, tab_exercicios, tab_provas, tab_redacoes, tab_correcao, tab_livros, tab_datas, tab_canais = st.tabs(["Início", "Vestibulares", "Resumos", "Exercícios", "Provas", "Redações", "Correção", "Leituras", "Datas", "Canais"])
with st.sidebar:
  sidebar.render()

with tab_inicio:
  inicio.render()
  
with tab_vestibulares:
  vestibulares.render()
  
with tab_resumos:
  resumos.render()
  
with tab_exercicios:
  exercicios.render()
  
with tab_provas:
  provas.render()
  
with tab_redacoes:
  redacoes.render()
  
with tab_correcao:
  correcao.render()
  
with tab_livros:
  livros.render()
  
with tab_datas:
  datas.render()
  
with tab_canais:
  canais.render()