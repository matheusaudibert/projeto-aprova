import streamlit as st
import urllib.parse

# Função para gerar link do Google Agenda
def gerar_link_google_agenda(titulo, descricao, local, data_inicio, data_fim):
    params = {
        'action': 'TEMPLATE',
        'text': titulo,
        'details': descricao,
        'location': local,
        'dates': f'{data_inicio}/{data_fim}'
    }
    base_url = 'https://www.google.com/calendar/render'
    return f"{base_url}?{urllib.parse.urlencode(params)}"

def render():
    st.markdown("<h1 style='color: #b0e1ff ;'>Datas Importantes</h1>", unsafe_allow_html=True)
    st.text("Aqui estão as datas importantes para os vestibulares de 2025 e 2026. Fique atento às datas de inscrição, provas e resultados para não perder nenhuma oportunidade!")
    st.divider()

    # ENEM 2025
    col_title, = st.columns(1)
    with col_title:
        st.subheader(":blue[ENEM 2025]")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("**Inscrição:** 26 de maio a 6 de junho de 2025")
        with st.container(border=True):
            st.markdown("**Resultado final:** ainda será divulgado")
    with col2:
        with st.container(border=True):
             st.markdown("**1º dia de prova:** 9 de novembro de 2025")            
    with col3:
        with st.container(border=True):
            st.markdown("**2º dia de prova:** 16 de novembro de 2025")

    st.write("")
    st.write("")

    # Botões Google Agenda - ENEM
    col1, = st.columns(1)
    with col1:
      st.markdown("#### 📅 Adicionar ao :blue[G]:red[o]:orange[o]:blue[g]:green[l]:red[e] Agenda:")
      
    col1, col2, col3 = st.columns(3)
    with col1:
      st.link_button("Adicionar 1º dia do ENEM (9/11)", gerar_link_google_agenda(
        "ENEM 2025 - 1º dia de prova", "Prova do ENEM 2025 - 1º dia", "Local a definir", "20251109T130000Z", "20251109T180000Z"))
    with col2:
      st.link_button("Adicionar 2º dia do ENEM (16/11)", gerar_link_google_agenda(
        "ENEM 2025 - 2º dia de prova", "Prova do ENEM 2025 - 2º dia", "Local a definir", "20251116T130000Z", "20251116T180000Z"))

    st.divider()

    # FUVEST 2026
    col_title, = st.columns(1)
    with col_title:
        st.subheader(":green[FUVEST 2026]")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("**Inscrição:** 18 de agosto a 7 de outubro de 2025")
        with st.container(border=True):
          st.markdown("**2ª Fase:** 14 e 15 de dezembro de 2025")
    with col2:
        with st.container(border=True):
            st.markdown("**1ª Fase:** 23 de novembro de 2025")
        with st.container(border=True):
            st.markdown("**Resultado:** 23 de janeiro de 2026")            
    with col3:
        with st.container(border=True):
          st.markdown("**Competências Específicas:** 9 a 12 de dezembro de 2025")
            

    st.write("")
    st.write("")

    # Botões Google Agenda - FUVEST
    col1, = st.columns(1)
    with col1:
      st.markdown("#### 📅 Adicionar ao :blue[G]:red[o]:orange[o]:blue[g]:green[l]:red[e] Agenda:")
      
    col1, col2, col3 = st.columns(3)
    with col1:
      st.link_button("Adicionar 1ª Fase FUVEST (23/11)", gerar_link_google_agenda(
        "FUVEST 2026 - 1ª Fase", "Prova da 1ª Fase da FUVEST 2026", "Local a definir", "20251123T120000Z", "20251123T170000Z"))
    with col2:
      st.link_button("Adicionar 2ª Fase FUVEST (14/12)", gerar_link_google_agenda(
        "FUVEST 2026 - 2ª Fase (1º dia)", "Prova da 2ª Fase da FUVEST 2026 - 1º dia", "Local a definir", "20251214T120000Z", "20251214T170000Z"))
    with col3:
      st.link_button("Adicionar 2ª Fase FUVEST (15/12)", gerar_link_google_agenda(
        "FUVEST 2026 - 2ª Fase (2º dia)", "Prova da 2ª Fase da FUVEST 2026 - 2º dia", "Local a definir", "20251215T120000Z", "20251215T170000Z"))

    st.divider()

    # UNICAMP 2026
    col_title, = st.columns(1)
    with col_title:
        st.subheader(":orange[UNICAMP 2026]")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("**Inscrição:** 1 de agosto a 1 de setembro de 2025")
        with st.container(border=True):
            st.markdown("**2ª Fase:** 30 de novembro e 1 de dezembro de 2025")
            
    with col2:
        with st.container(border=True):
            st.markdown("**Habilidades Específicas (Música):** Setembro (data a definir)")
        with st.container(border=True):
            st.markdown("**Habilidades Específicas (outros cursos):** 3 a 5 de dezembro de 2025")
            
    with col3:
        with st.container(border=True):
          st.markdown("**1ª Fase:** 26 de outubro de 2025")
        with st.container(border=True):
          st.markdown("**Resultado:** 23 de janeiro de 2026")
            
            
    st.write("")
    st.write("")
    
    # Botões Google Agenda - UNICAMP
    col1, = st.columns(1)
    with col1:
      st.markdown("#### 📅 Adicionar ao :blue[G]:red[o]:orange[o]:blue[g]:green[l]:red[e] Agenda:")
      
    col1, col2, col3 = st.columns(3)
    with col1:
      st.link_button("Adicionar 1ª Fase UNICAMP (26/10)", gerar_link_google_agenda(
        "UNICAMP 2026 - 1ª Fase", "Prova da 1ª Fase da UNICAMP 2026", "Local a definir", "20251026T120000Z", "20251026T170000Z"))
    with col2:
      st.link_button("Adicionar 2ª Fase UNICAMP (30/11)", gerar_link_google_agenda(
        "UNICAMP 2026 - 2ª Fase (1º dia)", "Prova da 2ª Fase da UNICAMP 2026 - 1º dia", "Local a definir", "20251130T120000Z", "20251130T170000Z"))
    with col3:
      st.link_button("Adicionar 2ª Fase UNICAMP (1/12)", gerar_link_google_agenda(
        "UNICAMP 2026 - 2ª Fase (2º dia)", "Prova da 2ª Fase da UNICAMP 2026 - 2º dia", "Local a definir", "20251201T120000Z", "20251201T170000Z"))
