import streamlit as st
from renders import sidebar
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Teste vocacional",
    initial_sidebar_state="expanded",
    page_icon="assets/aprovadinho/aprovadinho_bot_round.png",
    layout="centered",
)

with st.sidebar:
    sidebar.render()

col1, col2 = st.columns([1, 7])
with col2:
    st.markdown("<h1 style='color: #f08671;'>Comece seu Teste Vocacional</h1>", unsafe_allow_html=True)
with col1:
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    if st.button("VoItar", use_container_width=True, key="voltar_button", type="primary"):
        st.switch_page("app.py")
st.text("Responda algumas perguntas rápidas e descubra, com ajuda da IA, qual área combina mais com você e quais cursos são ideais para o seu perfil.")
    

def read_html():
    with open("./core/index.html") as f:
        return f.read()

components.html(
    read_html(),
    height=0,
    width=0,
)
