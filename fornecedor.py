from typing import Optional

class Fornecedor:
    def __init__(self, nome: str, cnpj: str, endereco: str, contato: int):
        self._nome = nome
        self._cnpj = cnpj
        self._endereco = endereco
        self._contato = contato
        self._eh_ativo = True
    
    def get_nome(self):
        return self._nome

    def get_cnpj(self):
        return self._cnpj

    def get_endereco(self):
        return self._endereco
    
    def get_contato(self):
        return self._contato
    
    def get_eh_ativo(self):
        return self._eh_ativo
    
    def set_eh_ativo(self, eh_ativo):
        self._eh_ativo = eh_ativo
    
    def __str__(self) -> str:
        return f"Nome: {self.get_nome()}, CNPJ: {self.get_cnpj()}, Endereço: {self.get_endereco()}, Contato: {self.get_contato()} - Está ativo? {self.get_eh_ativo()}"