import streamlit as st
import webbrowser
from constants.tests import enem_tests, fuvest_tests, unicamp_tests

def render():
  st.markdown("<h1 style='color: #F697DB;'>Provas Anteriores</h1>", unsafe_allow_html=True)
  
  st.text("Aqui você pode acessar provas antigas dos principais vestibulares. Use esse material para praticar, entender o estilo das questões e reforçar seus estudos com base em exames reais.")
  st.divider()
  
  enem = enem_tests
  fuvest = fuvest_tests 
  unicamp = unicamp_tests
  
  option = st.selectbox(
    "Escolha o tipo de simulado:",
    ("","ENEM", "Fuvest (USP)", "Unicamp")
  )
  
  if option == "":
    st.info("Selecione um vesibular para começar.")
    
  # Exibição condicional para ENEM
  if option == "ENEM":
    for ano in sorted(enem.keys(), reverse=True):
      with st.expander(f"ENEM {ano}", expanded=False):
              for dia in ["Dia 1", "Dia 2"]:
                  prova = enem[ano][dia]["Prova"]
                  gabarito = enem[ano][dia]["Gabarito"]
                  st.markdown(f"### {dia}")
                  col1, col2 = st.columns(2)
                  with col1:
                      if st.button(f"📄 Prova {dia}", key=f"{ano}_{dia}_prova", use_container_width=True, type="primary"):
                          webbrowser.open(prova)
                  with col2:
                      if st.button(f"✅ Gabarito {dia}", key=f"{ano}_{dia}_gabarito", use_container_width=True, type="secondary"):
                          webbrowser.open(gabarito)

  # Exibição condicional para Fuvest
  elif option == "Fuvest (USP)":
    for ano in sorted(fuvest.keys(), reverse=True):
          with st.expander(f"Fuvest {ano}", expanded=False):
              fase1 = fuvest[ano]["Primeira Fase"]
              fase2 = fuvest[ano]["Segunda Fase"]

              st.markdown("### Primeira Fase")
              col1, col2 = st.columns(2)
              with col1:
                  if st.button("📄 Prova - Primeira Fase", key=f"{ano}_primeira_prova", use_container_width=True, type="primary"):
                      webbrowser.open(fase1["Prova"])
              with col2:
                  if st.button("✅ Gabarito - Primeira Fase", key=f"{ano}_primeira_gabarito", use_container_width=True, type="secondary"):
                      webbrowser.open(fase1["Gabarito"])

              st.markdown("### Segunda Fase")
              col1, col2 = st.columns(2)
              with col1:
                  if st.button("📄 Dia 1 - Segunda Fase", key=f"{ano}_segunda_dia1", use_container_width=True, type="primary"):
                      webbrowser.open(fase2["Dia 1"])
              with col2:
                  if st.button("📄 Dia 2 - Segunda Fase", key=f"{ano}_segunda_dia2", use_container_width=True, type="primary"):
                      webbrowser.open(fase2["Dia 2"])

              col = st.columns(1)[0]
              with col:
                  if st.button("✅ Gabarito - Segunda Fase", key=f"{ano}_segunda_gabarito", use_container_width=True, type="secondary"):
                      webbrowser.open(fase2["Gabarito"])

    # Exibição condicional para Unicamp
  elif option == "Unicamp":
      for ano in sorted(unicamp_tests.keys(), reverse=True):
          with st.expander(f"Unicamp {ano}", expanded=False):
              fase1 = unicamp_tests[ano]["Primeira Fase"]
              fase2 = unicamp_tests[ano]["Segunda Fase"]

              st.markdown("### Primeira Fase")
              col1, col2 = st.columns(2)
              with col1:
                  if st.button("📄 Prova - Primeira Fase", key=f"{ano}_unicamp_primeira_prova", use_container_width=True, type="primary"):
                      webbrowser.open(fase1["Prova"])
              with col2:
                  if st.button("✅ Gabarito - Primeira Fase", key=f"{ano}_unicamp_primeira_gabarito", use_container_width=True, type="secondary"):
                      webbrowser.open(fase1["Gabarito"])

              st.markdown("### Segunda Fase - Dia 1")
              col1, col2 = st.columns(2)
              with col1:
                  if st.button("📄 Prova - Dia 1", key=f"{ano}_unicamp_segunda_dia1_prova", use_container_width=True, type="primary"):
                      webbrowser.open(fase2["Dia 1"]["Prova"])
              with col2:
                  if st.button("✅ Gabarito - Dia 1", key=f"{ano}_unicamp_segunda_dia1_gabarito", use_container_width=True, type="secondary"):
                      webbrowser.open(fase2["Dia 1"]["Gabarito"])

              st.markdown("### Segunda Fase - Dia 2")
              for area in ["Biológicas", "Exatas", "Humanas"]:
                  col1, col2 = st.columns(2)
                  with col1:
                      if st.button(f"📄 Prova - {area}", key=f"{ano}_unicamp_{area}_prova", use_container_width=True, type="primary"):
                          webbrowser.open(fase2["Dia 2"][area]["Prova"])
                  with col2:
                      if st.button(f"✅ Gabarito - {area}", key=f"{ano}_unicamp_{area}_gabarito", use_container_width=True, type="secondary"):
                          webbrowser.open(fase2["Dia 2"][area]["Gabarito"])
