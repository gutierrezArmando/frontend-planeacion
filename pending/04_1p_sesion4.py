import streamlit as st
import streamlit.components.v1 as components

st.title("🧱 Sesión 4: Layouts con Flexbox")
st.subheader("Distribución Elástica y Alineación de Componentes")

# --- SECCIÓN 1: CONCEPTOS FUNDAMENTALES ---
st.header("1. El Contenedor y los Ítems")
st.write("Flexbox funciona bajo una jerarquía Padre-Hijo. Al activar `display: flex`, el contenedor toma el control de sus hijos directos.")

# Propiedades comunes
with st.expander("🔍 Propiedades del Contenedor (Padre)"):
    st.markdown("""
    *   **justify-content:** Alinea los hijos en el eje principal (inicio, fin, centro, espacio entre)[cite: 31].
    *   **align-items:** Alinea los hijos en el eje secundario (arriba, abajo, centro)[cite: 31].
    *   **flex-direction:** Define si los hijos se apilan en fila o columna[cite: 31].
    *   **flex-wrap:** Decide si los hijos saltan de línea cuando no caben[cite: 31].
    """)

st.divider()

# --- SECCIÓN 2: SIMULADOR DE CÓDIGO ---
st.header("2. Ejemplo Práctico: Centrado Perfecto")
st.write("El dolor de cabeza histórico de CSS se resuelve con 3 líneas en el padre[cite: 31]:")

st.code("""
.contenedor-padre {
    display: flex;
    justify-content: center; /* Centrado horizontal */
    align-items: center;     /* Centrado vertical */
    height: 100vh;           /* Altura de toda la pantalla */
}
""", language="css")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Arquitecto Flex")
st.info("Pide a la IA que te ayude a diseñar una estructura compleja:")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un desarrollador frontend senior. Necesito crear una barra de navegación que tenga: 
> 1. Un logo a la izquierda.
> 2. Un menú centrado.
> 3. Un botón de "Login" a la derecha. 
> Dame el código HTML y el CSS usando Flexbox, y explícame por qué usaste space-between o margin-auto.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 5)")
st.markdown("""
1.  **Juego Práctico:** Completa los primeros 10 niveles de [Flexbox Froggy](https://flexboxfroggy.com/#es). Es una excelente herramienta TIC para aprender jugando.
2.  **Investigación:** ¿Qué es **CSS Grid** y en qué se diferencia de Flexbox? (Pista: Una es para una dimensión y la otra para dos)[cite: 31].
3.  **Reflexión:** Si Flexbox alinea elementos en una fila, ¿cómo harías una cuadrícula de fotos como la de Instagram?
""")