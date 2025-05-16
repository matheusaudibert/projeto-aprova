import re

def clear_summary(text):
    # Remove marcações de cor do Streamlit (ex: :blue[texto])
    text = re.sub(r':\w+\[(.*?)\]', r'\1', text)
    
    # Remove marcações de título markdown (##)
    text = re.sub(r'^##\s*', '', text, flags=re.MULTILINE)
    
    # Remove múltiplas linhas vazias
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()
