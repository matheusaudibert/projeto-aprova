import os
import google.generativeai as genai
from mimetypes import guess_type
import re
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')
MODEL = "gemini-2.5-flash"

genai.configure(api_key=API_KEY)

def get_criterios_vestibular(vestibular):
    vestibular = vestibular.upper()
    if vestibular == 'ENEM':
        return {
            'criterios': """
Corrija a redação com base nos critérios do ENEM:

- **Competência 1**: Domínio da modalidade escrita formal da língua portuguesa.
- **Competência 2**: Compreensão da proposta de redação e aplicação de conceitos para desenvolver o tema em texto dissertativo-argumentativo.
- **Competência 3**: Seleção, organização e interpretação de informações, fatos, opiniões e argumentos.
- **Competência 4**: Conhecimento dos mecanismos linguísticos para construção da argumentação.
- **Competência 5**: Elaboração de uma proposta de intervenção para o problema abordado, respeitando os direitos humanos.
""",
            'pontuacao': "A pontuação total da redação do ENEM é de 0 a 1000 pontos.",
            'instrucao_pontuacao': "Forneça uma pontuação para cada competência de 0 a 200 e uma pontuação total."
        }
    elif vestibular == 'UNICAMP':
        return {
            'criterios': """
Corrija a redação com base nos critérios da UNICAMP:

- Compreensão da proposta temática (até 2 pontos).
- Adequação ao gênero solicitado (até 3 pontos).
- Leitura pertinente dos textos de apoio (até 3 pontos).
- Convenções da escrita e coesão (até 4 pontos).
""",
            'pontuacao': "A pontuação total da redação da UNICAMP é de 0 a 12 pontos.",
            'instrucao_pontuacao': "Forneça a pontuação por critério e o total."
        }
    elif vestibular == 'FUVEST':
        return {
            'criterios': """
Corrija a redação com base nos critérios da FUVEST:

- Desenvolvimento consistente do tema.
- Argumentos coerentes.
- Domínio da norma culta.
""",
            'pontuacao': "A pontuação total da redação da FUVEST é de 0 a 50 pontos.",
            'instrucao_pontuacao': "Forneça uma pontuação geral."
        }
    else:
        raise ValueError("vestibular inválida.")

def verificar_sentido_redacao_com_arquivo(file_path, tema):
    try:
        mime_type, _ = guess_type(file_path)
        with open(file_path, "rb") as f:
            media = {
                "mime_type": mime_type,
                "data": f.read()
            }

        prompt = f"""
Este é um arquivo de redação. Verifique se o conteúdo parece ser uma redação coerente, com introdução, desenvolvimento e conclusão, e se está relacionado ao tema abaixo.

Tema: "{tema}"

Responda apenas com "SIM" ou "NÃO".
"""

        model = genai.GenerativeModel(model_name=MODEL)
        response = model.generate_content([prompt, media])
        resposta = response.text.strip().upper()
        return "SIM" in resposta
    except Exception as e:
        print(f"Erro ao verificar sentido da redação: {e}")
        return False

