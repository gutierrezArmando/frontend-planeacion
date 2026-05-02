import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Backend con Django - Ing. Software",
    page_icon="🐍",
    layout="wide"
)

# Título y Bienvenida
st.title("🚀 Desarrollo de Backend: Django")
st.subheader("Ingeniería en Desarrollo de Software")

st.markdown("""
---
### 📖 Bienvenidos, Ingenieros.
Este portal servirá como guía interactiva para el cuatrimestre. Aquí encontrarán el desarrollo de cada sesión, 
códigos sugeridos y recursos para sus proyectos.

### 🎯 Objetivo del Curso
Dominar el ciclo **Request-Response** tradicional, la arquitectura de **APIs REST** y las mejores prácticas 
de seguridad y despliegue profesional. [cite: 8, 19, 30]
""")

# Mostrar la planificación resumida por parciales
col1, col2, col3 = st.columns(3)

with col1:
    st.info("### Parcial 1\n**Monolitos y ORM** [cite: 7]")
    st.write("Fundamentos de Django, Modelos, Forms y Templates.")

with col2:
    st.success("### Parcial 2\n**APIs REST & CBV** [cite: 18]")
    st.write("Django REST Framework, Serializers y ViewSets.")

with col3:
    st.warning("### Parcial 3\n**Optimización & Seguridad** [cite: 29]")
    # st.write("JWT, Middlewares, Signals y Dockerización.")

st.divider()

st.markdown("""
A continuación se presenta el desglose de temas por parcial. Este temario es la referencia visual para el cumplimiento de los objetivos de la asignatura.
""")

# --- TABULADORES DE TEMARIO VISUAL ---
tab1, tab2, tab3 = st.tabs([
    "📦 PARCIAL 1: Arquitectura Monolítica",
    "🔌 PARCIAL 2: APIs REST & Microservicios",
    "🛡️ PARCIAL 3: Optimización & Seguridad"
])

with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("### Objetivo\nDominar el ciclo Request-Response, el ORM y el renderizado desde el servidor (SSR)[cite: 3, 5].")
    with col2:
        st.markdown("""
        **Contenido Temático:**
        *   **S1-S2:** Introducción a Django, entornos virtuales (`venv`) y estructura de proyectos[cite: 3, 4].
        *   **S3-S4:** El ORM: Modelos, tipos de datos, migraciones y relaciones (1:N, N:N)[cite: 5, 6].
        *   **S5:** Django Forms: Validaciones de ingeniería y seguridad CSRF[cite: 7].
        *   **S6:** Vistas basadas en funciones (FBV) y lógica de persistencia[cite: 8].
        *   **S7:** Motor de Plantillas: Herencia de bloques (`extends`, `block`) y filtros[cite: 9].
        *   **S8:** Class-Based Views (CBV): Automatización con `ListView` y `DetailView`[cite: 10].
        *   **S9:** **Evaluación Parcial 1:** Proyecto CRUD Monolítico con Bootstrap[cite: 12].
        """)

with tab2:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.success("### Objetivo\nTransicionar de aplicaciones monolíticas a servicios de datos desacoplados mediante DRF[cite: 13, 14].")
    with col2:
        st.markdown("""
        **Contenido Temático:**
        *   **S10:** Introducción a Django REST Framework (DRF) y configuración de CORS[cite: 13].
        *   **S11:** Serializers: Traducción de Modelos a JSON y validaciones de API.
        *   **S12:** APIView: Implementación de métodos HTTP (GET, POST, PUT, DELETE)[cite: 15].
        *   **S13:** Generic Views: Automatización con `ListCreate` y `RetrieveUpdateDestroy`[cite: 16].
        *   **S14-S15:** ViewSets y Routers: Abstracción máxima y personalización de `get_queryset`[cite: 17, 18].
        *   **S16:** Documentación interactiva: Implementación de OpenAPI/Swagger con `drf-spectacular`[cite: 19].
        *   **S17:** Taller de Integración: Pruebas con Postman y consumo externo[cite: 20].
        *   **S18:** **Evaluación Parcial 2:** Desarrollo de una API REST profesional documentada[cite: 21].
        """)

with tab3:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.warning("### Objetivo\nImplementar control de bajo nivel sobre la base de datos y asegurar el entorno de producción[cite: 23, 29].")
    with col2:
        st.markdown("""
        **Contenido Temático:**
        *   **S19-S20:** SQL Puro en Django: Uso de `connection.cursor()` para SELECT, INSERT y UPDATE[cite: 23, 24].
        *   **S21:** Batch Processing: Optimización con `bulk_create` y `executemany`[cite: 25].
        *   **S22:** Middlewares: Intercepción del ciclo de vida y auditoría de peticiones[cite: 26].
        *   **S23:** Signals: Automatización de disparadores (Triggers) en Python[cite: 27].
        *   **S24:** Seguridad en Producción: Variables de entorno (`.env`) y conexión remota a MySQL[cite: 28, 29].
        *   **S25:** **Evaluación Final:** Proyecto Integrador Fullstack (API Optimizado + Signals)[cite: 21].
        """)

#st.sidebar.success("Selecciona una Sesión arriba para comenzar.")
