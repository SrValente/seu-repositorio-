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
    .card {
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        margin-bottom: 25px;
        overflow: hidden;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
    }
    .card-content {
        padding: 25px;
    }
    .card-title {
        font-size: 1.4rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 15px;
    }
    .card-description {
        font-size: 0.95rem;
        color: #6b7280;
        line-height: 1.6;
    }
    .stButton>button {
        width: 100%;
        background: #3b82f6 !important;
        color: white !important;
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Conteúdo Principal
st.title("🏫 Bem-vindo à Raiza")
st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h3 style="color: #4b5563; font-weight: 400;">
            Plataforma Integrada de Gestão Escolar
        </h3>
    </div>
""", unsafe_allow_html=True)

# Grid de Cards para Navegação
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">📋 Registro de Ocorrências</div>
            <div class="card-description">
                Registre e acompanhe incidentes escolares:<br><br>
                • Histórico completo de alunos<br>
                • Sistema de classificação<br>
                • Relatórios personalizados
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_ocorrencias"):
        st.experimental_set_query_params(page="📋 Registro de Ocorrências")

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">🕒 Grade Horária</div>
            <div class="card-description">
                Gestão inteligente de horários:<br><br>
                • Visualização integrada<br>
                • Alocação de professores<br>
                • Exportação automática
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_grade"):
        st.experimental_set_query_params(page="🕒 Grade Horária")

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">📅 Gestão de Frequência</div>
            <div class="card-description">
                Controle de presenças integrado:<br><br>
                • Lançamento em massa<br>
                • Alertas automáticos<br>
                • Relatórios por período
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_faltas"):
        st.experimental_set_query_params(page="📅 Gestão de Frequência")

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">✏️ Gestão de Notas</div>
            <div class="card-description">
                Sistema completo de avaliação:<br><br>
                • Lançamento por disciplina<br>
                • Cálculo de médias<br>
                • Análise de desempenho
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_notas"):
        st.experimental_set_query_params(page="✏️ Gestão de Notas")

with col5:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">💳 Consulta de Planos</div>
            <div class="card-description">
                Visualize e gerencie os planos de pagamento:<br><br>
                • Consulta de planos disponíveis<br>
                • Detalhamento de pagamentos<br>
                • Atualizações e ajustes
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_planos"):
        st.experimental_set_query_params(page="💳 Consulta de Planos")

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
