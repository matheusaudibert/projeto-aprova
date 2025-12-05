import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "gemini-2.5-flash"

genai.configure(api_key=API_KEY)

def generate_exercises(subject):
    prompt = f"""
        Crie 5 questões de vestibular sobre {subject}.
        Apenas texto, sem imagens, gráficos ou fórmulas em LaTeX.
        Formate a resposta da seguinte maneira para cada questão:

        QUESTAO_1:
        Enunciado da questão
        A) Alternativa A
        B) Alternativa B
        C) Alternativa C
        D) Alternativa D
        E) Alternativa E
        CORRETA: Letra correta (apenas a letra)
        EXPLICACAO: Explicação detalhada da resposta correta, sempre completa.

        [Repita o formato para as 5 questões, numerando QUESTAO_2, QUESTAO_3, etc.]
    """
    
    try:
        model = genai.GenerativeModel(model_name=MODEL)
        response = model.generate_content(prompt)
        content = response.text.strip()

        questions = []
        current_question = {}

        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('QUESTAO_'):
                if current_question:
                    questions.append(current_question)
                current_question = {'alternatives': []}
            elif line.startswith(('A)', 'B)', 'C)', 'D)', 'E)')):
                current_question['alternatives'].append(line)
            elif line.startswith('CORRETA:'):
                current_question['correct'] = line.split(':', 1)[1].strip()
            elif line.startswith('EXPLICACAO:'):
                current_question['explanation'] = line.split(':', 1)[1].strip()
            elif line and current_question is not None:
                if 'question' not in current_question:
                    current_question['question'] = line

        if current_question:
            questions.append(current_question)

        return questions

    except Exception as e:
        print(f"Erro ao gerar exercícios: {e}")
        return []
