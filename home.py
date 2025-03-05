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
        position: relative;
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
    
    /* Área clicável invisível */
    .clickable-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        cursor: pointer;
        z-index: 1;
    }
    
    /* Botão visual (apenas decorativo) */
    .decorative-button {
        position: relative;
        z-index: 0;
        width: 100%;
        border: none;
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white !important;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: 500;
        transition: all 0.3s ease;
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
    # Card Ocorrências
    st.markdown("""
    <div class="card">
        <div class="clickable-overlay"></div>
        <div>
            <div class="card-title">📋 Registro de Ocorrências</div>
            <div class="card-description">
                Registre e acompanhe incidentes escolares com detalhamento completo:
                - Classificação por tipo
                - Registro de envolvidos
                - Acompanhamento temporal
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão invisível para funcionalidade
    if st.button("Acessar Ocorrências", key="btn_ocorrencias"):
        st.switch_page("pages/1_📋_Ocorrências.py")

with col2:
    # Card Grade Horária
    st.markdown("""
    <div class="card">
        <div class="clickable-overlay"></div>
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
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Grade", key="btn_grade"):
        st.switch_page("pages/2_🕒_Grade_Horária.py")

with col3:
    # Card Faltas
    st.markdown("""
    <div class="card">
        <div class="clickable-overlay"></div>
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
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Faltas", key="btn_faltas"):
        st.switch_page("pages/3_📅_Lançamento_Faltas.py")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #6b7280;">
    <p style="font-size: 0.9rem;">
        🚀 Versão 2.0 | Desenvolvido por <strong>BI</strong><br>
        📧 bi@raizaeducacao.com.br | 📞 (21) 98905-9301
    </p>
</div>
""", unsafe_allow_html=True)
