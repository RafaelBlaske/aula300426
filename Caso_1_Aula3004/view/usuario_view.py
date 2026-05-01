class ProdutoView:

    def mostrar_menu(self):
        print("1 - Criar produto")
        print("2 - Listar produtos")
        print("0 - Sair")

    def obter_dados_produto(self):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        return nome, preco

    def mostrar_produtos(self, produtos):
        print("\n=== Produtos ===")
        for p in produtos:
            print(f"{p.id} - {p.nome} (R$ {p.preco:.2f})")
        print("================")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)