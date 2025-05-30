from datetime import datetime
from categoria import Categoria, Categorias
from cliente import Cliente, Clientes
from produto import Produto, Produtos
from venda import Venda, Vendas
from venda_item import VendaItem, VendaItens

class UI:
    carrinho = None #atributo de classe
    @staticmethod
    def menu():
        s = f"Qual das seguintes opções você deseja executar?\n"
        s += f"\n1. Inserir cliente;\n"
        s += f"2. Excluir cliente;\n"
        s += f"3. Atualizar cliente;\n"
        s += f"4. Listar clientes;\n"
        s += f"\n5. Inserir categoria;\n"
        s += f"6. Excluir categoria;\n"
        s += f"7. Atualizar categoria;\n"
        s += f"8. Listar categorias;\n"
        s += f"\n9. Inserir produto;\n"
        s += f"10. Excluir produto;\n"
        s += f"11. Atualizar produto;\n"
        s += f"12. Listar produtos;\n"
        s += f"\n13. Iniciar carrinho de compras;\n"
        s += f"14. Listar as compras\n"
        s += f"15. Inserir produto no carrinho;\n"
        s += f"16. Confirmar compra;\n"
        s += f"\n100. Encerrar programa.\n"
        return int(input(f"{s}\nInsira sua escolha: "))
    
    
    @staticmethod
    def main():
        op = 0
        while op != 100:
            op = UI.menu()
            if op == 1:
                UI.cliente_inserir()
            elif op == 2:
                UI.cliente_excluir()
            elif op == 3:
                UI.cliente_atualizar()
            elif op == 4:
                UI.cliente_listar()
            elif op == 5:
                UI.categoria_inserir()
            elif op == 6:
                UI.categoria_excluir()
            elif op == 7:
                UI.categoria_atualizar()
            elif op == 8:
                UI.categoria_listar()
            elif op == 9:
                UI.produto_inserir()
            elif op == 10:
                UI.produto_excluir()
            elif op == 11:
                UI.produto_atualizar()
            elif op == 12:
                UI.produto_listar()
            elif op == 13:
                UI.iniciar_compra()
            elif op == 14:
                UI.listar_compras()
            elif op == 15:
                UI.venda_item_inserir()
            elif op == 16:
                UI.confirmar_compra()



    #CRUD de cliente
    @staticmethod
    def cliente_inserir():#Create
        id = int(input("Informe o ID do cliente: "))
        nome = input("Informe seu nome: ")
        email = input("Informe seu email: ")
        fone = input("Informe seu telefone: ")
        x = Cliente(id, nome, email, fone)
        Clientes.inserir(x)

    
    @staticmethod
    def cliente_excluir():#Delete
        UI.cliente_listar
        id = int(input("Informe o ID do cliente que será excluído: "))
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)


    @staticmethod
    def cliente_atualizar():#Update
        UI.cliente_listar
        id = int(input("Informe o ID do cliente a ser atualizado: "))
        nome = input("Informe seu novo nome: ")
        email = input("Informe seu novo email: ")
        fone = input("Informe seu novo telefone: ")
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)


    @staticmethod
    def cliente_listar():#Read
        print("Estes são todos os clientes cadastrados:")
        for c in Clientes.listar():
            print(c)


    #CRUD de categoria
    @staticmethod
    def categoria_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para sua categoria: ")
        x = Categoria(0, desc)
        Categorias.inserir(x)

    
    @staticmethod
    def categoria_excluir():#Delete
        UI.categoria_listar
        id = int(input("Informe o ID da categoria que será excluída: "))
        c = Categoria(id, "")
        Categorias.excluir(c)


    @staticmethod
    def categoria_atualizar():#Update
        UI.categoria_listar
        id = int(input("Informe o ID da categoria a ser atualizada: "))
        desc = input("Informe sua nova descrição: ")
        c = Categoria(id, desc)
        Categorias.atualizar(c)


    @staticmethod
    def categoria_listar():#Read
        print("Estas são todas as categorias existentes:")
        for c in Categorias.listar():
            print(c)


    #CRUD de produto
    @staticmethod
    def produto_inserir():#Create
        #id = int(input("Informe o ID do cliente: "))
        desc = input("Informe uma descrição para seu produto: ")
        preco = input("Informe seu preço: ")
        estoque = input("Informe a quantidade no estoque: ")
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID da categoria desejada: "))
        x = Produto(0, desc, preco, estoque, id_categoria)
        Produtos.inserir(x)

    
    @staticmethod
    def produto_excluir():#Delete
        UI.produto_listar
        id = int(input("Informe o ID do produto que será excluído: "))
        c = Produto(id, "", "", "", "")
        Produtos.excluir(c)


    @staticmethod
    def produto_atualizar():#Update
        UI.produto_listar
        id = int(input("Informe o ID do produto a ser atualizado: "))
        desc = input("Informe sua nova descrição: ")
        preco = input("Informe seu novo preço: ")
        estoque = input("Informe sua nova quantidade em estoque: ")
        UI.categoria_listar()
        id_categoria = int(input("Informe o ID do novo produto: "))
        c = Produto(id, desc, preco, estoque, id_categoria)
        Produtos.atualizar(c)


    @staticmethod
    def produto_listar():#Read
        print("Estes são todos os produtos disponíveis:")
        for c in Produtos.listar():
            print(c)


    #CRUD de Venda
    @classmethod
    def iniciar_compra(cls):#Create
        v = Venda(0)        
        Vendas.inserir(v)
        cls.carrinho = v


    @classmethod
    def venda_item_inserir(cls):
        print("O produto vai ser inserido nesse carrinho: ", cls.carrinho)
        """
        UI.produto_listar
        id_produto = int(input("Insira o ID do produto desejado: "))
        id_categoria = int(input("Insira o ID da categoria do produto: "))
        qtd = int(input("Qual a quantidade do produto desejada?: "))
        x = VendaItem(0, qtd, qtd*2, id_categoria, id_produto)
        """


    
    @staticmethod
    def cancelar_compra():#Delete
        UI.listar_compras
        id = int(input("Informe o ID da venda que será excluída: "))
        c = Venda(id, "", "", "")
        Vendas.excluir(c)


    @staticmethod
    def mudar_compra():#Update
        UI.listar_compras
        id = int(input("Informe o ID da compra a ser atualizada: "))
        data = datetime.now()
        carrinho = True
        UI.cliente_listar
        id_cliente = int(input("Informe seu novo ID (caso queira trocar): "))
        c = Venda(id, data, carrinho, id_cliente)
        Vendas.atualizar(c)


    @staticmethod
    def listar_compras():#Read
        print("Estas são todas as Vendas:")
        for c in Vendas.listar():
            print(c)


UI.main()