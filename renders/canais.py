import streamlit as st
from constants.channels import channels_geral

def mostrar_canais(canal1, canal2):
    col1, col2, col3, col4 = st.columns([1,1.3,1,1.3])
    with col1:
        st.image(channels_geral[canal1]["Imagem"], width=500)
    with col2:
        st.markdown(channels_geral[canal1]["Nome"])
        st.caption(channels_geral[canal1]["Descrição"])
    with col3:
        st.image(channels_geral[canal2]["Imagem"], width=500)
    with col4:
        st.markdown(channels_geral[canal2]["Nome"])
        st.caption(channels_geral[canal2]["Descrição"])

def render():
    st.markdown("<h1 style='color: #fc5353;'>Canais do YouTube</h1>", unsafe_allow_html=True)
    st.text("Encontre alguns canais do YouTube com conteúdos de qualidade para auxiliar nos estudos para vestibulares.")
    st.divider()

    canais = list(channels_geral.keys())
    canais_pares = [(canais[i], canais[i+1]) for i in range(0, len(canais), 2)]
    
    for canal1, canal2 in canais_pares:
        with st.container(border=True):
            mostrar_canais(canal1, canal2)


