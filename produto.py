class Produto:
    def __init__(self, nome: str, codigo_barras: str, preco: float, unidade_medida: str, qtd_itens: int, eh_ativo: bool = True):
        self._nome = nome
        self._codigo_barras = codigo_barras
        self._unidade_medida = unidade_medida
        self._qtd_itens = qtd_itens
        self._preco = round(preco, 2)
        self._eh_ativo = eh_ativo

    def get_nome(self):
        return self._nome
    
    def get_codigo_barras(self):
        return self._codigo_barras
    
    def get_unidade_medida(self):
        return self._unidade_medida
    
    def get_qtd_itens(self):
        return self._qtd_itens
    
    def get_preco(self):
        return self._preco
    
    def get_eh_ativo(self):
        return self._eh_ativo
    
    def set_preco(self, preco):
        self._preco = round(preco, 2)

    def set_eh_ativo(self, eh_ativo):
        self._eh_ativo = eh_ativo
    
    def set_qtd_itens(self, qtd_itens):
        self._qtd_itens = qtd_itens

    def __str__(self) -> str:
        return f"Nome: {self.get_nome()}, Código de barras: {self.get_codigo_barras()}, Preço: {self.get_preco()}, Quantidade: {self.get_qtd_itens()}/{self.get_unidade_medida()} - Está ativo? {self.get_eh_ativo()}"


