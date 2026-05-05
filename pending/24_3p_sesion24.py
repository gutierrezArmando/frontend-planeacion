import streamlit as st
import streamlit.components.v1 as components

st.title("🔍 Sesión 24: Taller de Depuración Avanzada")
st.subheader("Herramientas de Diagnóstico para Ingenieros")

# --- BLOQUE DE MERMAID ---
mermaid_code = """
graph LR
    Log[console.log] --> Level1[Nivel Básico]
    Watch[Watch Expressions] --> Level2[Nivel Intermedio]
    Break[Breakpoints / Step Into] --> Level3[Nivel Pro]
"""

# Configuración robusta para evitar errores de llaves
mermaid_config = "{ startOnLoad: true, theme: 'neutral' }"

st.write("### Niveles de Depuración")
components.html(
    f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {mermaid_code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({mermaid_config});
    </script>
    """,
    height=300,
)

# --- GUÍA TÉCNICA ---
st.header("1. El Poder del Breakpoint")
st.write("En lugar de llenar tu código de logs, usa la palabra reservada 'debugger' o haz clic en el número de línea en la pestaña Sources.")

st.code("""
const procesarDatos = (data) => {
    // El navegador pausará aquí automáticamente
    debugger; 
    
    const resultado = data.map(item => item.titulo.toUpperCase());
    return resultado;
};
""", language="javascript")

st.divider()

st.header("2. Inspección de Red (Network)")
st.write("Esencial para validar la integración con tu API de Django[cite: 1, 2].")

st.info("""
**Qué revisar en la pestaña Network:**
*   **Status:** ¿Es 200 (OK) o 403 (CSRF Error)?[cite: 1, 2]
*   **Payload:** ¿Qué datos le estoy enviando a Django en el POST?[cite: 1]
*   **Preview/Response:** ¿Qué JSON me está regresando exactamente el servidor?[cite: 1]
""")

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Oráculo de Errores")
st.info("La IA puede predecir errores antes de que ocurran.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un desarrollador Senior. Tengo el siguiente error en mi consola de Chrome: "Uncaught (in promise) TypeError: Cannot read properties of undefined (reading 'map')". Analiza mi código de Fetch y explícame por qué ocurre esto cuando la API de Django tarda en responder o devuelve un objeto vacío.'*[cite: 1]
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Evaluación Final)")
st.markdown("""
1.  **Proyecto Final**: Asegúrate de que todas las funcionalidades (CRUD) de tu Backend de Django estén operativas[cite: 1, 2].
2.  **Repaso**: Revisa que tu Frontend use **Bootstrap** para la estética, **Fetch** para los datos y **LocalStorage** para las preferencias[cite: 1].
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cómo puedo hacer un despliegue (deploy) básico de mi frontend y mi backend para que otros puedan verlo fuera de mi localhost?"*
""")