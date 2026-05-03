import streamlit as st
import streamlit.components.v1 as components

st.title("🏆 Sesión 18: Evaluación Parcial 2")
st.subheader("Proyecto: 'La Gran Conexión' (Fullstack)")

# --- RÚBRICA DE EVALUACIÓN ---
st.header("1. Criterios de Evaluación")
st.write("Tu proyecto será evaluado bajo los siguientes estándares de ingeniería:")

col1, col2 = st.columns(2)
with col1:
    st.info("### 🛠️ Funcionalidad (60%)")
    st.markdown("""
    *   **Lectura (GET):** Listar datos reales de Django en Cards de Bootstrap.
    *   **Escritura (POST):** Crear registros desde un formulario JS.
    *   **CORS:** Configuración correcta de orígenes permitidos.
    """)
with col2:
    st.success("### 💻 Código y UX (40%)")
    st.markdown("""
    *   **Asincronía:** Uso correcto de `async/await` y `try/catch`.
    *   **DOM:** Renderizado dinámico sin recarga de página.
    *   **Feedback:** Mensajes de éxito o error para el usuario.
    """)

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 IA: Tu Consultora de Producción")
st.info("Usa la IA para optimizar la respuesta de tu aplicación.")
st.markdown("""
> **Prompt de apoyo:** 
> *'Actúa como un desarrollador Fullstack. Ya logré hacer el POST a mi API de Django, pero después de guardar quiero que la lista de tareas se actualice automáticamente sin usar window.location.reload(). ¿Cómo puedo encapsular mi lógica de GET en una función para llamarla justo después del éxito del POST?'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Hacia el Parcial 3)")
st.markdown("""
1.  **Investigación:** ¿Qué es un **Web Component** y cómo nos ayuda a encapsular HTML, CSS y JS?
2.  **Preparación:** En el siguiente parcial, daremos el salto a **React.js**. Investiga qué es el **Virtual DOM** y en qué se diferencia del DOM real que usamos hoy.
3.  **Reflexión IA:** Pregunta a la IA: *'¿Por qué las empresas prefieren frameworks como React o Vue en lugar de usar JavaScript Vanilla para proyectos grandes?'*
""")