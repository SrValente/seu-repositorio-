import streamlit as st
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

st.set_page_config(page_title="Consulta de Grade Horária - TOTVS", layout="wide")

st.markdown(
    """
    <style>
    .streamlit-expanderHeader {
        color: #FFA500;
    }
    .stButton > button {
        color: #FFA500;
    }
    .stSelectbox, .stMultiselect, .stTextInput, .stSelectSlider, .stNumberInput, .stCheckbox {
        color: white;
    }
    .stTextInput input {
        color: white;
    }
    .stSelectbox, .stSelectSlider, .stMultiselect {
        border-color: #444;
    }
    .block-container {
        padding-bottom: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

USERNAME = "p_heflo"
PASSWORD = "Q0)G$sW]rj"
BASE_URL = "https://raizeducacao160286.rm.cloudtotvs.com.br:8051/api/framework/v1/consultaSQLServer/RealizaConsulta"

# ------------------------------------------------------------------------------
# Lista de filiais
# ------------------------------------------------------------------------------
filiais = [
    {"NOMEFANTASIA": "COLÉGIO QI TIJUCA",      "CODCOLIGADA": 2,  "CODFILIAL": 2},
    {"NOMEFANTASIA": "COLÉGIO QI BOTAFOGO",    "CODCOLIGADA": 2,  "CODFILIAL": 3},
    {"NOMEFANTASIA": "COLÉGIO QI FREGUESIA",   "CODCOLIGADA": 2,  "CODFILIAL": 6},
    {"NOMEFANTASIA": "COLÉGIO QI RIO 2",       "CODCOLIGADA": 2,  "CODFILIAL": 7},
    {"NOMEFANTASIA": "COLEGIO QI METROPOLITANO","CODCOLIGADA": 6,  "CODFILIAL": 1},
    {"NOMEFANTASIA": "COLEGIO QI RECREIO",     "CODCOLIGADA": 10, "CODFILIAL": 1},
]

# ------------------------------------------------------------------------------
# Função para consultar turmas (RAIZA.0005) usando parâmetro TURMA_NOME
# ------------------------------------------------------------------------------
def obter_turmas(codcoligada, codfilial, turma_nome=None):
    """
    Consulta RAIZA.0005, enviando CODCOLIGADA, CODFILIAL e TURMA_NOME (para busca parcial).
    É necessário que o SQL interno tenha algo como:
      (CODTURMA + ' - ' + DESCRICAO) LIKE :TURMA_NOME
      e retorne também 'TURMA_NOME' no SELECT.
    """
    if not turma_nome:
        turma_nome = "%"

    url = f"{BASE_URL}/RAIZA.0005/0/S"
    params = {"parameters": f"CODCOLIGADA={codcoligada};CODFILIAL={codfilial};TURMA_NOME={turma_nome}"}

    try:
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), params=params, verify=False)
        if response.status_code == 200:
            turmas = response.json()
            # Filtra localmente pela coligada/filial, se necessário
            return [t for t in turmas if t.get("CODCOLIGADA") == codcoligada and t.get("CODFILIAL") == codfilial]
        else:
            return {"error": f"Erro HTTP na consulta das turmas: {response.status_code}"}
    except requests.exceptions.SSLError:
        return {"error": "Erro de certificado SSL ao acessar a API"}

# ------------------------------------------------------------------------------
# Função para consultar grade horária (RAIZA.0004) usando CODTURMA
# ------------------------------------------------------------------------------
def obter_grade_horario(codturma, codcoligada, codfilial):
    url = f"{BASE_URL}/RAIZA.0004/0/S"
    params = {"parameters": f"CODCOLIGADA={codcoligada};CODFILIAL={codfilial};CODTURMA={codturma}"}
    try:
        response = requests.get(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), params=params, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Erro HTTP ao consultar a grade horária: {response.status_code}"}
    except requests.exceptions.SSLError:
        return {"error": "Erro de certificado SSL ao acessar a API"}

# ------------------------------------------------------------------------------
# Gera HTML para download/impressão da grade
# ------------------------------------------------------------------------------
def gerar_html(df, codturma):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Grade Horária - {codturma}</title>
        <style>
            @page {{
                size: A4 landscape;
                margin: 1cm;
            }}
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
            }}
            h1 {{
                color: #FFA500;
                text-align: center;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
                font-size: 12px;
            }}
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Grade Horária - {codturma}</h1>
        {df.to_html(index=False, escape=False)}
        <script>
            // Força o diálogo de impressão ao abrir o arquivo
            window.onload = function() {{
                window.print();
            }};
        </script>
    </body>
    </html>
    """
    return html

# ------------------------------------------------------------------------------
# Layout Streamlit
# ------------------------------------------------------------------------------
st.title("📅 Consulta de Grade Horária - TOTVS")
st.markdown("### 🏫 Selecionar Filial")

# Monta o selectbox de filiais
filiais_opcoes = {f"{f['NOMEFANTASIA']} ({f['CODFILIAL']})": (f['CODCOLIGADA'], f['CODFILIAL']) for f in filiais}
filial_escolhida = st.selectbox("Selecione a Filial:", list(filiais_opcoes.keys()))
codcoligada, codfilial = filiais_opcoes.get(filial_escolhida, (None, None))

# ------------------------------------------------------------------------------
# Se a filial for válida, pedir texto para buscar por Turma
# ------------------------------------------------------------------------------
if codcoligada and codfilial:

    # Campo de busca parcial da turma
    turma_nome_input = st.text_input(
        "Digite parte do nome/código da Turma (use '%' para listar todas):",
        value="%"
    )

    st.markdown("### 📋 Selecionar Turma")

    turmas = obter_turmas(codcoligada, codfilial, turma_nome_input)

    # Se retornou erro, exibir
    if isinstance(turmas, dict) and "error" in turmas:
        st.error(f"⚠️ {turmas['error']}")
    elif isinstance(turmas, list) and len(turmas) > 0:
        # Monta dicionário "TURMA_NOME" -> "CODTURMA"
        # Pressupõe que o RAIZA.0005 retorne um campo "TURMA_NOME"
        # ex.: "CODTURMA + ' - ' + DESCRICAO AS TURMA_NOME"
        turmas_opcoes = {
            t["TURMA_NOME"]: t["CODTURMA"]
            for t in turmas
            if "TURMA_NOME" in t and "CODTURMA" in t
        }

        if len(turmas_opcoes) == 0:
            st.warning("⚠️ Nenhuma turma encontrada para o filtro fornecido.")
        else:
            turma_selecionada = st.selectbox(
                "Selecione a Turma:",
                list(turmas_opcoes.keys())
            )
            codturma = turmas_opcoes[turma_selecionada]

            if st.button("🔎 Consultar Grade Horária"):
                grade = obter_grade_horario(codturma, codcoligada, codfilial)
                if isinstance(grade, list) and len(grade) > 0:
                    df = pd.DataFrame(grade).fillna("")
                    st.markdown("### 📅 Grade Horária")
                    st.dataframe(df)

                    # Gera e disponibiliza o HTML
                    html_content = gerar_html(df, codturma)
                    st.download_button(
                        label="📥 Baixar para PDF",
                        data=html_content,
                        file_name=f"Grade Horária - {codturma}.html",
                        mime="text/html",
                        help=(
                            "O arquivo será aberto automaticamente para impressão. "
                            "Use 'Salvar como PDF' nas opções de impressão do navegador."
                        )
                    )
                elif isinstance(grade, dict) and "error" in grade:
                    st.error(f"⚠️ {grade['error']}")
                else:
                    st.warning(
                        f"⚠️ Nenhuma grade horária encontrada para a turma {codturma} na filial {filial_escolhida}."
                    )
    else:
        st.warning("⚠️ Nenhuma turma encontrada para esta filial/filtro.")

else:
    st.warning("⚠️ Selecione uma filial válida.")
