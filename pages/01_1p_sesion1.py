import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🌐 Sesión 1: El Ecosistema Frontend")

# --- SECCIÓN: EL ROL DEL NAVEGADOR (Visualización Mermaid) ---
st.header("1. El Ciclo de Vida en el Navegador")
st.write("""
Como ingenieros, debemos entender qué sucede una vez que el servidor Django 
envía la respuesta. Este proceso se llama **Critical Rendering Path**.
""")

# Definición del diagrama en Mermaid
mermaid_code = """
graph TD
    A[Usuario escribe URL] -- Petición HTTP --> B[Servidor Django]
    B -- Retorna Documentos .html, .css, .js --> C{Navegador}
    C --> D[DOM Tree: Estructura HTML]
    C --> E[CSSOM Tree: Estilos CSS]
    D & E --> F[Render Tree]
    F --> G[Layout: Cálculo de posiciones]
    G --> H[Paint: Pintado de píxeles]
    H --> I[Ejecución de JavaScript]
    
    style B fill:#f96,stroke:#333
    style C fill:#69f,stroke:#333
    style I fill:#f9f,stroke:#333
"""
st.code(body=mermaid_code, language="mermaid")

# Renderizado del diagrama usando HTML/JavaScript
components.html(
    f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {mermaid_code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    """,
    height=800,
)

st.divider()

# --- SECCIÓN IA ---
st.header("🤖 Laboratorio de IA: El Traductor de Estándares")
st.info("Utiliza Gemini o ChatGPT con el siguiente prompt para iniciar el debate:")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en motores de renderizado. Explícame de forma técnica pero sencilla qué es el Critical Rendering Path y por qué optimizarlo hace que mi frontend se sienta más rápido.'*
""")

# --- SECCIÓN TICs ---
st.header("🛠️ TICs: El Kit de Ingeniería")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Herramientas de Estándar Industrial:**
    *   **Editor:** VS Code + Live Server.
    *   **Debugger:** Chrome DevTools (F12).
    *   **Estándares:** W3C (HTML5 / CSS3).
    """)
with col2:
    # Simulación de renderizado visual
    st.code("""
    <!-- Estructura básica que el navegador interpreta -->
    <!DOCTYPE html>
    <html>
      <head><title>Mi App</title></head>
      <body><h1>Hola Mundo</h1></body>
    </html>
    """, language="html")

st.divider()

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 2)")
st.markdown("""
1.  **Investigación:** ¿Cuál es la diferencia entre una etiqueta `<div>` y una etiqueta `<section>`? 
2.  **Práctica:** Asegúrate de tener instalada la extensión **Live Server** en VS Code.
3.  **Reflexión:** Investiga qué es el **SEO** y por qué el uso correcto de HTML ayuda a que una página aparezca primero en Google.
""")