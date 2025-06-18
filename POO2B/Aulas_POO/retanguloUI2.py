import streamlit as st
from POO2B.Aulas_POO.retangulo import Retangulo

class RetanguloUI2:
    def main():
        st.header("Cálculos com retângulo:")
        b = input("Base")
        h = input("Altura")
        if st.button("Calcular"):
            r = Retangulo(float(b), float(h))
            print(r)
            print(f"Área do retângulo: {r.calc_area():.2f}")
            print(f"Diagonal do retângulo: {r.calc_diagonal():.2f}")