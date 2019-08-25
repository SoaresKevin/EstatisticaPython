import util

valores = []
opcao = 0
linhas_num = int(input("Quantas linhas de dados deseja trabalhar?"))

for x in range(0,linhas_num): 
    itens = input("Digite os itens que deseja trabalhar separados por (/):")
    valores += itens.split('/')
valores = map(int, valores)
valores_sort = sorted(valores)

for x in teste:
    print(x)

