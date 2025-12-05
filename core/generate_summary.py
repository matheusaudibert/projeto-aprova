import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "gemini-2.5-flash"

genai.configure(api_key=API_KEY)

def generate_summary(subject):
    prompt = f"""
    Formate a resposta da seguinte maneira:

    # :blue[{subject}]

    Crie um resumo claro e objetivo para vestibulandos sobre o tema '{subject}'.
    O resumo deve conter informações relevantes e ser de fácil compreensão.

    Organize o resumo com títulos bem definidos, por exemplo:

    ## :blue[Título do tema]
    Texto do resumo, de forma clara e concisa, focado para vestibular.
    
    Ao fim coloque "como tal assunto é cobrado nos vestibulares".
    
    Não coloque "dicas ou algo do tipo", apenas o resumo.
    """
    
    try:
        model = genai.GenerativeModel(model_name=MODEL)
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print(f"Erro ao gerar o resumo: {e}")
        return "Não foi possível gerar o resumo no momento."
