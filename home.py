import streamlit as st

# ================ CONFIGURAÇÃO DA PÁGINA ================
st.set_page_config(
    page_title="Raiza - Gestão Escolar",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)

# ================ COMPONENTE DE VÍDEO ================
st.html(f"""
<iframe id="raiza-video-bg"
    style="
        position: fixed;
        top: -70px;
        left: 0;
        width: 100vw;
        height: 120vh;
        z-index: -2147483647;
        transform: scale(1.1);
        filter: brightness(0.98) contrast(1.05);
        pointer-events: none;
        border: none;
    "
    src="https://www.youtube-nocookie.com/embed/Hy-vN2uOLrY?autoplay=1&mute=1&controls=0&loop=1&playlist=Hy-vN2uOLrY&modestbranding=1&rel=0&enablejsapi=1&iv_load_policy=3&playsinline=1&widgetid=3" 
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>
""")

# ================ ESTILOS GLOBAIS ================
st.markdown("""
<style>
    /* Reset do Streamlit */
    .stApp {
        background: transparent !important;
        overflow: hidden !important;
    }

    /* Estrutura principal */
    .content-layer {
        position: relative;
        z-index: 2147483647;
        min-height: 100vh;
        background: linear-gradient(rgba(0,0,0,0.001), rgba(0,0,0,0.001));
    }

    /* Header */
    .raiza-header {
        text-align: center;
        padding: 8rem 0 4rem;
    }

    .raiza-header h1 {
        color: white !important;
        font-size: 4.5rem !important;
        font-weight: 900 !important;
        text-shadow: 0 8px 24px rgba(0,0,0,0.8) !important;
        letter-spacing: -1.5px !important;
        margin: 0 !important;
    }

    /* Cards */
    .glass-card {
        background: rgba(255,255,255,0.97) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,0.35) !important;
        border-radius: 15px !important;
        box-shadow: 0 12px 40px rgba(0,0,0,0.15) !important;
        transition: all 0.4s cubic-bezier(0.25,0.8,0.25,1) !important;
        margin-bottom: 2rem !important;
        overflow: hidden !important;
    }

    .glass-card:hover {
        transform: translateY(-8px) scale(1.02) !important;
        box-shadow: 0 20px 60px rgba(0,0,0,0.25) !important;
    }

    /* Botões */
    .stButton > button {
        width: 100% !important;
        background: rgba(59,130,246,0.9) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 28px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background: rgba(37,99,235,0.95) !important;
        transform: scale(1.05) !important;
    }
</style>
""", unsafe_allow_html=True)

# ================ CONTEÚDO PRINCIPAL ================
with st.container():
    st.markdown("""
    <div class="content-layer">
        <div class="raiza-header">
            <h1>Bem-vindo à Raiza</h1>
            <h3 style="color: #f0f0f0; font-size: 1.8rem; margin-top: 1rem;">Sua solução integrada de gestão escolar</h3>
        </div>
    """, unsafe_allow_html=True)

    # Seção 1: Módulos Principais
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
        st.button("Acessar Módulo", key="btn_ocorrencias")

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
        st.button("Acessar Módulo", key="btn_notas")

    # Seção 2: Módulos Secundários
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
        st.button("Acessar Módulo", key="btn_grade")

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
        st.button("Acessar Módulo", key="btn_faltas")

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
        st.button("Acessar Módulo", key="btn_planos")

    # Seção 3: EM BREVE
    st.markdown("""
    <div class="glass-card">
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
            🚀 Versão 2.4 | Desenvolvido por <strong>BI Raiza</strong><br>
            📧 bi@raizaeducacao.com.br | 📞 (21) 98905-9301
        </p>
    </div>
    </div> <!-- Fecha content-layer -->
    """, unsafe_allow_html=True)

# ================ SCRIPTS FINAIS ================
st.html("""
<script>
document.addEventListener('DOMContentLoaded', function() {
    const videoFrame = document.getElementById('raiza-video-bg');
    
    function updateVideoSource() {
        const newSrc = videoFrame.src.replace('autoplay=0', 'autoplay=1') + '&mute=1';
        videoFrame.src = newSrc;
        videoFrame.contentWindow.postMessage('{"event":"command","func":"playVideo","args":""}', '*');
    }

    document.body.addEventListener('click', updateVideoSource, {once: true});
    document.body.addEventListener('touchstart', updateVideoSource, {once: true});
    
    // Controle de redimensionamento
    function resizeVideo() {
        const aspectRatio = 16/9;
        const windowWidth = window.innerWidth;
        const windowHeight = window.innerHeight;
        
        if (windowWidth / windowHeight > aspectRatio) {
            videoFrame.style.width = "100vw";
            videoFrame.style.height = (windowWidth / aspectRatio) + "px";
        } else {
            videoFrame.style.height = "120vh";
            videoFrame.style.width = (windowHeight * aspectRatio) + "px";
        }
    }
    
    window.addEventListener('resize', resizeVideo);
    resizeVideo();
});
</script>
""")
