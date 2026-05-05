import streamlit as st
import streamlit.components.v1 as components

st.title("💾 Sesión 21: Almacenamiento Local (LocalStorage)")
st.subheader("Persistencia de Datos en el Cliente")

# --- BLOQUE DE MERMAID ---
mermaid_code = """
graph LR
    JS[JavaScript] -- "setItem('key', 'value')" --> LS[(LocalStorage)]
    LS -- "getItem('key')" --> JS
    LS -- "removeItem('key')" --> JS
    LS -- "clear()" --> JS
"""

st.write("### Operaciones del LocalStorage")
st.code(mermaid_code, language="mermaid")
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
    height=200,
)

# --- GUÍA TÉCNICA ---
st.header("1. Métodos Fundamentales")
st.write("LocalStorage solo guarda strings. Si quieres guardar un objeto, debes usar JSON.stringify().")

st.code("""
// 1. Guardar un dato simple
localStorage.setItem('tema', 'oscuro');

// 2. Guardar un objeto (como un mini-token de sesión)
const sesion = { usuario: 'profesor_cs', expiracion: '2026-05-30' };
localStorage.setItem('user_session', JSON.stringify(sesion));

// 3. Recuperar y convertir de vuelta
const datosGuardados = JSON.parse(localStorage.getItem('user_session'));
console.log(datosGuardados.usuario); // profesor_cs
""", language="javascript")

st.divider()

st.header("2. Ejemplo Práctico: Modo Oscuro")
st.write("Una de las utilidades más comunes para mejorar la UX sin tocar el Backend[cite: 1].")

st.code("""
const btnToggle = document.querySelector('#btn-theme');

// Al cargar la página, verificamos si ya existía una preferencia
if (localStorage.getItem('modo') === 'dark') {
    document.body.classList.add('bg-dark', 'text-white');
}

btnToggle.addEventListener('click', () => {
    document.body.classList.toggle('bg-dark');
    document.body.classList.toggle('text-white');
    
    // Guardamos la elección para la próxima visita
    const modoActual = document.body.classList.contains('bg-dark') ? 'dark' : 'light';
    localStorage.setItem('modo', modoActual);
});
""", language="javascript")

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: Seguridad en el Almacenamiento")
st.info("La IA te ayudará a entender las limitaciones de esta tecnología.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en seguridad web. Explícame por qué no es seguro guardar contraseñas o información sensible en LocalStorage y qué relación tiene esto con los ataques XSS (Cross-Site Scripting). ¿Qué alternativas existen para guardar datos sensibles?'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 22)")
st.markdown("""
1.  **Investigación**: ¿Cómo funcionan los métodos `.filter()` y `.map()` en JavaScript para arreglos de objetos?[cite: 1]
2.  **Práctica**: Abre la pestaña **Application** (o Almacenamiento) en las DevTools de tu navegador y localiza la sección de LocalStorage para ver qué páginas tienen datos guardados en tu equipo.
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cuál es la diferencia de capacidad de almacenamiento entre una Cookie y LocalStorage?"*
""")