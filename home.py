import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Raiza - Gestão Escolar",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS completo com efeito Siri
st.markdown("""
<style>
    /* Container do vídeo YouTube */
    .yt-bg {
        position: fixed;
        top: -60px;
        left: -10%;
        width: 120%;
        height: 120vh;
        z-index: -1000;
        overflow: hidden;
        transform: scale(1.1);
        filter: brightness(0.95);
    }

    /* Iframe responsivo */
    .yt-bg iframe {
        width: 100%;
        height: 100%;
        border: none;
        pointer-events: none;
    }

    /* Efeito de overlay dinâmico */
    .header-overlay {
        position: relative;
        z-index: 1000;
        padding: 8rem 0 3rem;
        text-align: center;
        background: linear-gradient(rgba(0,0,0,0.3), transparent 90%);
    }

    .header-overlay h1 {
        color: white !important;
        font-size: 4.5rem !important;
        font-weight: 800 !important;
        text-shadow: 0 8px 24px rgba(0,0,0,0.5) !important;
        margin: 0 !important;
    }

    .header-overlay h3 {
        color: #f3f4f6 !important;
        font-size: 1.8rem !important;
        font-weight: 300 !important;
        text-shadow: 0 4px 12px rgba(0,0,0,0.4) !important;
        margin-top: 1rem !important;
    }

    /* Cards com efeito de vidro */
    .card {
        background: rgba(255,255,255,0.96) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.3) !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1) !important;
        transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
    }

    .card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 12px 48px rgba(0,0,0,0.15) !important;
    }

    .card-title {
        color: #1f2937 !important;
        font-size: 1.6rem !important;
        padding-bottom: 12px !important;
        border-bottom: 2px solid #e5e7eb;
    }

    /* Botões estilizados */
    .stButton > button {
        background: rgba(59,130,246,0.9) !important;
        backdrop-filter: blur(4px);
        border-radius: 12px !important;
        padding: 14px 28px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: rgba(37,99,235,0.95) !important;
        transform: scale(1.05);
    }
</style>

<div class="yt-bg">
    <iframe src="https://www.youtube.com/embed/Hy-vN2uOLrY?autoplay=1&mute=1&controls=0&loop=1&playlist=Hy-vN2uOLrY&modestbranding=1&showinfo=0&rel=0&enablejsapi=1" 
            allow="autoplay; encrypted-media" 
            allowfullscreen>
    </iframe>
</div>

<div class="header-overlay">
    <h1>Bem-vindo à Raiza</h1>
    <h3>Sua solução integrada de gestão escolar</h3>
</div>
""", unsafe_allow_html=True)

# Seção 1: Módulos Principais
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

# Seção 2: Ferramentas Complementares
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

# Seção 3: Novidades
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
<div style="text-align: center; padding: 2rem; color: #6b7280;">
    <p style="font-size: 0.95rem;">
        🚀 Versão 2.1 | Desenvolvido por <strong>BI Raiza</strong><br>
        📧 bi@raizaeducacao.com.br | 📞 (21) 98905-9301
    </p>
</div>
""", unsafe_allow_html=True)
