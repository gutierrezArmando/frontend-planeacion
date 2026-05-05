import streamlit as st
import streamlit.components.v1 as components

st.title("🔗 Sesión 15: Integración Frontend-Backend")
st.subheader("Peticiones GET a tu propia API de Django")

# --- SECCIÓN 1: EL REQUISITO PREVIO (CORS) ---
st.header("1. El Portero de la API: CORS")
st.warning("Antes de programar en JS, asegúrate de que tu Backend tenga instalado 'django-cors-headers' y configurado en settings.py.")

st.code("""
# settings.py de tu proyecto Django
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500", # Origen de tu Frontend (Live Server)
    "http://localhost:5500",
]
""", language="python")

st.divider()

# --- SECCIÓN 2: PETICIÓN REAL ---
st.header("2. Consumiendo tus propios Datos")
st.write("Ahora usaremos fetch para traer la lista de tareas que guardaste en MySQL.")

st.code("""
const URL_API = "http://127.0.0.1:8000/api/tareas/";

const listarTareas = async () => {
    try {
        const respuesta = await fetch(URL_API);
        if (!respuesta.ok) throw new Error("Error en la conexión");
        
        const tareas = await respuesta.json();
        console.log("Tareas desde Django:", tareas);
        
        // Aquí iniciaremos la manipulación del DOM en la siguiente sesión
    } catch (error) {
        console.error("Fallo técnico:", error);
    }
};

listarTareas();
""", language="javascript")

st.divider()


st.header("Flujo de Integración Fullstack")
st.write("Este diagrama ilustra cómo viajan los datos desde la base de datos hasta la pantalla del usuario.")
mermaid_code ="""
sequenceDiagram
    participant B as Navegador (JS Fetch)
    participant D as Django (API REST)
    participant M as MySQL (DB)

    B->>D: GET /api/tareas/
    Note over D: Verifica CORS Middleware
    D->>M: SELECT * FROM tareas
    M-->>D: Lista de registros
    D-->>B: JSON [ {id: 1, titulo: "..."}, ... ]
    Note over B: console.log(datos)
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
    height=500,
)

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Debugger de Integración")
st.info("Utiliza este prompt si tu conexión falla:")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto Fullstack. Mi frontend en JS está intentando hacer un GET a mi API de Django pero recibo un error de "CORS policy". Explícame paso a paso qué debo revisar en mi middleware de Django y qué cabeceras debe incluir la respuesta para que el navegador permita la conexión.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 16)")
st.markdown("""
1.  **Investigación:** ¿Qué es un **Template Literal** (backticks `` ` ``) y cómo ayuda a crear HTML dinámico en JS?[cite: 31]
2.  **Práctica:** Repasa la **Sesión 11** de manipulación del DOM; la necesitaremos para inyectar los datos de la API en el HTML[cite: 31].
3.  **Reflexión IA:** Pregunta a la IA: *"¿Cuál es la forma más eficiente de recorrer un arreglo de objetos JSON para crear una lista de Cards de Bootstrap?"*[cite: 31]
""")