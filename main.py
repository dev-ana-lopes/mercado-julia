from produto import Produto
from fornecedor import Fornecedor
def main():
    #teste da classe produto
    produto1 = Produto("Sabão em pó - OMO", "0001", 19.9590, "Unidade", 50)
    produto2 = Produto("Detergente neutro - Ype", "0002", 1.99, "Unidade", 12)
    print(produto1)
    print(produto2)
    produto1.set_preco(15.90259)
    produto2.set_eh_ativo(False)
    print(produto1)
    print(produto2)

    #teste da classe fornecedor
    fornecedor1 = Fornecedor("Jose", "0001", "Rua da felicidade, 32 - Maringa/PR", 44984387858)
    print(fornecedor1)


if __name__ == "__main__":
    main()
