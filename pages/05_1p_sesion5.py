import streamlit as st
import streamlit.components.v1 as components

st.title("📐 Sesión 5: Layouts con CSS Grid")
st.subheader("Arquitectura de Rejillas Bidimensionales")

# --- SECCIÓN 1: DEFINICIÓN DE COLUMNAS Y FILAS ---
st.header("1. El Poder de la Fracción (fr)")
st.write("En Grid, usamos la unidad `fr` para representar una fracción del espacio disponible, lo que hace que el diseño sea intrínsecamente flexible.")

st.code("""
.contenedor-grid {
    display: grid;
    /* Crea 3 columnas: una fija de 200px y dos que se reparten el resto */
    grid-template-columns: 200px 1fr 2fr;
    /* Crea 2 filas de 100px y una automática */
    grid-template-rows: 100px 100px auto;
    gap: 20px; /* Espaciado entre celdas */
}
""", language="css")

st.divider()

# --- SECCIÓN 2: GRID TEMPLATE AREAS ---
st.header("2. Dibujando el Layout (Áreas)")
st.write("Podemos nombrar secciones de nuestra rejilla para que el código sea casi visual[cite: 31].")

st.code("""
.layout-dashboard {
    display: grid;
    grid-template-areas: 
        "header header header"
        "nav main aside"
        "footer footer footer";
    grid-template-columns: 1fr 3fr 1fr;
}

header { grid-area: header; }
main { grid-area: main; }
/* ... así con cada sección ... */
""", language="css")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Planificador de Grillas")
st.info("Pide a la IA que cree una estructura responsiva sin usar Media Queries:")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en CSS. Explícame cómo funciona la función repeat(auto-fit, minmax(200px, 1fr)) y genera un código para una galería de imágenes que se ajuste sola según el tamaño de la pantalla sin usar media queries.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 6)")
st.markdown("""
1.  **Juego Interactivo:** Supera los primeros niveles de [Grid Garden](https://cssgridgarden.com/#es) para practicar la sintaxis de forma visual.
2.  **Investigación:** ¿Qué es un **Framework de CSS** y por qué Bootstrap 5 es el más popular del mundo?[cite: 31]
3.  **Reflexión:** Si ya tenemos Flexbox y Grid, ¿qué ventaja nos da usar Bootstrap en lugar de escribir todo nuestro CSS desde cero?
""")