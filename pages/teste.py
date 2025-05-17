import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Teste Vocacional",
    initial_sidebar_state="expanded",
    page_icon="🧠",
    layout="centered",
)

with st.sidebar:
    
    st.markdown("""
    <style>
        .st-emotion-cache-j7qwjs.e1c29vlm3 {
            display: none;
        }
        
        .st-emotion-cache-vz9k5h.e1c29vlm19 {
            display: none;
        }
        
        .st-emotion-cache-1s1exd7.e1c29vlm19 {
            display: none;
        }
        
        .st-emotion-cache-14lrqrc.e1c29vlm19 {
            display: none;
        }
        
        .st-emotion-cache-1tuwfdi.e1c29vlm19 {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
    
    st.markdown("# 🎓 Aprova")  
    st.markdown("*Este projeto foi desenvolvido durante a **Imersão IA** da **:blue[Alura]** em parceria com o **:blue[G]:red[o]:orange[o]:blue[g]:green[l]:red[e] :violet[Gemini]***.")
  
    st.markdown("# 🎈 Extras") 
    st.text("Conheça o Aprovadinho, o chatbot da plataforma, e tire suas dúvidas sobre os principais vestibulares do Brasil.")
    if st.button("Aprovadinho", use_container_width=True, key="aprovadinho_sidebar_1_button"):
        st.switch_page("pages/aprovadinho.py")
        
    st.write("")
        
    st.text("Faça o teste vocacional agora e descubra qual carreira combina mais com você.")
    if st.button("Teste vocacional", use_container_width=True, key="teste_sidebar_1_button"):
        st.switch_page("pages/teste.py")
        
    st.write("")
    st.markdown("😼 GitHub do projeto [aqui](https://github.com/matheusaudibert/projeto-aprova)!")

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
