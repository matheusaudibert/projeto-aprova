import streamlit as st
from renders import inicio, provas, resumos, exercicios, redacoes, livros, vestibulares, correcao, datas, canais

st.set_page_config(
    page_title="Prataforma Aprova",
    initial_sidebar_state="expanded",
    page_icon="🎓",
    layout="centered",
)
def render():
  
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
        
        .st-emotion-cache-1gczx66.edtmxes2 {
            display: none;
        }
        
        .st-emotion-cache-1s1exd7.edtmxes19 {
            display: none;
        }
        
        .st-emotion-cache-1gczx66.edtmxes2 {
            display: none;
        }
        .st-emotion-cache-1s1exd7.edtmxes19 {
            display: none;
        }

        .st-emotion-cache-1s1exd7.edtmxes19 {
            display: none;
        }
        
        .st-emotion-cache-1gczx66.edtmxes2 {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)
  
with st.sidebar:
    st.markdown("**Tema: Dracula 🧛‍♀️**")
    st.markdown("# 🎓 Aprova")  
    st.markdown("*Este projeto foi desenvolvido durante a **Imersão IA** da **:blue[Alura]** em parceria com o **:blue[G]:red[o]:orange[o]:blue[g]:green[l]:red[e] :violet[Gemini]***.")
  
    st.markdown("# 🎈 Extras") 
    st.text("Conheça o Aprovadinho, o chatbot da plataforma, e tire suas dúvidas sobre os principais vestibulares do Brasil.")
    if st.button("Aprovadinho", use_container_width=True, key="aprovadinho_sidebar_button"):
        st.switch_page("pages/aprovadinho.py")
        
    st.write("")
        
    st.text("Faça o teste vocacional agora e descubra qual carreira combina mais com você.")
    if st.button("Teste vocacional", use_container_width=True, key="teste_sidebar_button"):
        st.switch_page("pages/teste.py")
        
    st.write("")
    st.markdown("😼 GitHub do projeto [aqui](https://github.com/matheusaudibert/projeto-aprova)!")


tab_inicio, tab_vestibulares, tab_resumos, tab_exercicios, tab_provas, tab_redacoes, tab_correcao, tab_livros, tab_datas, tab_canais = st.tabs(["Início", "Vestibulares", "Resumos", "Exercícios", "Provas", "Redações", "Correção", "Leituras Obrigatórias", "Datas", "Canais"])

with tab_inicio:
  inicio.render()
  
with tab_vestibulares:
  vestibulares.render()
  
with tab_resumos:
  resumos.render()
  
with tab_exercicios:
  exercicios.render()
  
with tab_provas:
  provas.render()
  
with tab_redacoes:
  redacoes.render()
  
with tab_correcao:
  correcao.render()
  
with tab_livros:
  livros.render()
  
with tab_datas:
  datas.render()
  
with tab_canais:
  canais.render()
  
with st.sidebar:
  render()
  
  