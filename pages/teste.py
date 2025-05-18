import streamlit as st
import time
import streamlit.components.v1 as components
import random  # Adicionar import

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
    
    st.markdown("**Tema: Dracula 🧛‍♀️**")
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
st.markdown("Responda algumas perguntas rápidas e descubra, **com ajuda da IA**, qual área combina mais com você e **quais cursos são ideais para o seu perfil**. O teste é rapidinho e divertido, você deve apenas responder **16 perguntas**! E você pode fazer quantas vezes quiser! **Vamos lá?**")
st.write("")
# Perguntas do teste vocacional
questions = [
    "Resolver problemas matemáticos é algo que você gosta?",
    "Você curte fazer ou acompanhar experimentos científicos?",
    "Ler e interpretar textos literários te agrada?",
    "Participar de debates sobre temas sociais é algo que te interessa?",
    "Criar ou apreciar arte faz parte do que você gosta de fazer?",
    "Você se sente atraído por tecnologia e computadores?",
    "Ajudar e cuidar das pessoas é algo que te faz bem?",
    "Assuntos sobre meio ambiente e sustentabilidade te interessam?",
    "Liderar grupos ou projetos é algo que você gosta de fazer?",
    "Aprender sobre culturas diferentes e novos idiomas te atrai?",
    "Você gosta de atividades que envolvem planejamento e organização?",
    "Aprender sobre o corpo humano e temas ligados à saúde te interessa?",
    "Empreender ou lidar com negócios é algo que te chama atenção?",
    "Estudar história e entender o passado é algo que te atrai?",
    "A mediação de conflitos e ajudar pessoas a se entenderem te interessa?",
    "Pesquisar e investigar sobre assuntos diversos é algo que você gosta?"
]


# Inicialização do estado da sessão
if 'test_started' not in st.session_state:
    st.session_state.test_started = False
    st.session_state.current_question = 0
    st.session_state.answers = {}
    # Adicionar lista de questões randomizadas ao estado
    st.session_state.randomized_questions = random.sample(questions, len(questions))

if not st.session_state.test_started:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Iniciar o teste", use_container_width=True, type="primary"):
            st.session_state.test_started = True
            st.rerun()
else:
    # Mostra progresso (ajustado para estar entre 0 e 1)
    progress = st.session_state.current_question / len(questions)
    st.progress(progress)
    
    # Mostra questão atual usando a lista randomizada
    if st.session_state.current_question < len(questions):
        question = st.session_state.randomized_questions[st.session_state.current_question]
        st.write(f"### {question}")
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        # Opções de resposta com emojis
        options = {
            "Detesto": ":material/sentiment_sad:",
            "Não gosto": ":material/sentiment_dissatisfied:",
            "Indiferente": ":material/sentiment_neutral:",
            "Gosto": ":material/sentiment_satisfied:",
            "Adoro": ":material/sentiment_very_satisfied:"
        }
        
        selected = None
        for i, (text, emoji) in enumerate(options.items()):
            with [col1, col2, col3, col4, col5][i]:
                if st.button(f"{text}\n\n{emoji}", key=f"q_{st.session_state.current_question}_{i}", use_container_width=True, type="secondary"):
                    st.session_state.answers[question] = text
                    st.session_state.current_question += 1
                    st.rerun()
                    
    else:
        from core.generate_response import generate_vocational_response
        
        st.success("Teste concluído! Analisando suas respostas...")
        
        formatted_answers = "\n".join([f"{q}: {a}" for q, a in st.session_state.answers.items()])
        
        with st.status("Gerando resposta do teste vocacional...", expanded=True):
            st.write("Analisando respostas...")
            time.sleep(3)
            st.write("Procurando cursos...")
            time.sleep(3)
            analysis = generate_vocational_response(formatted_answers)
            st.write("Formatando resposta...")
            time.sleep(3)
            
            
        with st.container(border=True):
            st.markdown("### 🎯 Sua Análise Vocacional")
            st.markdown(analysis)
        
        # Botão para recomeçar
        if st.button("Fazer o teste novamente", type="primary", use_container_width=True):
            st.session_state.test_started = False
            st.session_state.current_question = 0
            st.session_state.answers = {}
            # Gerar nova ordem aleatória ao recomeçar
            st.session_state.randomized_questions = random.sample(questions, len(questions))
            st.rerun()

        
def read_html():
    with open("./core/index.html") as f:
        return f.read()

components.html(
    read_html(),
    height=0,
    width=0,
)

