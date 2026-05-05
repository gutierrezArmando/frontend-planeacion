import streamlit as st
import streamlit.components.v1 as components

st.title("🖼️ Sesión 16: Renderizado Dinámico")
st.subheader("Transformando JSON en Interfaces de Bootstrap")

# --- SECCIÓN 1: LA PLANTILLA DINÁMICA ---
st.header("1. Template Literals: El molde del Ingeniero")
st.write("Usamos las comillas invertidas (`` ` ``) para mezclar HTML con variables de JavaScript de forma limpia.")

st.code("""
// Función que genera el HTML de una Card
const crearCard = (tarea) => {
    return `
        <div class="col-md-4 mb-3">
            <div class="card shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">${tarea.titulo}</h5>
                    <p class="card-text">${tarea.descripcion}</p>
                    <span class="badge ${tarea.completada ? 'bg-success' : 'bg-warning'}">
                        ${tarea.completada ? 'Completada' : 'Pendiente'}
                    </span>
                </div>
            </div>
        </div>
    `;
};
""", language="javascript")

st.divider()

# --- SECCIÓN 2: INYECCIÓN EN EL DOM ---
st.header("2. El Ciclo de Renderizado")
st.write("Combinamos Fetch con la iteración para pintar toda la lista de tareas en pantalla[cite: 31].")

st.code("""
const contenedor = document.querySelector('#lista-tareas');

const renderizarTareas = async () => {
    const respuesta = await fetch("http://127.0.0.1:8000/api/tareas/");
    const tareas = await respuesta.json();

    let htmlFinal = "";
    
    // Iteramos y acumulamos el HTML
    tareas.forEach(tarea => {
        htmlFinal += crearCard(tarea);
    });

    // Una sola inserción al DOM (más eficiente)
    contenedor.innerHTML = htmlFinal;
};

renderizarTareas();
""", language="javascript")

st.divider()

st.header("🔄 Ciclo de Renderizado Dinámico (Client-Side Rendering)")
st.write("""
A diferencia del Parcial 1, donde el servidor enviaba el HTML ya armado, ahora el 
navegador recibe datos "crudos" y construye la interfaz en tiempo real.
""")

# Definición del flujo de renderizado dinámico
mermaid_render_logic = """
sequenceDiagram
    participant API as Django API (JSON)
    participant JS as JavaScript (Fetch)
    participant DOM as DOM Tree (HTML)
    participant UI as Interfaz de Usuario

    API->>JS: 1. Entrega Arreglo de Objetos [{}, {}, {}]
    Note over JS: 2. Iteración (forEach / map)
    JS->>JS: 3. Construcción de Template Literal (Strings)
    JS->>DOM: 4. Inyección vía .innerHTML
    DOM->>UI: 5. El usuario ve las nuevas Cards/Tablas
    
    Note right of UI: No hubo recarga de página (F5)
"""

# Renderizado en Streamlit
components.html(
    f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {mermaid_render_logic}
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
st.header("🤖 Laboratorio de IA: El Maestro del Refactor")
st.info("Pide a la IA que mejore la eficiencia de tu renderizado.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en performance de JavaScript. Analiza mi código de renderizado dinámico. ¿Por qué es mejor acumular el HTML en una variable y hacer una sola inserción al final con innerHTML en lugar de usar appendChild() dentro del bucle? Explícame el concepto de Reflow y Repaint.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 17)")
st.markdown("""
1.  **Investigación**: ¿Qué es el objeto **FormData** en JavaScript y cómo ayuda a capturar datos de un formulario?[cite: 31]
2.  **Práctica**: Revisa en tu código de Django qué campos son obligatorios en tu `POST` (ej. titulo, prioridad)[cite: 14].
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cómo envío un objeto JSON al servidor usando fetch() con el método POST?"*[cite: 31]
""")