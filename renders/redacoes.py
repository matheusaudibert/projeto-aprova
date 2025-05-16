import streamlit as st
import webbrowser
from constants.texts import redacoes_enem, redacoes_fuvest, redacoes_unicamp

def render():
    st.markdown("<h1 style='color: #FFB530;'>Redações Nota Máxima</h1>", unsafe_allow_html=True)
    st.text("Aqui você encontra redações que tiraram nota máxima nos principais vestibulares. Leia, analise e inspire-se com exemplos reais para aprimorar sua escrita e se preparar melhor para a prova.")
    st.divider()

    vestibular = st.selectbox("Escolha o vestibular:", ["", "ENEM", "FUVEST", "UNICAMP"], index=0)

    if vestibular == "":
        st.info("Selecione um vestibular para ver as redações.")
        return  # ou apenas não mostrar nada
    elif vestibular == "ENEM":
        redacoes = redacoes_enem
    elif vestibular == "FUVEST":
        redacoes = redacoes_fuvest
    else:
        redacoes = redacoes_unicamp

    for ano in sorted(redacoes.keys(), reverse=True):
      with st.container(border=True):
        dados = redacoes[ano]
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image(dados["image"], width=300)
        with col2:
            st.markdown(f"**{ano}**")
            st.markdown(f"**Tema:** {dados['tema']}")
            if st.button(f"Ler online", key=f"ler_redacao_{ano}", use_container_width=True, type="primary"):
                webbrowser.open(dados["link"])
