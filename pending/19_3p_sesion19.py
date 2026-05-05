import streamlit as st
import streamlit.components.v1 as components

st.title("🛠️ Sesión 19: CRUD Completo")
st.subheader("Implementación de PUT, PATCH y DELETE")

st.header("El Flujo del CRUD")


mermaid_render_logic = """
graph TD
    A[Interfaz: Card/Tabla] --> B{¿Qué acción?}
    B -- Editar --> C[Cargar datos en Formulario]
    C --> D[Petición PUT/PATCH]
    D --> G[Refrescar UI]
    
    B -- Eliminar --> E[Confirmación Modal]
    E -- Sí --> F[Petición DELETE]
    F --> G
    
    style F fill:#f8d7da,stroke:#721c24
    style D fill:#fff3cd,stroke:#856404
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
    height=550,
)
st.divider()

# --- SECCIÓN 1: ELIMINACIÓN ---
st.header("1. Peticiones DELETE")
st.write("Es la petición más sencilla pero la más peligrosa. Requiere el ID del registro.")

st.code("""
const eliminarTarea = async (id) => {
    const confirmar = confirm("¿Seguro que deseas eliminar esta tarea?");
    if (!confirmar) return;

    try {
        const respuesta = await fetch(`http://127.0.0.1:8000/api/tareas/${id}/`, {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' }
        });

        if (respuesta.status === 204) {
            alert("Eliminado correctamente");
            renderizarTareas(); // Refrescamos la lista
        }
    } catch (error) {
        console.error("Error al eliminar:", error);
    }
};
""", language="javascript")

st.divider()

# --- SECCIÓN 2: ACTUALIZACIÓN ---
st.header("2. Peticiones PATCH (Actualización Parcial)")
st.write("Ideal para acciones rápidas como marcar una tarea como 'completada'.")

st.code("""
const alternarEstado = async (id, estadoActual) => {
    try {
        await fetch(`http://127.0.0.1:8000/api/tareas/${id}/`, {
            method: 'PATCH',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ completada: !estadoActual })
        });
        renderizarTareas();
    } catch (error) {
        console.error("Error al actualizar:", error);
    }
};
""", language="javascript")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Guardián del ID")
st.info("La IA puede ayudarte a gestionar el flujo de edición, que es el más complejo.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en JavaScript. Tengo una lista de tareas renderizada dinámicamente. ¿Cómo puedo hacer que al dar clic en el botón "Editar" de una Card, los datos de esa tarea específica se carguen en un formulario de edición (inputs) para luego enviarlos con un PUT? Dame un ejemplo usando data-attributes.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 20)")
st.markdown("""
1.  **Investigación**: ¿Qué es una **Single Page Application (SPA)** y en qué se diferencia de los sitios web tradicionales?
2.  **Práctica**: Revisa tu código de la Sesión 16; asegúrate de que tus botones de Editar/Eliminar tengan el ID de la tarea inyectado.
3.  **Reflexión IA**: Pregunta a la IA: *"¿Qué es un 'Spinner' de carga y por qué es importante mostrarlo mientras esperamos que se complete un DELETE o un PUT?"*
""")