def generate_correction(file_path, vestibular, tema):
    try:
        vestibular = vestibular.upper()
        info = get_criterios_vestibular(vestibular)

        # Prompts personalizados por vestibular
        if vestibular == "ENEM":
            corpo_prompt = """
Você é um corretor da vestibular ENEM.

Não printe as coisas que estiverem entre colchetes, eles são apenas instruções para você.

Corrija a redação enviada com base nos critérios abaixo, avaliando cada competência individualmente de forma estruturada.

Tema da redação: "{tema}"

{criterios}
{pontuacao}
{instrucao_pontuacao}

Formato obrigatório para cada competência:

Nota da Redação: [0 a 1000]

Competência 1

Domínio da modalidade escrita formal da língua portuguesa.

**Sua nota nessa competência foi: [nota de 0 a 200]**

[Justificativa técnica da nota]

(Repita esse padrão até a Competência 5. Não inclua dicas, reescritas ou conselhos. Apenas a correção estruturada.)
""".format(tema=tema, **info)

        elif vestibular == "UNICAMP":
            corpo_prompt = """
Você é um corretor da UNICAMP.

Não printe as coisas que estiverem entre colchetes, eles são apenas instruções para você.

Corrija a redação com base nos critérios da UNICAMP, avaliando os 4 itens abaixo de forma objetiva e técnica.

Tema da redação: "{tema}"

{criterios}
{pontuacao}
{instrucao_pontuacao}

Formato obrigatório:

Nota da Redação: [0 a 12]

Critério 1

Compreensão da proposta temática.

**Nota: [0 a 2]**

[Justificativa técnica]

[linha em branco]

Critério 2

Adequação ao gênero solicitado.

**Nota: [0 a 3]**

[Justificativa técnica]

[linha em branco]

Critério 3

Leitura pertinente dos textos de apoio.

**Nota: [0 a 3]**

[Justificativa técnica]

[linha em branco]

Critério 4

Convenções da escrita e coesão.

**Nota: [0 a 4]**

[Justificativa técnica]

[linha em branco]

Apenas entregue o relatório no formato acima. Não inclua dicas ou sugestões.
""".format(tema=tema, **info)

        elif vestibular == "FUVEST":
            corpo_prompt = """
Você é um corretor da FUVEST.

Não printe as coisas que estiverem entre colchetes, eles são apenas instruções para você.

Corrija a redação com base nos critérios da FUVEST:

- Desenvolvimento consistente do tema.  
- Argumentos coerentes.  
- Domínio da norma culta.

Tema da redação: "{tema}"

{criterios}
{pontuacao}
{instrucao_pontuacao}

Formato obrigatório:

Nota da redação: [0 a 50]

[Aqui coloque a justificativa técnica com base nos critérios acima. Seja objetivo.]

Apenas devolva a nota com a justificativa, sem dicas, reescritas ou sugestões.
""".format(tema=tema, **info)

        else:
            raise ValueError("vestibular inválida.")

        mime_type, _ = guess_type(file_path)
        with open(file_path, "rb") as f:
            media = {
                "mime_type": mime_type,
                "data": f.read()
            }

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([corpo_prompt, media])
        return response.text.strip()

    except Exception as e:
        return f"Erro ao corrigir: {e}"
      
    
def formatar_resultado(resultado: str, vestibular: str):
    vestibular = vestibular.upper()
    if vestibular == "ENEM":
        # Exibe a nota geral
        nota_geral = re.search(r"Nota da Redação:.*", resultado)
        if nota_geral:
            st.markdown(f"### {nota_geral.group()}")
        
        # Regex para pegar cada bloco da competência até antes da próxima competência ou fim do texto
        competencias = re.findall(
            r"(Competência \d(?:\n(?!Competência).*)+)",  # pega linhas que não começam com Competência
            resultado
        )

        # Para cada competência, cria um container separado
        for bloco in competencias:
            with st.container(border=True):
                st.markdown(bloco.strip())

    elif vestibular == "UNICAMP":
        nota_geral = re.search(r"Nota da Redação:.*", resultado)
        if nota_geral:
            st.markdown(f"### {nota_geral.group()}")

        criterios = re.findall(
            r"(Critério \d[\s\S]*?\*\*Nota:.*?\*\*[\s\S]*?(?=\nCritério|\Z))",
            resultado
        )

        for bloco in criterios:
            with st.container(border=True):
                st.markdown(bloco.strip())

    elif vestibular == "UNICAMP":
        nota_geral = re.search(r"Nota da Redação:.*", resultado)
        if nota_geral:
            st.markdown(f"### {nota_geral.group()}")

        criterios = re.split(r"(Critério \d[\s\S]*?\*\*Nota:.*?\*\*[\s\S]*?(?=\nCritério|\Z))", resultado)
        for bloco in criterios:
            if "Critério" in bloco:
                with st.container(border=True):
                    st.markdown(f"\n{bloco.strip()}\n")

    elif vestibular == "FUVEST":
        nota = re.search(r"Nota da redação:.*", resultado)
        if nota:
            st.markdown(f"### {nota.group()}")

        justificativa = resultado.split("Nota da redação:")[-1].strip()
        justificativa = re.sub(r"^\s*\d{1,3}\s*", "", justificativa)
        if justificativa:
            with st.container(border=True):
                st.markdown(f"\n{justificativa}\n")

    else:
        st.error("vestibular não reconhecido para formatação.")