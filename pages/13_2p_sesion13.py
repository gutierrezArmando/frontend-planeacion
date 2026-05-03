import streamlit as st
import streamlit.components.v1 as components

st.title("⏳ Sesión 13: Programación Asíncrona")
st.subheader("De Callbacks a la Elegancia de Async/Await")

st.header("Evolución de la Asincronía")

mermaid_code ="""
graph TD
    A[Callbacks] -->|Evolución| B[Promesas .then]
    B -->|Evolución| C[Async / Await]
    
    style A fill:#f8d7da,stroke:#721c24
    style B fill:#fff3cd,stroke:#856404
    style C fill:#d4edda,stroke:#155724
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
    height=300,
)

st.divider()

# --- SECCIÓN 1: ¿QUÉ ES UNA PROMESA? ---
st.header("1. La Promesa: Un pacto a futuro")
st.write("Una promesa representa un valor que puede estar disponible ahora, en el futuro o nunca.")

st.code("""
const pedirDatos = () => {
    return new Promise((resolve, reject) => {
        const exito = true;
        setTimeout(() => {
            if (exito) resolve("Datos de Django recibidos 🐍");
            else reject("Error en el servidor ❌");
        }, 2000); // Simula espera de 2 segundos
    });
};
""", language="javascript")

st.divider()

# --- SECCIÓN 2: ASYNC / AWAIT ---
st.header("2. Async / Await: Sintaxis Moderna")
st.write("Es la forma más legible de manejar promesas, haciendo que el código asíncrono parezca síncrono[cite: 31].")

st.code("""
async function ejecutarConsulta() {
    try {
        console.log("Iniciando petición...");
        const respuesta = await pedirDatos(); // Espera sin bloquear el navegador
        console.log(respuesta);
    } catch (error) {
        console.error("Hubo un fallo:", error);
    }
}

ejecutarConsulta();
""", language="javascript")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Limpiador de Callbacks")
st.info("La IA ayuda a convertir código antiguo y complejo en estructuras modernas.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un arquitecto de software. Explícame qué es el "Callback Hell" y por qué usar async/await con bloques try/catch mejora la mantenibilidad de mi código cuando trabajo con APIs de Django. Dame un ejemplo de cómo manejar múltiples promesas al mismo tiempo con Promise.all.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 14)")
st.markdown("""
1.  **Investigación:** ¿Qué es un **Endpoint** y qué formato tienen los datos **JSON**?[cite: 13, 14]
2.  **Práctica:** Abre tu proyecto de Backend (Sesión 10-14) y asegúrate de que tu servidor Django esté corriendo y respondiendo en el navegador[cite: 13, 17].
3.  **Reflexión IA:** Pregunta a la IA: *"¿Qué sucede si olvido poner la palabra 'await' antes de una función que devuelve una promesa?"*[cite: 31]
""")