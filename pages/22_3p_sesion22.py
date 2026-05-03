import streamlit as st
import streamlit.components.v1 as components

st.title("🔍 Sesión 22: Filtros y Búsquedas")
st.subheader("Manipulación de Arreglos para Interfaces Rápidas")

# --- BLOQUE DE MERMAID ---
mermaid_logic = """
graph LR
    Input[Escribir en Buscador] --> Logic{Array.filter}
    Logic --> Render[Re-renderizar DOM]
    Render --> Result[Resultados Visuales]
"""

st.code(mermaid_logic, language="mermaid")
components.html(
    f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {mermaid_logic}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    """,
    height=200,
)

# --- GUÍA TÉCNICA ---
st.header("1. Métodos de Arreglos (ES6+)")
st.write("Para filtrar, usamos métodos que no modifican el arreglo original, sino que crean uno nuevo.")

st.code("""
// Suponiendo que 'tareas' es el array que vino de Django
const tareas = [
    { id: 1, titulo: 'Repasar SQL', prioridad: 'Alta' },
    { id: 2, titulo: 'Configurar Cors', prioridad: 'Baja' }
];

// .filter(): Crea un subconjunto
const prioritarias = tareas.filter(t => t.prioridad === 'Alta');

// .find(): Busca un elemento único por ID
const tareaEspecifica = tareas.find(t => t.id === 2);
""", language="javascript")

st.divider()

st.header("2. Implementación del Buscador")
st.write("Escuchamos el evento 'input' para que la búsqueda sea instantánea mientras el usuario escribe[cite: 1].")

st.code("""
const inputBusqueda = document.querySelector('#buscador');
let todasLasTareas = []; // Se llena con el fetch inicial

inputBusqueda.addEventListener('input', (e) => {
    const texto = e.target.value.toLowerCase();
    
    const filtradas = todasLasTareas.filter(tarea => 
        tarea.titulo.toLowerCase().includes(texto)
    );
    
    // Reutilizamos la función de la Sesión 16
    pintarTareas(filtradas); 
});
""", language="javascript")

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: Optimización de Arreglos")
st.info("La IA te ayudará a escribir filtros más limpios.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en JavaScript. Tengo un arreglo de objetos que viene de una API de Django. Necesito crear una función de filtrado múltiple que me permita buscar por texto y al mismo tiempo filtrar por un checkbox de "Solo completadas". Usa métodos de arreglos modernos.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 23)")
st.markdown("""
1.  **Investigación**: ¿Qué es un **CSRF Token** en Django y por qué el servidor rechaza peticiones POST si no lo incluimos?[cite: 2]
2.  **Práctica**: Revisa en tu código de Backend la Sesión 5 (Forms) y busca dónde se insertaba el `{% csrf_token %}`[cite: 2].
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cómo puedo obtener el valor de una cookie llamada 'csrftoken' usando solo JavaScript Vanilla?"*
""")