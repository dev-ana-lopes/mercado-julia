from produto import Produto
from fornecedor import Fornecedor
from estoque import Estoque
def main():
    estoque = Estoque()

    # --teste da classe produto
    produto1 = Produto("Sabão em pó - OMO", "0001", 19.9590, "Unidade", 50)
    produto2 = Produto("Detergente neutro - Ype", "0002", 1.99, "Unidade", 12)
    produto1.set_preco(15.90259)
    produto2.set_eh_ativo(False)


    # --teste da classe fornecedor
    fornecedor1 = Fornecedor("Jose", "0001", "Rua da felicidade, 32 - Maringa/PR", 44984387858)
    fornecedor2 = Fornecedor("Lucas", "0002", "Rua da felicidade, 32 - Maringa/PR", 44984387858)
    fornecedor1.set_eh_ativo(False)
    fornecedor2.set_eh_ativo(False)

    # --teste da classe estoque
    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)
    #estoque.listar_todos_produtos()
    #estoque.listar_produtos_ativos()
    #print(estoque.buscar_por_codigo("0001"))
    print(estoque.adicionar_quantidade_itens("0001", 50))
    print(estoque.baixar_quantidade_itens("0001", 20))
    
    



if __name__ == "__main__":
    main()
