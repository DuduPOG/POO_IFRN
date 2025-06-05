from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas
from venda_item import VendaItem, VendaItens
from login import Login, Logins


class View:


    def cadastrar_admin():
        for cliente in Clientes.listar():
            if cliente.email == "admin":
                return
        View.cliente_inserir("admin", "admin", "84911223344")


    def cliente_inserir(nome, email, fone):
        x = Cliente(0, nome, email, fone)
        Clientes.inserir(x)
        pass


    def cliente_listar():
        return Clientes.listar()


    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)


    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)
        pass


    def inserir_no_carrinho(id_carrinho, id_produto, qtd):
        preco = float(Produtos.listar_id(id_produto).preco)
        vi = VendaItem(0, qtd, preco)
        vi.id_venda = id_carrinho
        vi.id_produto = id_produto
        VendaItens.inserir(vi)
        #atualizar o total da venda (carrinho)
        carrinho = Vendas.listar_id(id_carrinho)
        subtotal = qtd * preco
        carrinho.total += subtotal
        Vendas.atualizar(carrinho)

    pass