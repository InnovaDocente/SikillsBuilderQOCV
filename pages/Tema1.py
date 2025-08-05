import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Topic 1", layout="wide")
st.markdown("<h1 style='color:#1a73e8;'>Topic 1 — Molecular Representations</h1>", unsafe_allow_html=True)

@st.cache_data
def cargar_datos():
    df = pd.read_excel("skills.xlsx")
    df['Skills'] = df['Skills'].str.strip()
    return df

def mostrar_imagen(path: str, caption: str):
    path = path.strip()
    if os.path.exists(path):
        st.image(path, use_container_width=True, caption=caption)
    else:
        st.warning(f"No se encontró la imagen: {path}")

df = cargar_datos()

# Paso 1: Seleccionar habilidad
habilidades = sorted(df['Skills'].unique())
habilidad_seleccionada = st.selectbox("Selecciona una habilidad", habilidades)

df_filtrado = df[df['Skills'] == habilidad_seleccionada]

if df_filtrado.empty:
    st.warning("No se encontraron datos para esta habilidad.")
    st.stop()

# Paso 2: Mostrar esquema visual (Builder)
builder_path = df_filtrado.iloc[0]['Builder']
st.subheader("Esquema visual de la habilidad")
mostrar_imagen(builder_path, "Builder")

# Paso 3: Seleccionar ejercicio práctico
ej_practicos = df_filtrado[['ExercicePr', 'Practice']].drop_duplicates()
ejercicio_pr = st.selectbox("Selecciona un ejercicio práctico", ej_practicos['ExercicePr'].unique())

fila_practica = ej_practicos[ej_practicos['ExercicePr'] == ejercicio_pr].iloc[0]
st.subheader("Solución del ejercicio práctico")
mostrar_imagen(fila_practica['Practice'], ejercicio_pr)

# Paso 4: Seleccionar ejercicio de aplicación
ej_aplicacion = df_filtrado[['ExerciceAp', 'Apply']].drop_duplicates()
ejercicio_ap = st.selectbox("Selecciona un ejercicio de aplicación", ej_aplicacion['ExerciceAp'].unique())

fila_aplicacion = ej_aplicacion[ej_aplicacion['ExerciceAp'] == ejercicio_ap].iloc[0]
st.subheader("Solución del ejercicio de aplicación")
mostrar_imagen(fila_aplicacion['Apply'], ejercicio_ap)
