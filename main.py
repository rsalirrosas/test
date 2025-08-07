import streamlit as st
import numpy as np

st.title("Calculadora de IMC")

cantidad_personas = st.number_input("Ingrese la cantidad de personas a calcular:", min_value=1, step=1)

if cantidad_personas:
    array_IMC = np.zeros(cantidad_personas)

    for i in range(cantidad_personas):
        st.write(f"### Persona {i+1}")
        peso = st.number_input(f"Ingrese el peso (kg) de la persona {i+1}:", key=f"peso_{i}")
        estatura = st.number_input(f"Ingrese la estatura (m) de la persona {i+1}:", key=f"estatura_{i}")
        
        if estatura > 0:
            imc = peso / estatura**2
            array_IMC[i] = imc
            st.success(f"IMC Persona {i+1}: {imc:.2f}")
    
    if st.button("Calcular promedio"):
        promedio = array_IMC.mean()
        st.write(f"### El IMC promedio de {cantidad_personas} personas es: {promedio:.2f}")
