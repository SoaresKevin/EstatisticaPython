valores = []
opcao = 0

itens = input("Digite os itens que deseja trabalhar separados por (/):")
valores = itens.split('/')
for item in valores:
    print(item)