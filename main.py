import util
import statistics   
from Moda import Moda

from datetime import datetime 

now = datetime.now() 
hora = str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)

arquivo = "txt_s/"+hora+".txt"

arquivo = open(arquivo, "w")

valores = []
val_sorted = []
stage = "Dev"
media = 0

if stage == "Production":
    linhas_num = int(input("Quantas linhas de dados deseja trabalhar?"))

    for x in range(0,linhas_num): 
        itens = input("Digite os itens que deseja trabalhar separados por (/):")
        valores += itens.split('/')
else:
    itens = "80/85/90"
    valores = itens.split('/')

valores = map(float, valores)
val_sorted = sorted(valores)

print_valores = []
i = 0
msg = ""
for x in val_sorted:
    msg += str(x)+"/" 
    i += 1
    if i == 12:
        i = 0   
        print_valores.append(msg)
        msg = ""

if msg != "" :
    print_valores.append(msg)


print("-------------------------------------")
arquivo.write('-------------------------------------\n')
for y in print_valores:
    print(y)
    arquivo.write(y+"\n")
arquivo.write('-------------------------------------\n')
print("-------------------------------------")

media = statistics.mean(val_sorted)

msg = u"Media dos dados e de "+ str(round(media,6)) +'\n'
print(msg) 
arquivo.write(msg)

print("-------------------------------------")
arquivo.write('-------------------------------------\n')

msg = u"Mediana e "+ str(util.calc_mediana(val_sorted))+'\n'
print(msg)
arquivo.write(msg)

arquivo.write('-------------------------------------\n')
print("-------------------------------------")

print("Moda:")
arquivo.write("Moda:\n")
list = util.list_moda(val_sorted) 
msg = ""
for x in list:
    msg = str(x.valor) + " - " + str(x.qtd) +'\n'
    print(msg)
    arquivo.write(msg)

print("-------------------------------------")
arquivo.write('-------------------------------------\n')

msg = u"Medidas de variabilidade sao " + str(util.calc_medidas_variabilidade(val_sorted)) +'\n'
print(msg) 
arquivo.write(msg)

arquivo.close()