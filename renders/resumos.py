import streamlit as st
from core.generate_summary import generate_summary
from core.clear_summary import clear_summary
from constants.subjects import subjects

def render():
    st.markdown("<h1 style='color: #f26679;'>Gerador de Resumos</h1>", unsafe_allow_html=True)


    st.text("Gere resumos diretos ao ponto sobre os temas que mais caem nos vestibulares. Uma forma rápida e eficiente de revisar os conteúdos mais importantes para os exames.")

    st.divider()

    materias = subjects
    area = st.selectbox("Selecione a área:", [""] + list(materias.keys()), key="resumo_area")

    if area:
        if isinstance(materias[area], dict):
            materia = st.selectbox("Selecione a matéria:", [""] + list(materias[area].keys()), key="resumo_materia")
            subtopicos = materias[area][materia] if materia else []
        else:
            materia = None
            subtopicos = materias[area]

        if subtopicos:
            if isinstance(subtopicos, dict):
                subtopico_key = st.selectbox("Selecione o subtópico:", [""] + list(subtopicos.keys()), key="resumo_subtopico")
                topico = st.selectbox("Selecione o tema:", [""] + subtopicos[subtopico_key], key="resumo_topico") if subtopico_key else ""
            else:
                topico = st.selectbox("Selecione o tópico específico:", [""] + subtopicos, key="resumo_topico")
        else:
            topico = ""

        if area and (materia or not isinstance(materias[area], dict)) and topico:
            if st.button("Gerar Resumo", type="primary"):
                with st.spinner("Gerando resumo..."):
                    subject = f"{topico} - {materia if materia else area}"
                    resumo = generate_summary(subject)

                    with st.container(border=True):
                        st.markdown(resumo)

                    arquivo_nome = f"resumo_{subject.replace(' ', '_').replace('/', '_')}.txt"
                    texto_limpo = clear_summary(resumo)

                    st.download_button(
                        label="Baixar Resumo",
                        data=texto_limpo,
                        file_name=arquivo_nome,
                        mime="text/plain",
                        type="secondary",
                        use_container_width=True,
                    )
    else:
        st.info("Selecione uma área para começar.")
