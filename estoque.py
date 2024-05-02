from produto import Produto

class Estoque:

    _instance = None

    def __init__(self):
        Estoque._instance = self
        self._produtos = []

    def get_instance():
        Estoque._instance = Estoque()
        return Estoque._instance

    def adicionar_produto(self, produto):
        self._produtos.append(produto)

    def adicionar_quantidade_itens(self, codigo_barras, quantidade):
        produto = self.buscar_por_codigo(codigo_barras)
        if produto:
            produto.set_qtd_itens((produto.get_qtd_itens() + quantidade))
            return f"Quantidade do item atualizada para {produto.get_qtd_itens()}"

    def baixar_quantidade_itens(self, codigo_barras, quantidade):
        produto = self.buscar_por_codigo(codigo_barras)
        if produto:
            produto.set_qtd_itens((produto.get_qtd_itens() - quantidade))
            return f"Quantidade do item atualizada para {produto.get_qtd_itens()}"

    def remover_produto(self, produto):
        produto.set_eh_ativo = False
        self._produtos.remove(produto)
    
    def listar_todos_produtos(self):
        for produto in self._produtos:
            print(produto)
    
    def listar_produtos_ativos(self):
        for produto in self._produtos:
            if produto.get_eh_ativo():
                print(produto)

    def buscar_por_codigo(self, codigo_barras):
        for produto in self._produtos:
            if produto.get_eh_ativo():
                if produto.get_codigo_barras() == codigo_barras:
                    return produto
        return None


    

    
