from eq_2_grau import Eq_2_grau
import streamlit as st

class Eq_2_grau_UI:
    def main():
        st.header("Equação do II grau:")
        a = st.text_input("a")
        b = st.text_input("b")
        c = st.text_input("c")
        if st.button("Calcular"):
            e = Eq_2_grau(float(a), float(b), float(c))
            st.write(e)
            st.write(f"Delta = {e.delta():.2f}")
            st.write(f"x1: {e.mais_delta():.2f}")
            st.write(f"x2: {e.menos_delta():.2f}")