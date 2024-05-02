from produto import Produto
def main():
    produto1 = Produto("Omo", "0001", 19.9590, "Unidade", 50)
    print(produto1)
    produto1.set_preco(15.90259)
    print(produto1)

if __name__ == "__main__":
    main()
