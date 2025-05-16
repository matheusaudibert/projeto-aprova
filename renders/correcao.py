import os
import tempfile
import streamlit as st
from core.genetare_correction import generate_correction, verificar_sentido_redacao_com_arquivo, formatar_resultado

def render():
    st.markdown("<h1 style='color:  #d39eff;'>Correção de Redação</h1>", unsafe_allow_html=True)
    st.markdown("Escolha se deseja digitar a redação ou enviar um arquivo. Depois, selecione a vestibular, o tema e receba uma correção detalhada.")
    st.markdown("#### Como funciona a correção da redação de cada vestibular?")
    st.markdown("[Correção Enem](https://www.cnnbrasil.com.br/educacao/redacao-do-enem-perguntas-e-respostas-sobre-a-correcao/), [Correção Fuvest (USP)](https://www.cnnbrasil.com.br/educacao/redacao-da-fuvest-2025-saiba-como-e-feita-a-correcao/), [Correção Unicamp](https://querobolsa.com.br/revista/como-e-a-correcao-da-redacao-da-unicamp)", unsafe_allow_html=True)

    st.divider()
    

    modo = st.selectbox("Como você quer enviar sua redação?", ["", "Escrever texto", "Enviar arquivo"])

    texto_redacao = None
    arquivo = None

    if modo == "Escrever texto":
        texto_redacao = st.text_area("Digite sua redação aqui:", height=300)

    elif modo == "Enviar arquivo":
        arquivo = st.file_uploader(
            "Envie sua redação (PDF, imagem, DOCX ou TXT)",
            type=["pdf", "png", "jpg", "jpeg", "webp", "txt", "docx"]
        )

    tema = st.text_input("Qual o tema da redação?")
    
    vestibular = st.selectbox("Selecione a o vestibular para correção:", ["", "ENEM", "Fuvest", "Unicamp"])
    

    if st.button("Corrigir redação", type="primary"):
        if not vestibular:
            st.warning("Selecione o vestibular.")
        elif not tema:
            st.warning("Informe o tema da redação.")
        elif modo == "Escrever texto" and not texto_redacao:
            st.warning("Digite sua redação.")
        elif modo == "Enviar arquivo" and not arquivo:
            st.warning("Envie um arquivo.")
        else:
            with st.spinner("Verificando redação..."):
                if modo == "Escrever texto":
                    if len(texto_redacao.strip()) < 1000:
                        st.error("Por favor, envie uma redação com pelo menos 1000 caracteres.")
                        return

                    resultado = generate_correction(texto_redacao, vestibular=vestibular, tema=tema)

                else:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(arquivo.name)[1]) as tmp_file:
                        tmp_file.write(arquivo.getbuffer())
                        temp_path = tmp_file.name

                    try:
                        if not verificar_sentido_redacao_com_arquivo(temp_path, tema):
                            st.error("O conteúdo do arquivo enviado não parece ser uma redação válida sobre o tema proposto.")
                            return

                        resultado = generate_correction(temp_path, vestibular=vestibular, tema=tema)

                    finally:
                        if os.path.exists(temp_path):
                            os.unlink(temp_path)
                formatar_resultado(resultado, vestibular)

