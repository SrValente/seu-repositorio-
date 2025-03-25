import streamlit as st

# 1. Configuração crítica da página
st.set_page_config(
    page_title="Raiza - Gestão Escolar",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed",
    initial_sidebar_state="collapsed",
)

# 2. CSS otimizado com fallbacks
st.markdown("""
<style>
    /* Reset radical do fundo do Streamlit */
    .stApp {
        background: transparent !important;
        overflow: hidden !important;
    }

    /* Container do vídeo com hack de posicionamento */
    #raiza-video-bg {
        position: fixed;
        top: -70px;
        left: -10%;
        width: 120%;
        height: 120vh;
        z-index: -99999;
        overflow: hidden;
        transform: scale(1.05);
        filter: contrast(1.1) brightness(0.98);
    }

    /* Iframe do YouTube com políticas de autoplay */
    #raiza-video-bg iframe {
        width: 100%;
        height: 100%;
        border: none;
        pointer-events: none;
        transform: scale(1.15);
    }

    /* Camada de conteúdo interativo */
    .content-overlay {
        position: relative;
        z-index: 99999;
        background: linear-gradient(rgba(0,0,0,0.001), rgba(0,0,0,0.001));
        min-height: 100vh;
    }

    /* Header com tipografia reforçada */
    .raiza-header {
        text-align: center;
        padding: 9rem 0 4rem;
    }

    .raiza-header h1 {
        color: white !important;
        font-size: 5rem !important;
        font-weight: 900 !important;
        text-shadow: 0 12px 30px rgba(0,0,0,0.8) !important;
        letter-spacing: -1.5px !important;
    }

    /* Cards com efeito vidro otimizado */
    .glass-card {
        background: rgba(255,255,255,0.97) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,0.35) !important;
        box-shadow: 0 12px 40px rgba(0,0,0,0.15) !important;
        transition: all 0.4s cubic-bezier(0.25,0.8,0.25,1) !important;
    }

    .glass-card:hover {
        transform: translateY(-8px) scale(1.02) !important;
        box-shadow: 0 20px 60px rgba(0,0,0,0.25) !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Estrutura HTML/Javascript
st.markdown("""
<div id="raiza-video-bg">
    <iframe src="https://www.youtube-nocookie.com/embed/Hy-vN2uOLrY?autoplay=1&mute=1&controls=0&loop=1&playlist=Hy-vN2uOLrY&modestbranding=1&rel=0&enablejsapi=1&iv_load_policy=3&playsinline=1" 
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
    </iframe>
</div>

<div class="content-overlay">
    <div class="raiza-header">
        <h1>Bem-vindo à Raiza</h1>
        <h3 style="color: #f0f0f0; font-size: 1.8rem; margin-top: 1rem;">Sua solução integrada de gestão escolar</h3>
    </div>
""", unsafe_allow_html=True)

# 4. Conteúdo Principal
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card">
        <div style="padding: 2rem;">
            <div style="font-size: 1.6rem; color: #1f2937; border-bottom: 2px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                🗉️ Registro de Ocorrências
            </div>
            <div style="color: #6b7280; line-height: 1.7;">
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
    <div class="glass-card">
        <div style="padding: 2rem;">
            <div style="font-size: 1.6rem; color: #1f2937; border-bottom: 2px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                ✏️ Gestão de Notas
            </div>
            <div style="color: #6b7280; line-height: 1.7;">
                Sistema completo de avaliação:<br><br>
                • Lançamento por disciplina<br>
                • Análise de desempenho
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_notas"):
        st.switch_page("pages/4_✏️_Notas.py")

# Seção 2
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown("""
    <div class="glass-card">
        <div style="padding: 2rem;">
            <div style="font-size: 1.6rem; color: #1f2937; border-bottom: 2px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                🕒 Grade Horária
            </div>
            <div style="color: #6b7280; line-height: 1.7;">
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
    <div class="glass-card">
        <div style="padding: 2rem;">
            <div style="font-size: 1.6rem; color: #1f2937; border-bottom: 2px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                🗓 Gestão de Frequência
            </div>
            <div style="color: #6b7280; line-height: 1.7;">
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
    <div class="glass-card">
        <div style="padding: 2rem;">
            <div style="font-size: 1.6rem; color: #1f2937; border-bottom: 2px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1.5rem;">
                🛂 Consulta de Planos
            </div>
            <div style="color: #6b7280; line-height: 1.7;">
                Acesse informações sobre planos educacionais:<br><br>
                • Visualização dos alunos aderentes<br>
                • Exportação de listas
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Acessar Módulo", key="btn_planos"):
        st.switch_page("pages/5_🗂️_Consulta_Planos.py")

# Seção 3
st.markdown("""
<div class="glass-card" style="margin-top: 2rem;">
    <div style="padding: 2rem;">
        <div style="font-size: 1.6rem; color: #1f2937; border-bottom: 2px solid #e5e7eb; padding-bottom: 1rem; margin-bottom: 1.5rem;">
            💎 Central do Aluno (EM BREVE)
        </div>
        <div style="color: #6b7280; line-height: 1.7;">
            Portal completo para gestão de informações estudantis:<br><br>
            • Consulta de dados cadastrais<br>
            • Histórico escolar completo<br>
            • Notas online atualizadas<br>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 3rem 0; color: #6b7280;">
    <p style="font-size: 0.95rem;">
        🚀 Versão 2.2 | Desenvolvido por <strong>BI Raiza</strong><br>
        📧 bi@raizaeducacao.com.br | 📞 (21) 98905-9301
    </p>
</div>
</div>  <!-- Fecha content-overlay -->
""", unsafe_allow_html=True)

# Script final para garantir autoplay
st.markdown("""
<script>
document.addEventListener('click', function() {
    const iframe = document.querySelector('#raiza-video-bg iframe');
    iframe.src += '&autoplay=1';
}, {once: true});
</script>
""", unsafe_allow_html=True)
