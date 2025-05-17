import streamlit as st
import webbrowser

import streamlit as st

def render():
    st.markdown("<h1 style='color: #36e096;'>Vestibulares</h1>", unsafe_allow_html=True)
    st.text("Nesta seção, você vai conhecer os detalhes dos três vestibulares mais importantes para quem quer estudar nas maiores universidades públicas de São Paulo e do país: ENEM, FUVEST e UNICAMP. Descubra como funciona cada prova, o que elas cobram, e quais caminhos elas abrem para o seu futuro. Informação clara e direta, para te ajudar a escolher a melhor estratégia de preparação.")
    
    st.divider()
  
    # ENEM
    st.markdown("""
        <h3 style='font-size: 24px; color: #36e096;'>ENEM (Exame Nacional do Ensino Médio)</h3>
        <p style='font-size: 17px; text-align: justify;'>
        O ENEM é uma das principais portas de entrada para o ensino superior no Brasil. Aplicado anualmente em todo o país, o exame avalia os conhecimentos adquiridos ao longo do ensino médio. A prova é composta por 180 questões objetivas e uma redação, divididas em dois dias de aplicação.
        <br><br>
        As quatro áreas de conhecimento cobradas são: Linguagens, Códigos e suas Tecnologias; Ciências Humanas; Ciências da Natureza; e Matemática. A redação exige que o aluno desenvolva um texto dissertativo-argumentativo com base em uma situação-problema.
        <br><br>
        A nota do ENEM pode ser usada para ingressar em universidades públicas pelo <strong>SISU</strong>, além de permitir acesso a programas como o <strong>PROUNI</strong> (bolsas de estudo) e o <strong>FIES</strong> (financiamento estudantil). É uma prova que valoriza interpretação de texto, raciocínio lógico e resistência física e mental.</p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("assets/vestibulares/enem.png", width=400)

    st.divider()

    # FUVEST
    st.markdown("""
        <h3 style='font-size: 24px; color: #36e096;'>FUVEST (USP)</h3>
        <p style='font-size: 17px;  text-align: justify;'>
        A FUVEST é o vestibular da <strong>Universidade de São Paulo (USP)</strong>, uma das mais respeitadas instituições de ensino superior da América Latina. A prova é tradicionalmente uma das mais concorridas e exigentes do país.
        <br><br>
        O processo seletivo ocorre em duas fases: a <strong>primeira fase</strong> é composta por 90 questões objetivas de múltipla escolha envolvendo todas as disciplinas do ensino médio. Já a <strong>segunda fase</strong> é dissertativa, com questões específicas de acordo com a carreira escolhida, além de uma redação obrigatória.
        <br><br>
        A FUVEST valoriza a profundidade do conteúdo, clareza na argumentação e capacidade de análise crítica. É ideal para quem busca formação sólida em cursos de alto nível e reconhecimento nacional e internacional.</p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image("assets/vestibulares/fuvest.png", width=400)

    st.divider()

    # UNICAMP
    st.markdown("""
        <h3 style='font-size: 24px; color: #36e096;'>UNICAMP (Universidade Estadual de Campinas)</h3>
        <p style='font-size: 17px;  text-align: justify;'>
        O vestibular da <strong>UNICAMP</strong> é conhecido por sua abordagem interdisciplinar e por valorizar o raciocínio crítico. A universidade está entre as melhores do Brasil, com forte presença em pesquisas científicas e inovação.
        <br><br>
        A prova também ocorre em duas fases: a <strong>primeira fase</strong> possui questões objetivas de múltipla escolha que envolvem múltiplas áreas do conhecimento. A <strong>segunda fase</strong> traz questões dissertativas e inclui uma redação. Algumas carreiras exigem provas específicas (como habilidades para artes cênicas e música).
        <br><br>
        Além do vestibular tradicional, a UNICAMP também permite ingresso via ENEM e oferece modalidades específicas, como o vestibular indígena e o vestibular para pessoas com ensino médio em escolas públicas.
        <br><br>
        É uma excelente opção para quem busca uma formação de qualidade, com incentivo à pesquisa, inovação e extensão universitária.</p>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("assets/vestibulares/unicamp.png", width=200)
