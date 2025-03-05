import streamlit as st

st.set_page_config(
    page_title="Raiza",
    page_icon="🏫",
    layout="centered"
)

st.title("🏫 Sistema de Gestão Escolar")
st.markdown("---")

# Cards de navegação
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📋 Ocorrências", use_container_width=True):
        st.switch_page("1_📋_Ocorrências.py")

with col2:
    if st.button("🕒 Grade Horária", use_container_width=True):
        st.switch_page("2_🕒_Grade_Horária.py")

with col3:
    if st.button("📅 Lançamento de Faltas", use_container_width=True):
        st.switch_page("3_📅_Lançamento_Faltas.py")

st.markdown("---")
st.caption("Sistema integrado - Todos os módulos em uma única plataforma")
