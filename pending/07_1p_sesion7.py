import streamlit as st

st.title("🍱 Sesión 7: Componentes de Bootstrap")
st.subheader("Construcción de Interfaces Profesionales y Estilizadas")

# --- SECCIÓN 1: NAVBAR (Navegación) ---
st.header("1. Navbar: La Brújula del Sitio")
st.write("Es el componente más complejo pero esencial. Debe ser colapsable para dispositivos móviles.")
st.code("""
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Ing. Software</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item"><a class="nav-link active" href="#">Inicio</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Tareas</a></li>
      </ul>
    </div>
  </div>
</nav>
""", language="html")

st.divider()

# --- SECCIÓN 2: CARDS (Contenedores de Datos) ---
st.header("2. Cards: Presentando Información del Backend")
st.write("Ideal para mostrar objetos de una base de datos (productos, tareas, usuarios)[cite: 31].")
st.code("""
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Título de la Tarea</h5>
    <h6 class="card-subtitle mb-2 text-muted">Prioridad Alta</h6>
    <p class="card-text">Descripción breve que viene desde el ORM de Django.</p>
    <a href="#" class="btn btn-primary">Editar</a>
    <a href="#" class="btn btn-danger">Eliminar</a>
  </div>
</div>
""", language="html")

st.divider()

# --- SECCIÓN 3: MODALS (Interacción) ---
st.header("3. Modals: Diálogos de Confirmación")
st.warning("Nota: Los Modals requieren el archivo JavaScript de Bootstrap para funcionar[cite: 31].")
st.code("""
<!-- Botón que dispara el modal -->
<button type="button" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="#deleteModal">
  Borrar Tarea
</button>

<!-- Estructura del Modal -->
<div class="modal fade" id="deleteModal" tabindex="-1">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">¿Estás seguro?</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>
      <div class="modal-body">Esta acción no se puede deshacer en la base de datos MySQL.</div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
        <button type="button" class="btn btn-danger">Confirmar Borrado</button>
      </div>
    </div>
  </div>
</div>
""", language="html")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 8)")
st.markdown("""
1.  **Investigación**: ¿Qué son los **Breakpoints** en Bootstrap y qué significan las siglas `sm`, `md`, `lg` y `xl`?[cite: 31]
2.  **Práctica**: Intenta cambiar el color de un botón de Bootstrap usando clases como `btn-success`, `btn-outline-info` o `btn-lg`[cite: 12].
3.  **Reflexión IA**: Pregunta a la IA: *"¿Cómo puedo usar clases de utilidades de Bootstrap para centrar un Card horizontalmente sin escribir CSS personalizado?"*
""")