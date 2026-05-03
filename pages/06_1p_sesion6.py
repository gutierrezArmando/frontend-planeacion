import streamlit as st

st.title("🚀 Sesión 6: Bootstrap 5 - El Grid System")
st.subheader("Maquetación Profesional Basada en 12 Columnas")

# --- SECCIÓN 1: INSTALACIÓN RÁPIDA ---
st.header("1. ¿Cómo incluir Bootstrap?")
st.write("Para proyectos de clase, usamos el CDN (Content Delivery Network) en el `<head>` del HTML.")
st.code("""
<!-- Enlace de Bootstrap 5 -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
""", language="html")

st.divider()

# --- SECCIÓN 2: EL SISTEMA DE REJILLA ---
st.header("2. El Sistema de 12 Columnas")
st.write("Bootstrap divide el ancho en 12. Tú decides cuántas toma cada elemento.")

st.code("""
<div class="container">
    <div class="row">
        <div class="col-md-8"> 
            <!-- Ocupa 8 de 12 columnas en pantallas medianas -->
            <h3>Contenido Principal (Backend Data)</h3>
        </div>
        <div class="col-md-4">
            <!-- Ocupa las 4 restantes -->
            <h3>Barra Lateral</h3>
        </div>
    </div>
</div>
""", language="html")

st.divider()

# --- SECCIÓN 3: UTILIDADES DE ESPACIADO ---
st.header("3. Espaciado: Margin y Padding")
st.write("Bootstrap usa una sintaxis abreviada para el Box Model: `{propiedad}{lado}-{tamaño}`[cite: 31].")

st.markdown("""
*   **m** (margin), **p** (padding)[cite: 31].
*   **t** (top), **b** (bottom), **s** (start/left), **e** (end/right), **x** (horizontal), **y** (vertical)[cite: 31].
*   **Ejemplo:** `mt-5` aplica un margen superior grande; `px-2` aplica un padding horizontal pequeño[cite: 12, 31].
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 7)")
st.markdown("""
1.  **Investigación:** Busca en la [documentación de Bootstrap](https://getbootstrap.com/docs/5.3/components/card/) qué es un **Card** y un **Navbar**.
2.  **Práctica:** Intenta crear una fila con 4 columnas iguales. ¿Qué clases de `col` deberías usar? (Pista: 12 / 4 = ?)[cite: 31].
3.  **Reflexión IA:** Pregunta a la IA: *"¿Por qué Bootstrap usa la unidad 'rem' para el espaciado en lugar de 'px'?"*
""")