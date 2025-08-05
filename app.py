import streamlit as st

# Configuración
st.set_page_config(page_title="Skill Builder", layout="centered")

# Título principal
st.markdown("<h1 style='color:#1a73e8;'>🧪 Skills Builder in Organic Chemistry</h1>", unsafe_allow_html=True)

st.markdown("---")

# Subtítulo para Topic 1
st.subheader("📘 Topic 1: Molecular Representations")
st.markdown("Este módulo te ayuda a dominar representaciones moleculares clave: estructuras de Lewis, ángulos de enlace, representaciones en 3D, etc.")

st.markdown("[Ir a Topic 1 👉](./Tema1)")

# Separador
st.markdown("---")

# Subtítulo para Topic 2
st.subheader("📗 Topic 2: Chemical Reactivity and Mechanisms")
st.markdown("Este módulo cubre aspectos como mecanismos de reacción, transferencia de electrones, intermedios reactivos y más.")

st.markdown("[Ir a Topic 2 👉](./topic2)")
