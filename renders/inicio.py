import streamlit as st
import streamlit.components.v1 as components

# Função utilitária para trocar de aba

def switch_to_tab(tab_name):
    js_code = f"""
    <script>
        var tabContainer = window.parent.document.querySelector('.stTabs');
        var tabButtons = tabContainer.querySelectorAll('[role="tab"]');
        tabButtons.forEach(function(button) {{
            if (button.innerText.trim() === "{tab_name}") {{
                button.click();
            }}
        }});
    </script>
    """
    st.components.v1.html(js_code, height=0, width=0)

def render():

  st.title("🎓 Bem-vindo à :blue[APROVA]")
  st.markdown("A plataforma criada por vestibulandos para vestibulandos.")
  st.markdown("Na :blue[APROVA], você encontra tudo o que precisa para conquistar sua vaga nas principais universidades de São Paulo, com o poder da :blue[Inteligência Aritificial] te guiando em cada etapa.")
 
  st.write("")
  
  st.markdown("""
            <h3 style='font-size: 20px; color: #36e096;'>Foco nos maiores vestibulares</h3>
            <p style='font-size: 17px; color: white;'>Nosso foco é te preparar para os três principais vestibulares de São Paulo: Fuvest (2026), Unicamp (2026) e, é claro, o Enem (2025). Mas se o seu objetivo está em outro processo seletivo, não se preocupe, a plataforma também te ajuda nessa jornada.
</p>
    """, unsafe_allow_html=True)

  if st.button("Conhecer os vestibulares", use_container_width=True, key="vestibulares_button", type="primary"):
        switch_to_tab("Vestibulares")
  
  st.divider()
  
  with st.container():
    col1, col2 = st.columns([1, 2])

  with col1: 
    st.image("assets/aprovadinho/aprovadinho_1.png")

  with col2:
    st.markdown("""
            <h3 style='font-size: 20px; color: #f26679;'>Estude de forme inteligente</h3>
            <p style='font-size: 17px; color: white;'>Escolha a matéria que quer estudar e receba resumos gerados por IA, objetivos, claros e atualizados.</p>
            <p style='font-size: 17px; color: white;'>Pratique com exercícios inéditos criados por Inteligência Artificial, adaptados ao seu ritmo.</p>
            <p style='font-size: 17px; color: white;'>Evolua com foco: todo o conteúdo é organizado por disciplina.</p>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    with col1:
      if st.button("Gerar resumos", use_container_width=True, key="resumos_button", type="primary"):
        switch_to_tab("Resumos")
    with col2:
      if st.button("Praticar", use_container_width=True, key="exercicios_button", type="primary"):
        switch_to_tab("Exercícios")

  st.divider()

  with st.container():
    col1,col2 = st.columns([1.9, 1])

    with col1: 
      with st.container():
          st.markdown("""
                <h3 style='font-size: 20px; color: #F697DB;'>Acesse as provas dos anos anteriores</h3>
                <p style='font-size: 17px; color: white;'>Acesse provas anteriores do Enem, Fuvest e Unicamp para treinar como se fosse o dia da prova.</p>
                <p style='font-size: 17px; color: white;'>Escolha o ano, a prova e comece a responder. É uma forma eficiente de revisar conteúdos e identificar seus pontos fortes e fracos.</p>
                <p style='font-size: 17px; color: white;'>Cada prova vem acompanhada de sua resolução comentada, baseadas nos critérios das vestibulars, para você aprender com os erros e evoluir a cada tentativa.</p>
        """, unsafe_allow_html=True)
          if st.button("Acessar provas", use_container_width=True, key="simulados_button", type="primary"):
              switch_to_tab("Provas")

    st.divider()

    with col2:
      st.image("assets/aprovadinho/aprovadinho_2.png")

  with st.container():
    col1, col2 = st.columns(2)
    with col1:
      with st.container(border=True):
          st.markdown("""
                  <h3 style='font-size: 20px; color: #FFB530;'>Leia as Redações mais exemplares</h3>
                  <p style='font-size: 17px; color: white;'>Veja exemplos reais de redações que alcançaram a nota máxima no Enem, Fuvest e Unicamp. Analise o que fez cada texto se destacar e entenda como aplicar essas estratégias na sua própria escrita.</p>
          """, unsafe_allow_html=True)
      if st.button("Ler textos", use_container_width=True, key="redacoes_button", type="primary"):
          switch_to_tab("Redações")

    with col2:
      with st.container(border=True):
        st.markdown("""
              <h3 style='font-size: 20px; color: #d39eff;'>Correção personalizada de redações</h3>
              <p style='font-size: 17px; color: white;'>Envie sua redação, escolha o vestibular e receba uma correção detalhada feita por Inteligência Artificial. A avaliação segue fielmente os critérios oficiais de cada vestibular.</p>
      """, unsafe_allow_html=True)
      if st.button("Corrigir texto", use_container_width=True, key="corracao_button", type="primary"):
          switch_to_tab("Correção")

  with st.container():
    col1, col2 = st.columns(2)

    with col1:
      with st.container(border=True):
        st.markdown("""
              <h3 style='font-size: 20px; color: #7144EE;'>Leitura obrigatória sem sofrimento</h3>
              <p style='font-size: 17px; color: white';>Saiba quais são os livros exigidos em cada vestibular e explore resumos completos, organizados e fáceis de entender para cada obra.</p>
      """, unsafe_allow_html=True)
      if st.button("Checar livros", use_container_width=True, key="livros_button", type="primary"):
          switch_to_tab("Livros")

    with col2:
      with st.container(border=True):
        st.markdown("""
              <h3 style='font-size: 20px; color: #b0e1ff;'>Saiba as Datas importantes sem stress</h3>
              <p style='font-size: 17px; color: white';>Fique por dentro de todos os prazos dos principais vestibulares, inscrições, datas de prova, resultados e muito mais, tudo em um só lugar.</p>
      """, unsafe_allow_html=True)
      if st.button("Ver datas", use_container_width=True, key="datas_button", type="primary"):
          switch_to_tab("Datas")

  st.divider()

  with st.container():
    col1, col2 = st.columns([2, 1])

  with col2: 
    st.image("assets/aprovadinho/aprovadinho_3.png")

  with col1:
    st.markdown("""
            <h3 style='font-size: 20px; color: #60B4FF;'>Conheça o Aprovadinho</h3><p style='font-size: 17px; color: white;'>O Aprovadinho é mais do que um mascote fofo.</p>
            <p style='font-size: 17px; color: white;'>Ele é um chatbot inteligente preparado para responder suas dúvidas sobre conteúdos, vestibulares, datas, estratégias e muito mais.</p>
            <p style='font-size: 17px; color: white;'>Fale com ele a qualquer hora. Ele está sempre pronto para te ajudar!</p>
    """, unsafe_allow_html=True)

    if st.button("Falar com o Aprovadinho", use_container_width=True, key="aprovadinho_button", type="primary"):
      switch_to_tab("Aprovadinho")
      
  st.divider()
  
  with st.container():
    col1, col2 = st.columns([1, 2])

  with col1: 
    st.image("assets/aprovadinho/aprovadinho_4.png")

  with col2:
    st.markdown("""
    <h3 style='font-size: 20px; color: #f08671;'>Ainda não sabe qual carreira seguir?</h3>
    <p style='font-size: 17px; color: white;'>Tudo bem! A escolha da profissão nem sempre é fácil, e você não precisa decidir isso sozinho.</p>
    <p style='font-size: 17px; color: white;'>Aqui na APROVA, você pode fazer um <strong>teste vocacional</strong> gratuito que te ajuda a descobrir quais áreas combinam mais com seus interesses, habilidades e valores.</p>
""", unsafe_allow_html=True)

    if st.button("Fazer o teste", use_container_width=True, key="carreira_button", type="primary"):
      switch_to_tab("Carreira")
  
  def read_html():
    with open("core/index.html") as f:
        return f.read()

  components.html(
    read_html(),
    height=0,
    width=0,
  )