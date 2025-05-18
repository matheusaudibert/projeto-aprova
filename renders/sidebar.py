import streamlit as st

def render():
  
  st.markdown("""
    <style>
        .st-emotion-cache-j7qwjs.e1c29vlm3 {
            display: none;
        }
        
        .st-emotion-cache-vz9k5h.e1c29vlm19 {
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
  
with st.sidebar:
    st.markdown("Tema: Dracula")
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
