import streamlit as st
import streamlit.components.v1 as components

st.title("🛡️ Sesión 23: Seguridad Frontend (CSRF)")
st.subheader("Integración de Tokens de Seguridad con Django")

# --- BLOQUE DE MERMAID ---

mermaid_code = """
sequenceDiagram
    participant B as Navegador (JS)
    participant C as Cookie Storage
    participant D as Django Server

    D-->>C: Envía cookie 'csrftoken' (en el primer GET)
    B->>C: Lee valor de la cookie
    Note over B: Prepara Headers de Fetch
    B->>D: POST /api/tareas/ (Header: X-CSRFToken)
    D->>D: Compara Token de Header vs Cookie
    alt Tokens Coinciden
        D-->>B: 201 Created / 200 OK
    else Tokens NO Coinciden
        D-->>B: 403 Forbidden
    end
"""

st.write("### Flujo de Validación CSRF")
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
    height=650,
)

# --- GUÍA TÉCNICA ---
st.header("1. Extrayendo el Token de la Cookie")
st.write("Django recomienda una función estándar para obtener el token desde el almacenamiento de cookies del navegador.")

st.code("""
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');
""", language="javascript")

st.divider()

st.header("2. Petición Fetch con Seguridad")
st.write("Al realizar un POST, PUT o DELETE, debemos incluir el encabezado 'X-CSRFToken'[cite: 1].")

st.code("""
const enviarConSeguridad = async (datos) => {
    const response = await fetch('/api/tareas/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Inyección del token de seguridad
        },
        body: JSON.stringify(datos)
    });
    
    if (response.ok) {
        console.log("Petición autorizada y procesada");
    }
};
""", language="javascript")

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: Auditoría de Seguridad")
st.info("La IA puede ayudarte a fortalecer tu aplicación.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en ciberseguridad. Explícame paso a paso cómo ocurre un ataque CSRF si no utilizo tokens en mi aplicación de Django y por qué el navegador no bloquea este tipo de ataques automáticamente mediante la política de mismo origen (SOP).'*[cite: 1, 2]
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 24)")
st.markdown("""
1.  **Investigación**: ¿Qué es el **Call Stack** y para qué sirve el **Breakpoint** en las herramientas de desarrollo?[cite: 1]
2.  **Práctica**: Intenta provocar un error `403` en tu proyecto de Django quitando el header del token y observa el mensaje que devuelve el servidor[cite: 1, 2].
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cuál es la diferencia entre un log de consola (console.log) y un punto de interrupción (breakpoint) al depurar código?"*[cite: 1]
""")