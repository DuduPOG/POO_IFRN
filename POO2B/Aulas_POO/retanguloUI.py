import streamlit as st
from POO2B.Aulas_POO.retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com retângulo:")
        b = st.text_input("Base")
        h = st.text_input("Altura")
        if st.button("Calcular"):
            r = Retangulo(float(b), float(h))
            st.write(r)
            st.write(f"Área do retângulo: {r.calc_area():.2f}")
            st.write(f"Diagonal do retângulo: {r.calc_diagonal():.2f}")