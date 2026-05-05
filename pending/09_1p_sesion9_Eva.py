import streamlit as st

st.title("🏁 Sesión 9: Evaluación Parcial 1")
st.subheader("Proyecto Integrador: Maquetación de Monolito")

# --- INDICACIONES DEL EXAMEN ---
st.header("1. Instrucciones del Reto")
st.write("""
Deberás aplicar los estilos de Frontend a tu proyecto de Django del Parcial 1. 
La entrega consiste en el repositorio de GitHub con el código actualizado.
""")

with st.expander("✅ Checklist de Requisitos Técnicos"):
    st.markdown("""
    - [ ] **Estructura:** El archivo `base.html` debe usar etiquetas semánticas de HTML5.
    - [ ] **Navegación:** Un `navbar` responsivo que incluya enlaces a 'Inicio' y 'Nueva Tarea'.
    - [ ] **Visualización:** La lista de registros (de tu ListView) debe mostrarse en `Cards` de Bootstrap[cite: 10, 31].
    - [ ] **Formularios:** Uso de clases de Bootstrap (`form-control`) mediante `django-widget-tweaks`[cite: 12].
    - [ ] **Interacción:** El borrado debe solicitar confirmación mediante un `Modal` o una alerta estilizada[cite: 12, 31].
    """)

st.divider()

# --- LABORATORIO DE IA ---
st.header("🤖 IA como Consultora de Estilo")
st.info("Puedes usar la IA para pulir los detalles finales de tu entrega:")
st.markdown("""
> **Prompt de apoyo:** 
> *'Actúa como un experto en UI/UX. Analiza mi estructura de tarjetas de Bootstrap y sugiere cómo mejorar el espaciado (padding/margin) y las sombras (shadows) para que la lista de tareas de mi proyecto Django sea más legible y profesional.'*
""")

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Hacia el Parcial 2)")
st.markdown("""
1. **Investigación:** ¿Qué es **JavaScript Vanilla** y por qué es importante entenderlo antes de usar frameworks como React o Vue?[cite: 31]
2. **Preparación:** Asegúrate de tener instalado **Node.js** en tu equipo (opcional pero recomendado para herramientas futuras).
3. **Reflexión:** En el próximo parcial dejaremos de renderizar HTML desde Django y empezaremos a pedir solo datos JSON. ¿Cómo crees que cambiará tu código JS?[cite: 13, 31]
""")