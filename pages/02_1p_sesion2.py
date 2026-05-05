import streamlit as st
import streamlit.components.v1 as components

st.title("📑 Sesión 2: HTML5 Semántico")
st.subheader("Ingeniería de Software: Estructuración vs. 'Div-itis'")

# --- COMPARATIVA VISUAL (MERMAID) ---
st.header("1. ¿Cómo entiende el navegador tu código?")
st.write("A la izquierda, lo que sucede cuando usas etiquetas semánticas. A la derecha, el caos de los divs genéricos.")

mermaid_code = """
graph TD
    subgraph "Estructura Profesional (Semántica)"
        A[header] --- B[nav]
        A --- C[main]
        C --- D[section]
        D --- E[article]
        A --- F[footer]
    end
    
    subgraph "Estructura No Profesional (Div-itis)"
        G[div id='cabecera'] --- H[div id='menu']
        G --- I[div id='principal']
        I --- J[div id='contenido']
        G --- K[div id='pie']
    end
    
    style A fill:#d4edda,stroke:#155724
    style G fill:#f8d7da,stroke:#721c24
"""

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
    height=400,
)

st.divider()

# --- SECCIÓN: CÓDIGO DE EJEMPLO ---
st.header("2. Comparativa de Código")

col_bad, col_good = st.tabs(["❌ Estructura NO Profesional", "✅ Estructura Profesional"])

with col_bad:
    st.error("### El error del 'Div-itis'")
    st.write("Este código funciona y se ve igual en pantalla, pero es **invisible** para Google y **hostil** para los lectores de pantalla.")
    st.code("""
<!-- Código NO Profesional: Todo es un div -->
<div id="header">
    <div class="title">Mi Blog de Django</div>
    <div class="nav">
        <div class="link">Inicio</div>
        <div class="link">Contacto</div>
    </div>
</div>

<div id="main-content">
    <div class="post">
        <div class="post-title">Aprendiendo Serializers</div>
        <div class="post-body">Hoy veremos cómo convertir modelos a JSON...</div>
    </div>
</div>

<div id="footer">
    <div class="copy">Copyright 2026</div>
</div>
    """, language="html")

with col_good:
    st.success("### Estándar de Ingeniería (Semántico)")
    st.write("Este código utiliza el estándar de la W3C, mejorando el SEO y la accesibilidad automáticamente.")
    st.code("""
<!-- Código Profesional: Etiquetas con significado -->
<header>
    <h1>Mi Blog de Django</h1>
    <nav>
        <ul>
            <li><a href="#">Inicio</a></li>
            <li><a href="#">Contacto</a></li>
        </ul>
    </nav>
</header>

<main>
    <article>
        <h2>Aprendiendo Serializers</h2>
        <p>Hoy veremos cómo convertir modelos a JSON...</p>
    </article>
</main>

<footer>
    <p>&copy; 2026 - Ingeniería de Software</p>
</footer>
    """, language="html")

st.divider()

# --- SECCIÓN IA ---
st.header("🤖 Laboratorio de IA: Auditoría Semántica")
st.info("Pega el código 'No Profesional' en la IA para ver qué te recomienda.")
st.markdown("""
> **Prompt sugerido:** 
> *'Analiza este código HTML lleno de divs. Explícame técnicamente por qué es una mala práctica para el SEO y cómo podrías refactorizarlo usando HTML5 semántico para que sea más accesible.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida")
st.markdown("""
1.  **Investigación:** ¿Qué es un **lector de pantalla** y cómo interactúa con las etiquetas `<nav>` y `<main>`?
2.  **Práctica:** Instala la extensión **Lighthouse** en Chrome y audita el sitio web de tu universidad. ¿Qué puntaje de Accesibilidad tiene?
3.  **Preparación:** Investiga los 3 tipos de selectores básicos de CSS (etiqueta, clase e ID) para la próxima sesión.
""")