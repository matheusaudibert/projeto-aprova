import streamlit as st
from renders import inicio, resumos, exercicios, simulados, redacoes, livros, vestibulares, correcao, sidebar

st.set_page_config(
    page_title="Plataforma Aprova",
    page_icon="assets/logo.png",
    layout="centered",
)

tab_inicio, tab_vestibulares, tab_resumos, tab_exercicios, tab_simulados, tab_redacoes, tab_correcao, tab_livros, tab_teste, tab_datas = st.tabs(["Início", "Vestibulares", "Resumos", "Exercícios", "Provas", "Redações", "Correção", "Livros", "Teste", "Datas"])
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
  
with tab_simulados:
  simulados.render()
  
with tab_redacoes:
  redacoes.render()
  
with tab_correcao:
  correcao.render()
  
with tab_livros:
  livros.render()