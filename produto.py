from typing import Optional
class Produto:
    def __init__(self, nome: str, codigo_barras: str, preco: float, unidade_medida: str, qtd_itens: int):
        self._nome = nome
        self._codigo_barras = codigo_barras
        self._unidade_medida = unidade_medida
        self._qtd_itens = qtd_itens
        self._preco = round(preco, 2)

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
    
    def set_preco(self, preco):
        self._preco = round(preco, 2)

    def __str__(self):
        return f"Código de barras: {self.get_codigo_barras()}, Nome: {self.get_nome()}, Preço: {self.get_preco()}, Quantidade: {self.get_qtd_itens()}/{self.get_unidade_medida()}"

    