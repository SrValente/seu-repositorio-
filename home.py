import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Raiza - Gestão Escolar",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo: vídeo no topo fixo + container com margem
st.markdown("""
<style>
    .video-bg {
        position: absolute;
        top: 0;
        left: 0;
        width: 100vw;
        height: 400px;
        object-fit: cover;
        z-index: -1;
        pointer-events: none;
    }

    .main {
        margin-top: 380px;
    }

    .header-overlay {
        position: absolute;
        top: 60px;
        width: 100%;
        text-align: center;
        z-index: 1;
    }

    .header-overlay h1 {
        color: white;
        font-size: 3rem;
        font-weight: 700;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7);
    }

    .header-overlay h3 {
        color: white;
        font-weight: 400;
        text-shadow: 1px 1px 6px rgba(0, 0, 0, 0.5);
    }

    .card {
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        margin-bottom: 25px;
        overflow: hidden;
        border: 1px solid #ddd;
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

<video class="video-bg" autoplay muted loop playsinline>
    <source src="static/Raiza fundo branco.mp4" type="video/mp4">
</video>

<div class="header-overlay">
    <h1>Bem-vindo à Raiza</h1>
    <h3>Sua solução integrada de gestão escolar</h3>
</div>
""", unsafe_allow_html=True)

# ⬇️ Conteúdo principal com margem após o vídeo
st.markdown('<div class="main">', unsafe_allow_html=True)

# Seção 1: Ocorrências e Notas
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">🗉️ Registro de Ocorrências</div>
            <div class="card-description">
                Registre e acompanhe incidentes escolares:<br><br>
                • Histórico completo de alunos<br>
                • Lançamento de ocorrências<br>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_ocorrencias"):
        st.switch_page("pages/1_📋_Ocorrências.py")

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">✏️ Gestão de Notas</div>
            <div class="card-description">
                Sistema completo de avaliação:<br><br>
                • Lançamento por disciplina<br>
                • Análise de desempenho
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_notas"):
        st.switch_page("pages/4_✏️_Notas.py")

# Seção 2: Grade Horária, Faltas, Planos
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">🕒 Grade Horária</div>
            <div class="card-description">
                Gestão inteligente de horários:<br><br>
                • Visualização integrada<br>
                • Exportação automática
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_grade"):
        st.switch_page("pages/2_🕒_Grade_Horária.py")

with col4:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">🗓 Gestão de Frequência</div>
            <div class="card-description">
                Controle de presenças integrado:<br><br>
                • Lançamento em massa<br>
                • Lançamento retroativo
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_faltas"):
        st.switch_page("pages/3_📅_Lançamento_Faltas.py")

with col5:
    st.markdown("""
    <div class="card">
        <div class="card-content">
            <div class="card-title">🛂 Consulta de Planos</div>
            <div class="card-description">
                Acesse informações sobre planos educacionais:<br><br>
                • Visualização dos alunos aderentes<br>
                • Exportação de listas
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_planos"):
        st.switch_page("pages/5_🗂️_Consulta_Planos.py")

# Seção 3: Central do Aluno
st.markdown("""
<div class="card">
    <div class="card-content">
        <div class="card-title">💎 Central do Aluno (EM BREVE)</div>
        <div class="card-description">
            Portal completo para gestão de informações estudantis:<br><br>
            • Consulta de dados cadastrais<br>
            • Histórico escolar completo<br>
            • Notas online atualizadas<br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
if st.button("Acessar Central do Aluno", key="btn_central"):
    st.switch_page("pages/0_👤_Central_Aluno.py")

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

# ⬆️ Fecha div principal
st.markdown('</div>', unsafe_allow_html=True)
