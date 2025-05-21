import classes

class UI:

    @staticmethod
    def menu():
        s = f"Qual das seguintes opções você deseja executar?\n"
        s += f"1. Inserir cliente\n"
        s += f"2. Excluir cliente\n"
        s += f"3. Atualizar cliente\n"
        s += f"4. Listar clientes\n"
        s += f"10. Encerrar programa.\n"
        return int(input(s))
    
    @staticmethod
    def main():
        op = UI.menu()
        while op != 10:
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_excluir()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_listar()

    @staticmethod
    def cliente_listar():
        x = 1

    @staticmethod
    def cliente_inserir():
        x = 1

    @staticmethod
    def cliente_atualizar():
        x = 1
    
    @staticmethod
    def cliente_excluir():
        x = 1


    pass

UI.main()