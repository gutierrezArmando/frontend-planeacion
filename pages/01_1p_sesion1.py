import streamlit as st

st.title("🌐 Sesión 1: El Ecosistema Frontend")

# --- SECCIÓN TICs ---
st.header("🛠️ TICs: El Kit de Ingeniería")
st.write("Para esta asignatura utilizaremos herramientas de estándar industrial:")
st.markdown("""
*   **Editor:** VS Code con extensiones (Live Server, Prettier).
*   **Debugger:** Chrome DevTools (F12).
*   **Versión:** Git y GitHub para el control de versiones de sus plantillas.
""")

st.divider()

# --- SECCIÓN IA ---
st.header("🤖 Laboratorio de IA: El Traductor de Estándares")
st.info("Utiliza Gemini o ChatGPT con el siguiente prompt para iniciar el debate:")
st.markdown("> *'Actúa como un experto en motores de renderizado. Explícame de forma técnica pero sencilla qué es el Critical Rendering Path y por qué optimizarlo hace que mi frontend se sienta más rápido.'*")

st.divider()

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 2)")
st.markdown("""
Antes de la próxima clase, realiza lo siguiente:
1.  **Investigación:** ¿Cuál es la diferencia entre una etiqueta `<div>` y una etiqueta `<section>`? 
2.  **Práctica:** Instala la extensión **Live Server** en tu VS Code.
3.  **Reflexión:** Investiga qué es el **SEO** y por qué el uso correcto de HTML ayuda a que una página aparezca primero en Google.
""")