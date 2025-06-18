import streamlit as st
from view import View

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar"], ["Inserir"], ["Atualizar"], ["Excluir"])
        with tab1:
            ManterCategoriaUI.listar()
        with tab2:
            ManterCategoriaUI.inserir()
        with tab3:
            ManterCategoriaUI.atualizar()
        with tab4:
            ManterCategoriaUI.excluir()

        def listar():
            st.write("Listar")
        
        def inserir():
            if st.button("Inserir"):
                nome = st.text_input("Nome")
                email = st.text_input("Email")
                fone = st.text_input("Telefone")
                View.cliente_inserir(nome, email, fone)
            st.write("Inserir")