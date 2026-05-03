import streamlit as st
import streamlit.components.v1 as components

st.title("🚨 Sesión 20: Manejo de Errores y Feedback")
st.subheader("Comunicación Efectiva entre el Servidor y el Usuario")
#-----------------------------------
st.header("Flujo de Control de Errores")


mermaid_render_logic = """
graph TD
    A[Petición Fetch] --> B{¿Respuesta OK?}
    B -- Sí (2xx) --> C[Notificación de Éxito]
    B -- No (4xx / 5xx) --> D{¿Qué código es?}
    D -- 400 --> E[Error de Validación: Datos inválidos]
    D -- 404 --> F[Error de Recurso: No encontrado]
    D -- 500 --> G[Error Crítico: Servidor caído]
    E & F & G --> H[Mostrar Alert / Toast de Bootstrap]
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
    height=700,
)
st.divider()
#---------------------------------

# --- SECCIÓN 1: EL CONTROLADOR DE ESTADOS ---
st.header("1. Lógica de Intercepción de Códigos")
st.write("Usamos el objeto 'response' de fetch para decidir qué mostrar al usuario.")

st.code("""
const manejarRespuesta = async (response) => {
    const contenedor = document.querySelector('#alertas-container');
    
    if (response.status === 201) {
        mostrarAlerta("¡Registro creado con éxito!", "success");
    } else if (response.status === 400) {
        const errores = await response.json();
        mostrarAlerta("Error en los datos: " + Object.values(errores)[0], "warning");
    } else if (response.status === 500) {
        mostrarAlerta("Error crítico en el servidor. Contacte a soporte.", "danger");
    }
};

const mostrarAlerta = (mensaje, tipo) => {
    const alertHTML = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${mensaje}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    document.querySelector('#notificaciones').innerHTML = alertHTML;
};
""", language="javascript")

st.divider()

# --- SECCIÓN 2: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: UX de Errores")
st.info("Pide a la IA que mejore la accesibilidad de tus mensajes.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un experto en UX Writing. Tengo un sistema que devuelve errores 403 (No autorizado) y 404 (No encontrado) desde Django. Redacta mensajes de error que no asusten al usuario, que sean profesionales y que sugieran una acción para solucionar el problema.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Hacia el Parcial 3)")
st.markdown("""
1.  **Investigación**: ¿Qué es **NPM (Node Package Manager)** y para qué sirve en el desarrollo moderno?
2.  **Preparación**: Asegúrate de tener una cuenta en **GitHub**; la usaremos para desplegar tus aplicaciones de React en el tercer parcial.
3.  **Reflexión IA**: Pregunta a la IA: *"¿Por qué las aplicaciones modernas usan Toasts (notificaciones pequeñas que desaparecen) en lugar de la función alert() de JavaScript?"*
""")