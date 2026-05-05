import streamlit as st
import streamlit.components.v1 as components

st.title("🚀 Sesión 10: JavaScript Moderno (ES6+)")
st.subheader("Fundamentos de Programación para el Cliente")

# --- RENDERIZADO DE MERMAID ---
mermaid_code = """
graph LR
    A[Entrada de Datos] --> B{Lógica JS}
    B --> C[let: Variables de Bloque]
    B --> D[const: Constantes]
    C & D --> E[Funciones de Flecha =>]
    E --> F[Salida / DOM]
"""

st.code(body=mermaid_code, language="mermaid")


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
    height=250,
)

st.divider()

# --- SECCIÓN 1: VARIABLES Y TIPOS ---
st.header("1. Gestión de Memoria: let vs const")
st.write("A diferencia del `var` antiguo, estas nuevas palabras reservadas tienen 'scope' de bloque.")

st.code("""
// No cambiará: ideal para URLs de tu API Django
const API_URL = "http://localhost:8000/api/tareas/";

// Puede cambiar: ideal para contadores o estados
let contador = 0;
contador++; 

// Tipos de datos
const esIngeniero = true; // Boolean
const materias = ["Backend", "Frontend"]; // Array (Objeto)
""", language="javascript")

st.divider()

# --- SECCIÓN 2: FUNCIONES DE FLECHA (Arrow Functions) ---
st.header("2. Funciones de Flecha (=>)")
st.write("Sintaxis compacta y moderna que utilizaremos para callbacks y promesas[cite: 31].")

st.code("""
// Función tradicional
function saludar(nombre) {
    return "Hola " + nombre;
}

// Función de flecha (Moderna)
const saludarPersona = (nombre) => `Hola ${nombre}`;

console.log(saludarPersona("Ingeniero"));
""", language="javascript")

st.divider()

# --- SECCIÓN IA ---
st.header("🤖 Laboratorio de IA: Refactorización")
st.info("Pide a la IA que modernice tu lógica de programación.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un desarrollador Senior de JavaScript. Tengo estas 3 funciones tradicionales en JS que calculan promedios. Por favor, refactorízalas a Funciones de Flecha usando const y explícame por qué el uso de Template Literals (las comillas invertidas) es mejor que concatenar con +.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 11)")
st.markdown("""
1.  **Investigación:** ¿Qué es el **DOM (Document Object Model)** y cómo se relaciona con el HTML?[cite: 31]
2.  **Práctica:** Abre la consola de Chrome (F12 -> Console) y escribe `document.body.style.backgroundColor = "red"`. Observa qué sucede.
3.  **Reflexión IA:** Pregunta a la IA: *"¿Cuál es la diferencia entre document.getElementById y document.querySelector?"*[cite: 31]
""")