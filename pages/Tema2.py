import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Topic 1", layout="wide")
st.markdown("<h1 style='color:#1a73e8;'>Topic 1 — Molecular Representations</h1>", unsafe_allow_html=True)

# Función para cargar hoja de estilos CSS externa
def cargar_css_local(ruta_css):
    """Carga un archivo CSS externo y lo inyecta en el documento Streamlit."""
    with open(ruta_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Cargar el archivo CSS ubicado en assets/css/style.css
cargar_css_local("assets/css/style.css")

@st.cache_data
def cargar_datos():
    df = pd.read_excel("skills.xlsx")
    df['Skills'] = df['Skills'].str.strip()
    return df

def mostrar_imagenes(path_str: str, caption_base: str, multiple=False):
    if not isinstance(path_str, str):
        st.info("No se proporcionó ruta de imagen.")
        return

    paths = [p.strip() for p in path_str.split(";")] if multiple else [path_str.strip()]
    cargada = False

    for idx, path in enumerate(paths):
        if os.path.exists(path):
            caption = f"{caption_base} ({idx + 1})" if multiple and len(paths) > 1 else caption_base
            st.image(path, use_container_width=True, caption=caption)
            cargada = True
        else:
            st.warning(f"No se encontró la imagen: {path}")
    
    if not cargada:
        st.info("No se pudo cargar ninguna imagen.")

df = cargar_datos()

# Paso 1: Seleccionar habilidad
habilidades = sorted(df['Skills'].unique())
habilidades_opciones = ["Selecciona una habilidad"] + habilidades
#habilidad_seleccionada = st.selectbox("Habilidad", habilidades_opciones, index=0)
st.markdown("<div class='titulo-secundario'>Habilidad</div>", unsafe_allow_html=True)
habilidad_seleccionada = st.selectbox("", habilidades_opciones, index=0)

if habilidad_seleccionada != "Selecciona una habilidad":
    df_filtrado = df[df['Skills'] == habilidad_seleccionada]

    # Paso 2: Mostrar esquema visual (Builder) — ahora permite múltiples imágenes
    builder_path = df_filtrado.iloc[0]['Builder']
    #st.subheader("Esquema visual de la habilidad")
    st.markdown("<div class='titulo-secundario'>Esquema visual de la habilidad</div>", unsafe_allow_html=True)
    mostrar_imagenes(builder_path, "Learn", multiple=True)

    # Paso 3: Seleccionar ejercicio práctico
    ej_practicos = df_filtrado[['ExercicePr', 'Practice']].drop_duplicates()
    ejercicios_practicos_opciones = ["Selecciona un ejercicio práctico"] + ej_practicos['ExercicePr'].tolist()
    ejercicio_pr = st.selectbox("Ejercicio práctico", ejercicios_practicos_opciones, index=0)

    if ejercicio_pr != "Selecciona un ejercicio práctico":
        fila_practica = ej_practicos[ej_practicos['ExercicePr'] == ejercicio_pr].iloc[0]
        #st.subheader("Solución del ejercicio práctico")
        st.markdown("<div class='titulo-secundario'>Solución del ejercicio práctico</div>", unsafe_allow_html=True)
        mostrar_imagenes(fila_practica['Practice'], ejercicio_pr, multiple=False)

    # Paso 4: Seleccionar ejercicio de aplicación
    ej_aplicacion = df_filtrado[['ExerciceAp', 'Apply']].drop_duplicates()
    ejercicios_aplicados_opciones = ["Selecciona un ejercicio aplicado"] + ej_aplicacion['ExerciceAp'].tolist()
    ejercicio_ap = st.selectbox("Ejercicio aplicado", ejercicios_aplicados_opciones, index=0)

    if ejercicio_ap != "Selecciona un ejercicio aplicado":
        fila_aplicacion = ej_aplicacion[ej_aplicacion['ExerciceAp'] == ejercicio_ap].iloc[0]
        #st.subheader("Solución del ejercicio de aplicación")
        st.markdown("<div class='titulo-secundario'>Solución del ejercicio de aplicación</div>", unsafe_allow_html=True)
        mostrar_imagenes(fila_aplicacion['Apply'], ejercicio_ap, multiple=False)

