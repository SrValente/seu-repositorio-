import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Raiza - Gestão Escolar",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Customizado
st.markdown("""
<style>
    /* Gradiente no cabeçalho */
    [data-testid="stHeader"] {
        background: linear-gradient(135deg, #1e3a8a, #3b82f6);
        color: white;
    }
    
    /* Cards modernos */
    .card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        min-height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .card-title {
        font-size: 1.5rem;
        color: #1e3a8a;
        margin-bottom: 15px;
    }
    
    .card-description {
        color: #4b5563;
        line-height: 1.6;
    }
    
    /* Botões estilizados */
    .stButton > button {
        width: 100%;
        border: none;
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white !important;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        opacity: 0.9;
        transform: scale(1.02);
    }
    
    /* Layout responsivo */
    @media (max-width: 768px) {
        .col {
            margin-bottom: 20px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Conteúdo Principal
st.title("🏫 Bem-vindo ao Sistema Raiza")
st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h3 style="color: #4b5563; font-weight: 400;">
            Plataforma Integrada de Gestão Escolar
        </h3>
    </div>
""", unsafe_allow_html=True)

# Grid de Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">📋 Registro de Ocorrências</div>
            <div class="card-description">
                Registre e acompanhe incidentes escolares com detalhamento completo:
                - Classificação por tipo
                - Registro de envolvidos
                - Acompanhamento temporal
            </div>
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <button>Acessar Módulo</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(" ", key="btn1"):
        st.switch_page("pages/1_📋_Ocorrências.py")

with col2:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">🕒 Grade Horária Inteligente</div>
            <div class="card-description">
                Controle completo da grade curricular:
                - Visualização por turma/professor
                - Alertas de conflitos
                - Exportação para PDF
                - Integração com calendário
            </div>
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <button>Acessar Módulo</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(" ", key="btn2"):
        st.switch_page("pages/2_🕒_Grade_Horária.py")

with col3:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">📅 Gestão de Frequência</div>
            <div class="card-description">
                Sistema completo de controle de presenças:
                - Lançamento em massa
                - Relatórios automáticos
                - Integração com diário de classe
                - Alertas de infrequência
            </div>
        </div>
        <div style="text-align: center; margin-top: 20px;">
            <button>Acessar Módulo</button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button(" ", key="btn3"):
        st.switch_page("pages/3_📅_Lançamento_Faltas.py")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #6b7280;">
    <p style="font-size: 0.9rem;">
        🚀 Versão 2.0 | Desenvolvido por <strong>Raiza</strong><br>
        📧 bi@raizaeducacao.com.br | 📞 (21) 98905-9301
    </p>
    <div style="margin-top: 10px;">
        <img src="https://img.icons8.com/fluency/48/000000/instagram-new.png" style="margin: 0 10px; height: 32px;">
        <img src="https://img.icons8.com/color/48/000000/facebook.png" style="margin: 0 10px; height: 32px;">
    </div>
</div>
""", unsafe_allow_html=True)
