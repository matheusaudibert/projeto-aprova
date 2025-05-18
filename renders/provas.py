import streamlit as st
import webbrowser
from constants.tests import enem_tests, fuvest_tests, unicamp_tests

def display_button_pair(prova_url, resolucao_url, prefix, key_suffix):
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"Prova {prefix}", key=f"{key_suffix}_prova", use_container_width=True, type="primary"):
            webbrowser.open(prova_url)
    with col2:
        if st.button(f"Resolução {prefix}", key=f"{key_suffix}_resolucao", use_container_width=True, type="secondary"):
            webbrowser.open(resolucao_url)

def render_enem(ano, data):
    with st.expander(f"ENEM {ano}", expanded=False):
        for dia in ["Dia 1", "Dia 2"]:
            st.markdown(f"### {dia}")
            display_button_pair(
                data[dia]["Prova"],
                data[dia]["Gabarito"],
                dia,
                f"enem_{ano}_{dia.lower()}"
            )

def render_fuvest(ano, data):
    with st.expander(f"Fuvest {ano}", expanded=False):
        st.markdown("### Primeira Fase")
        display_button_pair(
            data["Primeira Fase"]["Prova"],
            data["Primeira Fase"]["Gabarito"],
            "Primeira Fase",
            f"fuvest_{ano}_primeira"
        )
        
        st.markdown("### Segunda Fase")
        fase2 = data["Segunda Fase"]
        for dia in ["Dia 1", "Dia 2"]:
            display_button_pair(
                fase2[dia]["Prova"],
                fase2[dia]["Gabarito"],
                dia,
                f"fuvest_{ano}_segunda_{dia.lower()}"
            )

def render_unicamp(ano, data):
    with st.expander(f"Unicamp {ano}", expanded=False):
        st.markdown("### Primeira Fase")
        display_button_pair(
            data["Primeira Fase"]["Prova"],
            data["Primeira Fase"]["Gabarito"],
            "Primeira Fase",
            f"unicamp_{ano}_primeira"
        )
        
        fase2 = data["Segunda Fase"]
        st.markdown("### Segunda Fase - Dia 1")
        display_button_pair(
            fase2["Dia 1"]["Prova"],
            fase2["Dia 1"]["Gabarito"],
            "Dia 1",
            f"unicamp_{ano}_segunda_dia1"
        )
        
        st.markdown("### Segunda Fase - Dia 2")
        for area in ["Biológicas", "Exatas", "Humanas"]:
            display_button_pair(
                fase2["Dia 2"][area]["Prova"],
                fase2["Dia 2"][area]["Gabarito"],
                area,
                f"unicamp_{ano}_{area.lower()}"
            )

def render():
    st.markdown("<h1 style='color: #F697DB;'>Provas Anteriores</h1>", unsafe_allow_html=True)
    st.text("Acesse provas antigas dos principais vestibulares para praticar, entender o estilo das questões e reforçar seus estudos com base em exames reais.")
    st.divider()
    
    vestibular = st.selectbox(
        "Escolha o vestibular:",
        ("", "ENEM", "Fuvest (USP)", "Unicamp")
    )
    
    if vestibular == "":
        st.info("Selecione um vestibular para começar.")
        return
        
    render_functions = {
        "ENEM": (enem_tests, render_enem),
        "Fuvest (USP)": (fuvest_tests, render_fuvest),
        "Unicamp": (unicamp_tests, render_unicamp)
    }
    
    tests, render_func = render_functions[vestibular]
    for ano in sorted(tests.keys(), reverse=True):
        render_func(ano, tests[ano])
