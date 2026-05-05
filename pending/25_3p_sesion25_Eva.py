import streamlit as st
import streamlit.components.v1 as components

st.title("🚀 Sesión 25: Evaluación Final")
st.subheader("Proyecto Integrador: Aplicación Fullstack Desacoplada")

# --- BLOQUE DE MERMAID ---
mermaid_code = """
graph LR
    A[HTML5/CSS3] --> D{Dashboard}
    B[Bootstrap 5] --> D
    C[JS / Fetch] --> D
    D <--> E[Django API]
    E <--> F[MySQL DB]
"""

mermaid_config = "{ startOnLoad: true, theme: 'neutral' }"

st.write("### Componentes del Sistema Integrado")
components.html(
    f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {mermaid_code}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({mermaid_config});
    </script>
    """,
    height=250,
)

# --- CHECKLIST DE ENTREGA ---
st.header("📋 Requisitos de la Entrega Final")
st.info("Asegúrate de que tu aplicación cumpla con todos estos puntos antes de la defensa.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Frontend (Interfaz)**
    *   [ ] Layout responsivo con Bootstrap 5.
    *   [ ] Consumo de API mediante Fetch (GET, POST, PUT, DELETE).
    *   [ ] Filtros de búsqueda en tiempo real[cite: 1].
    *   [ ] Manejo de LocalStorage para preferencias[cite: 1].
    """)
with col2:
    st.markdown("""
    **Backend (Servicios)**
    *   [ ] API REST documentada con Swagger[cite: 2].
    *   [ ] Seguridad CSRF implementada en las peticiones.
    *   [ ] Uso de Signals para automatización[cite: 2].
    *   [ ] Consultas de SQL puro para reportes complejos[cite: 2].
    """)

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 IA: Preparación para la Defensa")
st.success("Usa la IA para practicar las posibles preguntas del profesor.")
st.markdown("""
> **Prompt sugerido:** 
> *'Actúa como un sínodo de examen profesional de ingeniería. Revisa mi arquitectura que usa Django y JS Vanilla. Hazme 5 preguntas técnicas difíciles sobre cómo gestiono la seguridad CSRF, cómo optimicé el renderizado del DOM y qué ventajas tiene usar SQL puro sobre el ORM para reportes de negocio.'*[cite: 1, 2]
""")

# --- CIERRE DEL CUATRIMESTRE ---
st.balloons()
st.warning("### 🏁 ¡Felicidades, Ingeniero!")
st.write("""
Has completado el ciclo completo de desarrollo. Ahora tienes las bases para aprender cualquier 
framework moderno como React o Vue, entendiendo lo que sucede 'bajo el capó'.
""")