import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("🌳 Sesión 11: Manipulación del DOM")
st.subheader("Selección, Modificación e Inyección de Elementos")

st.header("El Árbol del DOM")
st.write("Jerarquía padre-hijo")
mermaid_code ="""
graph TD
    A[Window] --> B[Document]
    B --> C[html]
    C --> D[head]
    C --> E[body]
    E --> F[header]
    E --> G[main]
    E --> H[footer]
    G --> I[section]
    I --> J[h2]
    I --> K[div#lista-tareas]
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
    height=600,
)

st.divider()

# --- SECCIÓN 1: SELECCIÓN DE ELEMENTOS ---
st.header("1. ¿Cómo encontrar elementos?")
st.write("Existen métodos modernos que funcionan de forma similar a los selectores de CSS que vimos en la Sesión 3.")

st.code("""
// Selección por ID
const titulo = document.getElementById('mi-titulo');

// Selección moderna (Recomendada)
const contenedor = document.querySelector('.container'); // Por clase
const botones = document.querySelectorAll('button');    // Todos los botones
""", language="javascript")

st.divider()

# --- SECCIÓN 2: MODIFICACIÓN EN TIEMPO REAL ---
st.header("2. Modificando el Contenido y Estilo")
st.write("Podemos cambiar lo que el usuario ve sin refrescar el navegador[cite: 31].")

st.code("""
// Cambiar texto
titulo.innerText = "Tareas del Parcial 2";

// Cambiar estilos (Inline - Usar con moderación)
titulo.style.color = "blue";

// Gestión de clases (Lo mejor para Bootstrap)
titulo.classList.add('text-center', 'text-primary');
titulo.classList.remove('d-none');
""", language="javascript")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Creador de Nodos")
st.info("La IA puede ayudarte a crear elementos desde cero de forma limpia.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en JavaScript Vanilla. Necesito una función que reciba un objeto tarea {id: 1, titulo: "Tarea A"} y cree dinámicamente un <div> de Bootstrap con la clase "card", le asigne el texto del título y lo inserte dentro de un contenedor con el ID "lista-tareas". Usa document.createElement().'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 12)")
st.markdown("""
1.  **Investigación:** ¿Cuál es la diferencia entre un **Evento** y una **Función** en JavaScript?[cite: 31]
2.  **Práctica:** Busca qué hace el método `.addEventListener()` y para qué sirve el parámetro `'click'`[cite: 31].
3.  **Reflexión IA:** Pregunta a la IA: *"¿Por qué es mejor usar addEventListener que el atributo onclick directamente en el HTML?"*[cite: 31]
""")