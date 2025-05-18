import streamlit as st
import os
import streamlit.components.v1 as components
import google.generativeai as genai
from constants.settings import system_instruction
from dotenv import load_dotenv
import base64

st.set_page_config(
    page_title="Aprovadinho Chat",
    initial_sidebar_state="expanded",
    page_icon="🤖",
    layout="centered",
)

def base64_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def display_message(text, sender):
    if sender == "user":
        avatar = "assets/aprovadinho/aprovadinho_user.png"
        color = "#ffffff" 
        name_color = "#995EA9" 
        name = "Você"
        align = "flex-end"
        text_align = "right"
        bg_color = "#36393e"
    else:
        avatar = "assets/aprovadinho/aprovadinho_bot.png"
        color = "#ffffff"
        name_color = "#60B4FF" 
        name = "Aprovadinho"
        align = "flex-start"
        text_align = "left"
        bg_color = "#26282b"

    st.markdown(f"""
    <div style="display: flex; justify-content: {align}; margin: 10px 0;">
        <div style="display: flex; align-items: flex-start; flex-direction: row; max-width: 80%; {'flex-direction: row-reverse;' if sender == 'user' else ''}">
            <img src="data:image/png;base64,{base64_image(avatar)}" width="40" style="margin: 0 10px; border-radius: 50%;" />
            <div>
                <strong style="display:block; text-align: {text_align}; color: {name_color};">{name}</strong>
                <div style="background: {bg_color}; padding: 10px 14px; border-radius: 10px; text-align: {text_align}; color: {color};">{text}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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
    
    st.markdown("Tema: Dracula")
    st.markdown("# 🎓 Aprova")  
    st.markdown("*Este projeto foi desenvolvido durante a **Imersão IA** da **:blue[Alura]** em parceria com o **:blue[G]:red[o]:orange[o]:blue[g]:green[l]:red[e] :violet[Gemini]***.")
  
    st.markdown("# 🎈 Extras") 
    st.text("Conheça o Aprovadinho, o chatbot da plataforma, e tire suas dúvidas sobre os principais vestibulares do Brasil.")
    if st.button("Aprovadinho", use_container_width=True, key="aprovadinho_sidebar_2_button"):
        st.switch_page("pages/aprovadinho.py")
        
    st.write("")
        
    st.text("Faça o teste vocacional agora e descubra qual carreira combina mais com você.")
    if st.button("Teste vocacional", use_container_width=True, key="teste_sidebar_2_button"):
        st.switch_page("pages/teste.py")
        
    st.write("")
    st.markdown("😼 GitHub do projeto [aqui](https://github.com/matheusaudibert/projeto-aprova)!")

col1, col2 = st.columns([1, 7])
with col2:
    st.markdown("<h1 style='color: #60B4FF;'>Converse com o Aprovadinho</h1>", unsafe_allow_html=True)
with col1:
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    if st.button("Voltar", use_container_width=True, key="voitar_button", type="primary"):
        st.switch_page("app.py")
st.markdown("Use o **Aprovadinho** para **tirar dúvidas rápidas** e **revisar os conteúdos** essenciais do vestibular com respostas diretas e objetivas. **Sua preparação mais eficiente começa aqui!**")

# Variável que armazenará o texto vindo dos botões
user_input = None

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Dicas para o vestibular", use_container_width=True, key="1", type="secondary"):
        user_input = "Me dê dicas para o vestibular."
        
with col2:
    if st.button("Maiores notas de corte", use_container_width=True, key="2", type="secondary"):
        user_input = "Quais são as maiores notas de corte dos vestibulares?"

with col3:
    if st.button("Possíveis temas de redação", use_container_width=True, key="3", type="secondary"):
        user_input = "Me diga possíveis temas de redação para o vestibulares da Unicamp e Fuvest 2026 e ENEM 2025."  
    
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "gemini-2.0-flash"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    model_name=MODEL,
    system_instruction=system_instruction
)

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Exibe histórico da conversa
for msg in st.session_state.chat_session.history:
    sender = "user" if msg.role == "user" else "bot"
    display_message(msg.parts[0].text, sender)

# Se veio input por botão, processa aqui
if user_input is not None:
    display_message(user_input, "user")
    response = st.session_state.chat_session.send_message(user_input)
    display_message(response.text.strip(), "bot")

# Campo normal para input do usuário
typed_input = st.chat_input("Digite sua mensagem:")

if typed_input:
    display_message(typed_input, "user")
    response = st.session_state.chat_session.send_message(typed_input)
    display_message(response.text.strip(), "bot")
    
def read_html():
    with open("./core/index.html") as f:
        return f.read()

components.html(
    read_html(),
    height=0,
    width=0,
)
