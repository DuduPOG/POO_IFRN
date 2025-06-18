import streamlit as st
from view import View

class ManterClienteUI:
    @staticmethod
    def main():
        st.header("Cadastro de clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar"], ["Inserir"], ["Atualizar"], ["Excluir"])
        with tab1:
            ManterClienteUI.listar()
        with tab2:
            ManterClienteUI.inserir()
        with tab3:
            ManterClienteUI.atualizar()
        with tab4:
            ManterClienteUI.excluir()

        @staticmethod
        def listar():
            st.write("Listar")
        
        @staticmethod
        def inserir():
            if st.button("Inserir"):
                nome = st.text_input("Nome")
                email = st.text_input("Email")
                fone = st.text_input("Telefone")
                View.cliente_inserir(nome, email, fone)
            st.write("Inserir")