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
    </style>
""", unsafe_allow_html=True)

  st.markdown("# 🎓 Aprova")  
  st.markdown("*Este projeto foi desenvolvido durante a **Imersão IA** da **Alura** em parceria com o **Google Gemini***.")
  
  if st.button("Aprovadinho", use_container_width=True, key="aprovadinho_sidebar_button"):
      st.switch_page("pages/aprovadinho.py")
