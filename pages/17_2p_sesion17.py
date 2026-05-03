import streamlit as st
import streamlit.components.v1 as components

st.title("📝 Sesión 17: Envío de Datos con POST")
st.subheader("Conectando Formularios con ViewSets de Django")

#------------------------------------------------------------
st.header("🔄 Anatomía de una Petición POST")

# Definición del flujo de renderizado dinámico
mermaid_render_logic = """
graph LR
    A[Formulario HTML] --> B[Evento Submit]
    B --> C[Objeto FormData / JSON]
    C --> D{Fetch POST}
    D --> E[Headers: Content-Type]
    D --> F[Body: JSON.stringify]
    E & F --> G[Django ViewSet]
    G --> H{Validación Serializer}
    H -- OK --> I[Status 201 Created]
    H -- Error --> J[Status 400 Bad Request]
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
    height=200,
)
st.divider()
#------------------------------------------------------------


# --- SECCIÓN 1: CAPTURA DE DATOS ---
st.header("1. FormData y Serialización")
st.write("Para enviar datos, primero debemos capturarlos del DOM y convertirlos a una cadena JSON.")

st.code("""
const formulario = document.querySelector('#form-nueva-tarea');

formulario.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Captura de datos simple
    const nuevaTarea = {
        titulo: document.querySelector('#id_titulo').value,
        descripcion: document.querySelector('#id_descripcion').value,
        completada: false
    };

    await enviarDatos(nuevaTarea);
});
""", language="javascript")

st.divider()

# --- SECCIÓN 2: LA PETICIÓN FETCH POST ---
st.header("2. Configuración de fetch()")
st.write("A diferencia de GET, el método POST requiere un objeto de configuración con method, headers y body.")

st.code("""
const enviarDatos = async (datos) => {
    try {
        const respuesta = await fetch("http://127.0.0.1:8000/api/tareas/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(datos) // Convierte objeto a texto JSON
        });

        if (respuesta.ok) {
            alert("¡Tarea guardada con éxito!");
            window.location.reload(); // Recarga para ver el nuevo registro
        } else {
            const errores = await respuesta.json();
            console.table(errores); // Muestra errores de validación de Django
        }
    } catch (error) {
        console.error("Fallo en la comunicación:", error);
    }
};
""", language="javascript")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Validador de Peticiones")
st.info("Utiliza la IA para generar código que maneje los errores de Django de forma elegante.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un desarrollador Frontend Senior. Tengo un formulario que envía datos a Django vía POST. Si el serializador de Django devuelve un error 400 con un mensaje como {"titulo": ["Este campo es obligatorio"]}, ¿cómo puedo usar JavaScript para mostrar ese mensaje específicamente debajo del input del título usando clases de Bootstrap?'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 18)")
st.markdown("""
1.  **Investigación**: ¿Qué son los métodos **PUT** y **PATCH** y en qué se diferencian al actualizar un registro?
2.  **Práctica**: Asegúrate de tener identificado el **ID** de los registros en tu consola; lo necesitaremos para saber *qué* registro editar o borrar.
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cómo puedo capturar el ID de un elemento al que le hice clic dentro de una lista generada dinámicamente?"*
""")