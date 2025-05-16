import streamlit as st
def render():
  st.title("Datas dos Vestibulares 2025/2026")
  st.text("Aqui estão as datas importantes para os vestibulares de 2025 e 2026. Fique atento às datas de inscrição, provas e resultados para não perder nenhuma oportunidade!")
  st.divider()
  
  col1, col2, col3 = st.columns(3)

  with col1:
      st.subheader("ENEM 2025")
      st.markdown("""
      - **Inscrição:** 26 de maio a 6 de junho de 2025  
      - **Provas:** 9 e 16 de novembro de 2025  
      - **Isenção/Justificativa:** Resultado: 12 de maio de 2025  
      - **Recursos (Isenção):** 22 de maio de 2025  
      - **Resultado final:** Ainda será divulgado  
      """)

  with col2:
      st.subheader("FUVEST 2026")
      st.markdown("""
      - **Inscrição:** 18 de agosto a 7 de outubro de 2025  
      - **1ª Fase:** 23 de novembro de 2025  
      - **2ª Fase:** 14 e 15 de dezembro de 2025  
      - **Comp. Específicas:** 9 a 12 de dezembro de 2025  
      - **Resultado:** 23 de janeiro de 2026  
      """)

  with col3:
      st.subheader("UNICAMP 2026")
      st.markdown("""
      - **Isenção:** 12 de maio a 6 de junho de 2025  
      - **Inscrição:** 1º de agosto a 1º de setembro de 2025  
      - **Hab. Específicas (Música):** Setembro (data a definir)  
      - **1ª Fase:** 26 de outubro de 2025  
      - **2ª Fase:** 30 de nov. e 1º de dez. de 2025  
      - **Hab. Específicas (demais):** 3 a 5 de dezembro de 2025  
      - **Resultado:** 23 de janeiro de 2026  
      """)
