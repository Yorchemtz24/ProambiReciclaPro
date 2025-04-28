import streamlit as st
import pandas as pd

# Cargar los datos desde el Excel
@st.cache_data
def cargar_datos():
    return pd.read_excel('operaciones_hoe.xlsx')

df = cargar_datos()

st.title("ProambiReciclaPro")

# Entradas del usuario
equipo = st.selectbox("Selecciona el tipo de equipo:", df['Equipo'].unique())
costo_hora = st.number_input("Costo de mano de obra ($/hora):", value=60)

if st.button("Generar HOE"):
    operaciones = df[df['Equipo'] == equipo]
    tiempo_total = operaciones['Tiempo (min)'].sum()
    costo_estimado = (tiempo_total / 60) * costo_hora

    st.subheader("Operaciones sugeridas:")
    for idx, row in operaciones.iterrows():
        st.write(f"- {row['Operación']} ({row['Tiempo (min)']} min)")

    st.markdown("---")
    st.write(f"**Tiempo Total:** {tiempo_total} minutos")
    st.write(f"**Costo Estimado:** ${costo_estimado:.2f}")
