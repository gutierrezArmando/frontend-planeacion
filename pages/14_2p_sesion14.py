import streamlit as st

st.title("🌐 Sesión 14: Consumo de APIs con Fetch")
st.subheader("El Estándar de Comunicación JSON")

# --- SECCIÓN 1: ¿QUÉ ES JSON? ---
st.header("1. El Formato JSON")
st.write("Es el formato que tu API de Django devuelve a través de los Serializers[cite: 13, 14].")

st.code("""
{
    "id": 1,
    "titulo": "Aprender Fetch",
    "completada": false
}
""", language="json")

st.divider()

# --- SECCIÓN 2: USO DE FETCH ---
st.header("2. Peticiones con fetch()")
st.write("Combinamos Fetch con Async/Await para un código limpio y profesional.")

st.code("""
const obtenerDatos = async () => {
    try {
        // 1. Realizar la petición
        const respuesta = await fetch('https://jsonplaceholder.typicode.com/todos/1');
        
        // 2. Convertir la respuesta a JSON
        const datos = await respuesta.json();
        
        // 3. Usar los datos
        console.log("Título de la tarea:", datos.title);
    } catch (error) {
        console.error("Error al conectar con la API:", error);
    }
};

obtenerDatos();
""", language="javascript")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Analista de Tráfico")
st.info("La IA puede ayudarte a entender estructuras de JSON complejas.")
st.markdown("""
> **Prompt sugerido**: 
> *'Actúa como un experto en desarrollo web. Explícame paso a paso qué sucede en el navegador cuando ejecuto un fetch(). ¿Qué son las cabeceras (headers) y por qué es importante el "Content-Type: application/json" cuando trabajamos con APIs de Django?'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 15)")
st.markdown("""
1.  **Investigación**: ¿Qué es **CORS** y por qué mi navegador bloquea las peticiones de `localhost:5500` a `localhost:8000`?
2.  **Práctica**: Asegúrate de tener instalado el paquete `django-cors-headers` en tu proyecto de Django como vimos en la planeación de Backend[cite: 31].
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cómo puedo pasar parámetros en la URL (Query Params) usando fetch para filtrar tareas por ID en mi API?"*
""")