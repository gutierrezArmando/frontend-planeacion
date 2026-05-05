import streamlit as st

st.title("📱 Sesión 8: Personalización y Responsive Design")
st.subheader("Media Queries vs. Clases Utilitarias")

# --- SECCIÓN 1: BREAKPOINTS ---
st.header("1. Los Puntos de Interrupción (Breakpoints)")
st.write("Como ingenieros, diseñamos para un ecosistema de dispositivos. Bootstrap usa estos prefijos:")

st.markdown("""
| Prefijo | Dispositivo | Tamaño |
| :--- | :--- | :--- |
| **(ninguno)** | Móvil | < 576px |
| **sm** | Tablet (vertical) | ≥ 576px |
| **md** | Tablet (horizontal) | ≥ 768px |
| **lg** | Laptop | ≥ 992px |
| **xl** | Desktop | ≥ 1200px |
""")

st.divider()

# --- SECCIÓN 2: CLASES UTILITARIAS ---
st.header("2. El poder de las Clases Utilitarias")
st.write("¿Por qué escribir CSS manual si Bootstrap ya lo tiene? Ejemplo de visibilidad y orden:")

st.code("""
<!-- Ocultar en móvil, mostrar en desktop -->
<div class="d-none d-lg-block">
  Solo me veo en pantallas grandes
</div>

<!-- Cambiar el orden de las columnas en móvil -->
<div class="row">
  <div class="col-12 order-2 col-md-8 order-md-1">Contenido Principal</div>
  <div class="col-12 order-1 col-md-4 order-md-2">Publicidad (Aparece primero en móvil)</div>
</div>
""", language="html")

st.divider()

# --- SECCIÓN 3: LABORATORIO DE IA ---
st.header("🤖 Laboratorio de IA: El Optimizador Responsivo")
st.info("Utiliza este prompt para resolver problemas de diseño móvil:")
st.markdown("""
> **Prompt sugerido:** 
> *'Tengo una fila de Bootstrap con 4 columnas. Quiero que en móvil se vea una sola columna por fila (1x4), en tablet se vean dos columnas (2x2) y en desktop se vean las cuatro (4x1). ¿Qué clases exactas de Bootstrap 5 debo usar y por qué?'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 9 - Evaluación)")
st.markdown("""
1.  **Repaso General:** Asegúrate de que tu proyecto del Parcial 1 de Backend esté corriendo[cite: 12].
2.  **Práctica:** Intenta crear un "Hero Section" (un encabezado grande con imagen de fondo) que cambie la alineación del texto de centrado (móvil) a izquierda (desktop)[cite: 31].
3.  **Reflexión IA:** Pregunta a la IA: *"¿Cuándo es mejor escribir una Media Query personalizada en lugar de usar clases de Bootstrap?"*
""")