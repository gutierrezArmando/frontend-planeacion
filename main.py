import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="Ingeniería Frontend | Dashboard del Curso",
    page_icon="💻",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
# Se corrigió el parámetro 'unsafe_allow_name' por 'unsafe_allow_html'
st.markdown("""
    <style>
    .main-title { font-size: 3rem; font-weight: 800; color: #1E1E1E; margin-bottom: 0; }
    .subtitle { font-size: 1.5rem; color: #666; margin-bottom: 2rem; }
    .card-parcial { 
        padding: 1.5rem; 
        border-radius: 10px; 
        border: 1px solid #ddd; 
        background-color: #f9f9f9; 
        margin-bottom: 1rem;
        min-height: 200px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown('<p class="main-title">Ingeniería de Software: Desarrollo Frontend</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Sincronización Fullstack con Django & MySQL</p>', unsafe_allow_html=True)

st.info("""
**Descripción del Curso:** Esta asignatura transforma a los estudiantes de programadores de lógica en arquitectos de interfaces. 
El enfoque es 100% integrador: cada píxel diseñado en el frontend responde a un dato real gestionado en el backend de Django.
""")

st.divider()

# --- DIAGRAMA DE ARQUITECTURA GLOBAL ---
st.header("🌐 El Ecosistema del Proyecto Integrador")
mermaid_global = """
graph TD
    subgraph "Frontend (El Cliente)"
        A[HTML5 Semántico] --> B[Bootstrap 5 / CSS3]
        B --> C[JavaScript Vanilla]
    end
    subgraph "Backend (El Servidor)"
        D[Django REST Framework] --> E[MySQL DB]
    end
    C -- "Fetch API (JSON)" --> D
    D -- "Response" --> C
"""

# Renderizado de Mermaid
components.html(
    f"""
    <div class="mermaid" style="display: flex; justify-content: center;">
        {mermaid_global}
    </div>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
        mermaid.initialize({{ startOnLoad: true, theme: 'neutral' }});
    </script>
    """,
    height=350,
)

st.divider()

# --- DESGLOSE DE TEMAS ---
st.header("📋 Planificación Académica")

# Resumen General en Columnas
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card-parcial">
        <h3>Parcial 1</h3>
        <p><b>Foco:</b> Estructura y Estética Profesional.</p>
        <p><i>Maquetación responsiva y estándares W3C.</i></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-parcial">
        <h3>Parcial 2</h3>
        <p><b>Foco:</b> Lógica y Dinamismo.</p>
        <p><i>Consumo de APIs y manipulación del DOM.</i></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-parcial">
        <h3>Parcial 3</h3>
        <p><b>Foco:</b> Interacción Avanzada.</p>
        <p><i>Seguridad, persistencia y CRUD completo.</i></p>
    </div>
    """, unsafe_allow_html=True)

# Tabs con Desglose Detallado por Sesión
st.subheader("Desglose Detallado por Sesiones")
tab1, tab2, tab3 = st.tabs(["Sesiones Parcial 1", "Sesiones Parcial 2", "Sesiones Parcial 3"])

with tab1:
    st.markdown("""
    *   **Sesiones 1-2:** Ecosistema Web y HTML5 Semántico.
    *   **Sesiones 3-5:** CSS3 Profundo: Box Model, Flexbox y Grid.
    *   **Sesiones 6-8:** Bootstrap 5: Grid System, Componentes y Responsive.
    *   **Sesión 9:** **Evaluación:** Maquetación del Monolito Django.
    """)

with tab2:
    st.markdown("""
    *   **Sesiones 10-12:** JS Moderno, DOM y Gestión de Eventos.
    *   **Sesiones 13-14:** Asincronía (Async/Await) y Formato JSON.
    *   **Sesiones 15-17:** Integración con Django API y Renderizado Dinámico.
    *   **Sesión 18:** **Evaluación:** 'La Gran Conexión' Fullstack.
    """)

with tab3:
    st.markdown("""
    *   **Sesiones 19-20:** CRUD Completo y Gestión de Errores HTTP.
    *   **Sesiones 21-22:** LocalStorage y Filtros de Datos en Tiempo Real.
    *   **Sesiones 23-24:** Seguridad CSRF y Taller de Depuración (DevTools).
    *   **Sesión 25:** **Evaluación Final:** Dashboard Integrador de Negocio.
    """)

st.sidebar.success("Selecciona una sesión en el menú para comenzar.")