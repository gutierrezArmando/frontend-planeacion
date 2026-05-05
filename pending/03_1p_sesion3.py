import streamlit as st

st.title("🎨 Sesión 3: CSS3 Fundamental")
st.subheader("Selectores, Cascada y la Matemática del Box Model")

# --- SECCIÓN 1: SELECTORES Y ESPECIFICIDAD ---
st.header("1. ¿Quién gana? La Cascada")
st.write("En CSS, el orden y la especificidad determinan qué estilo se aplica finalmente.")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Jerarquía de Selectores:**")
    st.code("""
/* 1. Etiqueta (Baja) */
p { color: black; }

/* 2. Clase (Media) */
.texto-rojo { color: red; }

/* 3. ID (Alta - Evitar para estilos) */
#titulo-unico { color: blue; }

/* 4. Estilo en línea (Extrema - NO USAR) */
<p style="color: green;">...</p>
    """, language="css")

with col2:
    st.info("### 🤖 Reto de IA: Especificidad")
    st.write("Usa este prompt para entender conflictos:")
    st.markdown("> *'Tengo un botón con una clase .btn y un ID #enviar. Si en mi CSS .btn tiene background: red y #enviar tiene background: blue, ¿de qué color será el botón y por qué técnicamente sucede esto?'*")

st.divider()

# --- SECCIÓN 2: EL BOX MODEL ---
st.header("2. El Modelo de Caja (Matemáticas de UI)")
st.write("Como ingenieros, debemos calcular el ancho total de un elemento:")

st.latex(r'''
Ancho\ Total = Width + (Padding \times 2) + (Border \times 2) + (Margin \times 2)
''')

st.success("💡 **Tip de Oro:** Usa `box-sizing: border-box;` en todo tu proyecto para que el padding y border no sumen al ancho definido[cite: 31].")

# --- SECCIÓN 3: HERENCIA ---
st.header("3. Herencia: Propiedades que se pasan de padres a hijos")
st.code("""
body {
    font-family: Arial; /* Se hereda a todos los hijos */
    color: #333;        /* Se hereda */
    border: 1px solid black; /* NO se hereda */
}
""", language="css")

st.divider()

# --- AULA INVERTIDA ---
st.warning("### 🏫 Aula Invertida (Preparación Sesión 4)")
st.markdown("""
1.  **Investigación:** ¿Cuál es la diferencia entre `display: block`, `display: inline` y `display: inline-block`?[cite: 31]
2.  **Práctica:** Intenta centrar un `div` dentro de otro usando solo `margin: auto;`. ¿Funciona siempre?
3.  **Exploración IA:** Pregunta a la IA: *"¿Qué es Flexbox y por qué vino a solucionar los problemas de diseño que teníamos con floats?"*[cite: 31]
""")