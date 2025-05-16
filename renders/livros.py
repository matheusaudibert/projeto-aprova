import streamlit as st
from core.generate_reads import a_visao_das_plantas, as_meninas, balada_de_amor_ao_vento, caminho_de_pedras, cancao_para_ninar_menino_grande, memorias_de_martha, nebulosas, o_cristo_cigano, opusculo_humanitario, a_vida_nao_e_util, alice_no_pais_das_maravilhas, cancoes_escolhidas, casa_velha, morangos_mofados, no_seu_pescoco, olhos_d_agua, prosas_seguidas_de_odes_minimas, vida_e_morte_de_m_j_gonzaga_de_sa

def render():
  st.title("Leituras Obrigatórias")  
  st.text("Use esta ferramenta para praticar seus conhecimentos com simulados focados. Basta escolher a área do conhecimento, a matéria e o tema desejado, e o gerador criará questões que ajudam a fixar o conteúdo mais cobrado no ENEM e nos principais vestibulares. Ideal para testar seu aprendizado e se preparar para as provas.")
  
  st.divider()
  
  col1, col2 = st.columns([1,2.25])
  
  with col1:
    with st.container(border=False):
      st.markdown("##### Selecione o livro da Fuvest")
      
      if st.button("A Visão das Plantas", key="a_visao_das_plantas", use_container_width=True, type="primary"):
        with col2:
          a_visao_das_plantas()
      if st.button("As meninas", key="as_meninas", use_container_width=True, type="primary"):
        with col2:
          as_meninas()
      if st.button("Balada de amor ao vento", key="balada_de_amor_ao_vento", use_container_width=True, type="primary"):
        with col2:
          balada_de_amor_ao_vento()
      if st.button("Caminho de Pedras", key="caminho_de_pedras", use_container_width=True, type="primary"):
        with col2:
          caminho_de_pedras()
      if st.button("Canção para ninar menino grande", key="cancao_para_ninar_menino_grande", use_container_width=True, type="primary"):
        with col2:
          cancao_para_ninar_menino_grande()
      if st.button("Memórias de Martha", key="memorias_de_martha", use_container_width=True, type="primary"):
        with col2:
          memorias_de_martha()
      if st.button("Nebulosas", key="nebulosas", use_container_width=True, type="primary"):
        with col2:
          nebulosas()
      if st.button("O Cristo Cigano", key="o_cristo_cigano", use_container_width=True, type="primary"):
        with col2:
          o_cristo_cigano()
      if st.button("Opúsculo Humanitário", key="opusculo_humanitario", use_container_width=True, type="primary"):
        with col2:
          opusculo_humanitario()
          
      st.write("")
      st.write("")
  
  with col1:
     with st.container(border=False):
      st.markdown("##### Selecione o livro da Unicamp")
      if st.button("A vida não é útil", key="a_vida_nao_e_util", use_container_width=True, type="primary"):
        with col2:
          a_vida_nao_e_util()
      if st.button("Alice no país das maravilhas", key="alice_no_pais_das_maravilhas", use_container_width=True, type="primary"):
        with col2:
          alice_no_pais_das_maravilhas()
      if st.button("Canções Escolhidas - Cartola", key="cancoes_escolhidas", use_container_width=True, type="primary"):
        with col2:
          cancoes_escolhidas()
      if st.button("Casa Velha", key="casa_velha", use_container_width=True, type="primary"):
        with col2:
          casa_velha()
      if st.button("Morangos Mofados", key="morangos_mofados", use_container_width=True, type="primary"):
        with col2:
          morangos_mofados()
      if st.button("No seu pescoço", key="no_seu_pescoco", use_container_width=True, type="primary"):
        with col2:
          no_seu_pescoco()
      if st.button("Olhos D'Água", key="olhos_d_agua", use_container_width=True, type="primary"):
        with col2:
          olhos_d_agua()
      if st.button("Prosas seguidas de odes mínima", key="prosas_seguidas_de_odes_minimas", use_container_width=True, type="primary"):
        with col2:
          prosas_seguidas_de_odes_minimas()
      if st.button("Vida e morte de M.J. Gonzaga de Sá", key="vida_e_morte_de_m_j_gonzaga_de_sa", use_container_width=True, type="primary"):
        with col2:
          vida_e_morte_de_m_j_gonzaga_de_sa()
  