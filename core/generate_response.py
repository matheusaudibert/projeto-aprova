import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "gemini-1.5-flash"

genai.configure(api_key=API_KEY)

def generate_vocational_response(answers):
    prompt = f"""
    Como conselheiro vocacional especializado, analise as respostas do teste vocacional abaixo:
    
    {answers}
    
    Com base nessas respostas:
    1. Identifique as principais áreas de interesse e habilidades
    2. Sugira 2-3 possíveis cursos que combinem com o perfil
    3. Explique brevemente por que estes cursos se alinham com as características demonstradas
    4. Forneça algumas orientações sobre os caminhos profissionais dessas áreas
    
    Formato da resposta:
    - Comece com "Com base nas suas respostas, identifiquei que você tem maior afinidade com..."
    - Use linguagem acolhedora mas profissional
    - Seja específico nas sugestões de cursos
    - Inclua uma mensagem motivacional no final
    
    Mantenha a resposta concisa e focada nas informações mais relevantes.
    """
    
    try:
        model = genai.GenerativeModel(model_name=MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print(f"Erro ao gerar resposta do teste vocacional: {e}")
        return "Não foi possível gerar a análise vocacional no momento."
