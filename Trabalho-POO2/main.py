class UI:

    @staticmethod
    def menu():
        s = f"Qual das seguintes opções você deseja executar?\n"
        s += f"1. Inserir cliente;\n"
        s += f"2. Excluir cliente;\n"
        s += f"3. Atualizar cliente;\n"
        s += f"4. Listar clientes;\n"
        s += f"10. Encerrar programa.\n"
        return int(input(f"{s}\nInsira sua escolha: "))
    
    
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = UI.menu()
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_excluir()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_listar()


UI.main()