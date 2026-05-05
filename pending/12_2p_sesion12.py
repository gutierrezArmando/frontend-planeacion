import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("⚡ Sesión 12: Eventos y Validaciones")
st.subheader("Control de Interacción y Limpieza de Datos")

st.header("Ciclo de un Evento de Formulario")
mermaid_code = """
sequenceDiagram
    participant U as Usuario
    participant D as DOM (Formulario)
    participant J as JavaScript (Script)
    participant S as Servidor (Django)

    U->>D: Escribe datos y da Clic en Enviar
    D->>J: Dispara evento 'submit'
    Note over J: e.preventDefault()
    J->>J: Ejecuta Validaciones
    alt Datos Válidos
        J->>S: Envía petición (Fetch)
    else Datos Inválidos
        J->>D: Muestra alertas visuales
    end
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

# --- SECCIÓN 1: EL ESCUCHADOR DE EVENTOS ---
st.header("1. addEventListener: El Estándar")
st.write("Es la forma profesional de asignar comportamiento a los elementos del DOM.")

st.code("""
const boton = document.querySelector('#btn-guardar');

// Escuchar el clic
boton.addEventListener('click', (event) => {
    console.log("¡Hiciste clic en el botón!");
    console.log(event.target); // El elemento que originó el evento
});
""", language="javascript")

st.divider()

# --- SECCIÓN 2: MANEJO DE FORMULARIOS ---
st.header("2. El evento 'submit' y preventDefault")
st.write("Al enviar un formulario, el navegador intenta recargar la página por defecto. Debemos detenerlo para manejar la lógica con JS[cite: 31].")

st.code("""
const formulario = document.querySelector('#form-tarea');

formulario.addEventListener('submit', (e) => {
    e.preventDefault(); // Evita que la página se recargue
    
    const titulo = document.querySelector('#id_titulo').value;
    
    // Validación simple
    if (titulo.length < 5) {
        alert("El título es muy corto");
        return; // Detiene la ejecución
    }
    
    console.log("Datos listos para enviar a Django:", titulo);
});
""", language="javascript")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Maestro de las Validaciones")
st.info("La IA es excelente para generar reglas de validación robustas.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en JavaScript. Necesito una función de validación para un formulario que verifique: 
> 1. Que el correo electrónico sea válido. 
> 2. Que la contraseña tenga al menos 8 caracteres, una mayúscula y un número. 
> Dame el código usando event.target y clases de Bootstrap (.is-invalid) para mostrar los errores visualmente.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 13)")
st.markdown("""
1.  **Investigación:** ¿Qué significa que JavaScript sea **Asíncrono** y qué es el "Event Loop"?[cite: 31]
2.  **Práctica:** Busca la diferencia entre una **Promesa** y un **Callback**.
3.  **Reflexión IA:** Pregunta a la IA: *"¿Por qué necesitamos async/await cuando pedimos datos a una API de Django en lugar de usar código normal?"*[cite: 31]
""")