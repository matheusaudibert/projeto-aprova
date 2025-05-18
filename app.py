import streamlit as st
from renders import inicio, provas, resumos, exercicios, redacoes, livros, vestibulares, correcao, datas, canais
from streamlit_plugins.components.theme_changer import st_theme_changer
from streamlit_plugins.components.theme_changer.entity import ThemeInfo, ThemeInput, ThemeBaseLight, ThemeBaseDark

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


init_theme_data = dict(
    light_day=ThemeInput(
        name="Light Day",
        icon=":material/light_mode:", 
        order=0,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#000000",
            backgroundColor="#ffffff",
            secondaryBackgroundColor="#e8e8e8",
            textColor="#000000",
            fontSizes={
                "bodyFont": 16,
                "codeFont": 16,
            },
        )
    ),
    dark_night=ThemeInput(
        name="Dark Night",
        icon=":material/dark_mode:",
        order=1,
        themeInfo=ThemeInfo(
            base=ThemeBaseDark.base,
            primaryColor="#d6d4d4",
            backgroundColor="#000000",
            secondaryBackgroundColor="#1e1e1e",
            textColor="#ffffff",
            fontSizes={
                "bodyFont": 16,
                "codeFont": 16,
            },
        )
    ),
    discord=ThemeInput(
        name="Discord",
        icon=":material/savings:",
        order=2,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#7289da",
            backgroundColor="#1e2124",
            secondaryBackgroundColor="#282b30",
            textColor="#f8f8f2",
            fontSizes={
                "bodyFont": 16,
                "codeFont": 16,
            },
            
        )
    ),
    dracula=ThemeInput(
        name="Dracula",
        icon=":material/menstrual_health:",
        order=3,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#ff79c6",
            backgroundColor="#282a36",
            secondaryBackgroundColor="#44475a",
            textColor="#f8f8f2",
            fontSizes={
                "bodyFont": 16,
                "codeFont": 16,
            },
            
        )
    ),
    github=ThemeInput(
        name="GitHub",
        icon=":material/code:",
        order=4,
        themeInfo=ThemeInfo(
            base=ThemeBaseLight.base,
            primaryColor="#5FED83",
            backgroundColor="#0D1117",
            secondaryBackgroundColor="#24292e",
            textColor="#ffffff",
            fontSizes={
                "bodyFont": 16,
                "codeFont": 16,
            },
        )
    ),
)

# if st.session_state.get("theme_data") is None:
#     st.session_state["theme_data"] = init_theme_data
    
# theme_data = st.session_state["theme_data"]
  
# st_theme_changer(themes_data=theme_data, render_mode="pills")
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
  
  