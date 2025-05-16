import streamlit as st
import os
import google.generativeai as genai
from constants.settings import system_instruction
from dotenv import load_dotenv
import base64

# Título
st.title("Converse com o Aprovadinho")
st.text("Use o Aprovadinho para tirar dúvidas rápidas e revisar os conteúdos essenciais do vestibular com respostas diretas e objetivas. Sua preparação mais eficiente começa aqui!")

# Carrega variáveis do .env
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "gemini-2.0-flash"

# Configura a API
genai.configure(api_key=API_KEY)

# Cria o modelo com instrução de sistema
model = genai.GenerativeModel(
    model_name=MODEL,
    system_instruction=system_instruction
)

# Inicia sessão
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Função para codificar imagem em base64
def base64_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Função para exibir mensagem com imagem e alinhamento
def display_message(text, sender):
    if sender == "user":
        avatar = "assets/aprovadinho/aprovadinho_user.png"
        color = "#ffffff"  # Cor do texto do usuário
        name = "Você"
        align = "flex-end"
        text_align = "right"
        bg_color = "#36393e"
    else:
        avatar = "assets/aprovadinho/aprovadinho_bot.png"
        color = "#ffffff"  # Cor do texto do bot
        name = "Aprovadinho"
        align = "flex-start"
        text_align = "left"
        bg_color = "#1e2124"

    st.markdown(f"""
    <div style="display: flex; justify-content: {align}; margin: 10px 0;">
        <div style="display: flex; align-items: flex-start; flex-direction: row; max-width: 80%; {'flex-direction: row-reverse;' if sender == 'user' else ''}">
            <img src="data:image/png;base64,{base64_image(avatar)}" width="40" style="margin: 0 10px; border-radius: 50%;" />
            <div>
                <strong style="display:block; text-align: {text_align}; color: {color};">{name}</strong>
                <div style="background: {bg_color}; padding: 10px 14px; border-radius: 10px; text-align: {text_align}; color: {color};">{text}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Renderiza histórico
for msg in st.session_state.chat_session.history:
    sender = "user" if msg.role == "user" else "bot"
    display_message(msg.parts[0].text, sender)

# Entrada
user_input = st.chat_input("Digite sua mensagem:")

if user_input:
    display_message(user_input, "user")
    response = st.session_state.chat_session.send_message(user_input)
    display_message(response.text.strip(), "bot")