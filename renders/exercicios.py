import streamlit as st
from constants.subjects import subjects
from core.generate_exercises import generate_exercises

def render():
  st.markdown("<h1 style='color: #f26679;'>Gerador de Exercícios</h1>", unsafe_allow_html=True)

  st.text("Pratique com exercícios gerados por AI focados nos temas que mais caem nos vestibulares. Escolha a área, a matéria e o assunto para testar seus conhecimentos de forma estratégica.")

  if 'exercises' not in st.session_state:
      st.session_state.exercises = None

  if 'answers' not in st.session_state:
      st.session_state.answers = {}

  if 'show_explanation' not in st.session_state:
      st.session_state.show_explanation = {}

  materias = subjects

  st.divider()

  area = st.selectbox("Selecione a área:", [""] + list(materias.keys()), key="exercicios_area")

  if area:  
      if isinstance(materias[area], dict):
          materia = st.selectbox("Selecione a matéria:", [""] + list(materias[area].keys()), key="exercicios_materia")
          if materia:  
              subtopicos = materias[area][materia]
          else:
              subtopicos = []
      else:
          materia = None
          subtopicos = materias[area]

      if subtopicos:  
          if isinstance(subtopicos, dict):
              subtopico_key = st.selectbox("Selecione o subtópico:", [""] + list(subtopicos.keys()), key="exercicios_subtopico")
              if subtopico_key:
                  topico = st.selectbox("Selecione o tema:", [""] + subtopicos[subtopico_key], key="exercicios_topico")
              else:
                  topico = ""
          else:
              topico = st.selectbox("Selecione o tópico específico:", [""] + subtopicos, key="exercicios_topico")
      else:
          topico = ""

      if area and (materia or not isinstance(materias[area], dict)) and topico:
          if st.button("Gerar Exercícios", type="primary", key="gen_exercises"):
              with st.spinner("Gerando exercícios..."):
                  subject = f"{topico} - {materia if isinstance(materias[area], dict) else area}"
                  st.session_state.exercises = generate_exercises(subject=subject)
                  st.session_state.answers = {}
                  st.session_state.show_explanation = {}

      if st.session_state.exercises:
          for i, exercise in enumerate(st.session_state.exercises, 1):
              with st.container(border=True):
                  st.markdown(f"**Questão {i}**")
                  st.markdown(exercise['question'])

                  options = [alt.strip() for alt in exercise['alternatives']]
                  answer = st.radio("Escolha uma alternativa:",
                                    options,
                                    key=f"q_{i}",
                                    index=None,
                                    label_visibility="collapsed")

                  if answer:
                      st.session_state.answers[i] = answer

                  if st.button("Verificar", key=f"check_{i}", type="primary"):
                      st.session_state.show_explanation[i] = True

                  if i in st.session_state.answers and i in st.session_state.show_explanation:
                      correct_letter = exercise['correct']
                      if st.session_state.answers[i].startswith(correct_letter):
                          st.success("Resposta correta! 🎉")
                      else:
                          st.error(f"Resposta incorreta. A alternativa correta é {correct_letter}")
                      st.info("**Explicação:**\n\n" + exercise['explanation'])
  else:
      st.info("Selecione uma área para começar.")
