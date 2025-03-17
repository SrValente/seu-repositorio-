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
    /* ... (mantido o mesmo CSS anterior) ... */
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

# Grid de Cards
col1, col2, col3, col4 = st.columns(4)  # Alterado para 4 colunas

with col1:
    # Card Ocorrências (mantido igual)
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">📋 Registro de Ocorrências</div>
            <div class="card-description">
                Registre e acompanhe incidentes escolares com detalhamento completo:<br><br>
                • Acesse o histórico dos alunos<br>
                • Registro de novas ocorrências<br>
                • Download de histórico disponível
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_ocorrencias"):
        st.switch_page("pages/1_📋_Ocorrências.py")

with col2:
    # Card Grade Horária (mantido igual)
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">🕒 Grade Horária Inteligente</div>
            <div class="card-description">
                Controle completo da grade curricular:<br><br>
                • Visualização por turma/professor<br>
                • Integração com o TOTVS<br>
                • Exportação para PDF<br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_grade"):
        st.switch_page("pages/2_🕒_Grade_Horária.py")

with col3:
    # Card Faltas (mantido igual)
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">📅 Gestão de Frequência</div>
            <div class="card-description">
                Sistema completo de controle de presenças:<br><br>
                • Lançamento de faltas em massa<br>
                • Relatórios automáticos<br>
                • Integração com TOTVS<br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_faltas"):
        st.switch_page("pages/3_📅_Lançamento_Faltas.py")

with col4:
    # Novo Card Notas
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">✏️ Gestão de Notas</div>
            <div class="card-description">
                Sistema completo para lançamento e acompanhamento:<br><br>
                • Lançamento de notas por disciplina<br>
                • Cálculo automático de médias<br>
                • Relatórios de desempenho<br>
                • Integração com TOTVS
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar Módulo", key="btn_notas"):
        st.switch_page("pages/4_✏️_Notas.py")

# Footer (mantido igual)
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #6b7280;">
    <p style="font-size: 0.9rem;">
        🚀 Versão 2.0 | Desenvolvido por <strong>BI</strong><br>
        📧 bi@raizaeducacao.com.br | 📞 (21) 98905-9301
    </p>
</div>
""", unsafe_allow_html=True)
