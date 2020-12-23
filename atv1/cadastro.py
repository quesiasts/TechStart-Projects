class Produtos:

    def __init__(self, nome, preco): 
        self.nome = nome
        self.preco = preco

class Interface:

    produtos = []

    def cadastrar_produto(self):
        nome = input('Qual é o nome do Produto?\n')
        preco = input('Qual o preço?')

        self.produtos.append(Produtos(nome, preco))
        print('Produto adicionado!')

    def listar_produtos(self):
        for i, Produtos in enumerate(self.produtos):
            print(i, Produtos.nome, Produtos.preco)

    def loop(self):
        while True:
            cmd = input('\n1 - Listar produtos\n2 - Cadastrar produto\n')
            if cmd == '1':
                self.listar_produtos()
            elif cmd == '2':
                self.cadastrar_produto()
            else:
                print('Não entendi!')
                continue


if __name__ == '__main__':
    interface = Interface()
    interface.loop()
