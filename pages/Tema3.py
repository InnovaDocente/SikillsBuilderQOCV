import streamlit as st
import pandas as pd
import os
from streamlit_ketcher import st_ketcher
from streamlit_quill import st_quill

st.set_page_config(page_title="Topic 1", layout="wide")

# Cargar CSS personalizado
def cargar_css_local(ruta_css):
    with open(ruta_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

cargar_css_local("assets/css/style.css")

# Cargar el Excel con las habilidades y ejercicios
@st.cache_data
def cargar_datos():
    df = pd.read_excel("skills.xlsx")
    df['Skills'] = df['Skills'].str.strip()
    return df

# Mostrar múltiples imágenes (solo para Builder)
def mostrar_imagenes(path_str: str, caption_base: str, multiple=False):
    if not isinstance(path_str, str):
        return
    paths = [p.strip() for p in path_str.split(";")] if multiple else [path_str.strip()]
    for idx, path in enumerate(paths):
        if os.path.exists(path):
            caption = f"{caption_base} ({idx + 1})" if multiple and len(paths) > 1 else caption_base
            st.image(path, use_container_width=True, caption=caption)
        else:
            st.warning(f"No se encontró la imagen: {path}")

df = cargar_datos()

# HABILIDAD
st.markdown("<div class='titulo-primario'>Habilidad</div>", unsafe_allow_html=True)
habilidades_opciones = ["Selecciona una habilidad"] + sorted(df['Skills'].unique())
habilidad_seleccionada = st.selectbox("", habilidades_opciones, index=0)

if habilidad_seleccionada != "Selecciona una habilidad":
    df_filtrado = df[df['Skills'] == habilidad_seleccionada]

    # BUILDER
    st.markdown("<div class='titulo-secundario'>Esquema visual de la habilidad</div>", unsafe_allow_html=True)
    builder_path = df_filtrado.iloc[0]['Builder']
    mostrar_imagenes(builder_path, "Builder", multiple=True)

    # EJERCICIO PRÁCTICO
    st.markdown("<div class='titulo-primario'>Ejercicio práctico</div>", unsafe_allow_html=True)
    ej_practicos = df_filtrado[['ExercicePr', 'Practice']].drop_duplicates()
    ejercicios_practicos_opciones = ["Selecciona un ejercicio práctico"] + ej_practicos['ExercicePr'].tolist()
    ejercicio_pr = st.selectbox("", ejercicios_practicos_opciones, index=0)

    if ejercicio_pr != "Selecciona un ejercicio práctico":
        fila_practica = ej_practicos[ej_practicos['ExercicePr'] == ejercicio_pr].iloc[0]

        # Editor antes de ver solución
        st.markdown("<div class='titulo-secundario'>Dibuja tu solución</div>", unsafe_allow_html=True)
        mol = st_ketcher(height=400)

        if mol:
            st.success("Molécula dibujada. Puedes comparar con la solución oficial.")
            st.markdown("<div class='titulo-secundario'>Solución del ejercicio práctico</div>", unsafe_allow_html=True)
            mostrar_imagenes(fila_practica['Practice'], ejercicio_pr, multiple=False)
        else:
            st.info("Dibuja la estructura antes de ver la solución del ejercicio.")

    # EJERCICIO APLICADO
    st.markdown("<div class='titulo-primario'>Ejercicio aplicado</div>", unsafe_allow_html=True)
    ej_aplicacion = df_filtrado[['ExerciceAp', 'Apply']].drop_duplicates()
    ejercicios_aplicados_opciones = ["Selecciona un ejercicio aplicado"] + ej_aplicacion['ExerciceAp'].tolist()
    ejercicio_ap = st.selectbox("", ejercicios_aplicados_opciones, index=0)

    if ejercicio_ap != "Selecciona un ejercicio aplicado":
        fila_aplicacion = ej_aplicacion[ej_aplicacion['ExerciceAp'] == ejercicio_ap].iloc[0]

        st.markdown("<div class='titulo-secundario'>Dibuja tu solución</div>", unsafe_allow_html=True)
        mol_ap = st_ketcher(key="aplicado", height=400)

        if mol_ap:
            st.success("Molécula dibujada. Puedes comparar con la solución oficial.")
            st.markdown("<div class='titulo-secundario'>Solución del ejercicio aplicado</div>", unsafe_allow_html=True)
            mostrar_imagenes(fila_aplicacion['Apply'], ejercicio_ap, multiple=False)
        else:
            st.info("Dibuja la estructura antes de ver la solución del ejercicio aplicado.")
