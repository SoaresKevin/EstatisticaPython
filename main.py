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
stage = "dev"
media = 0

if stage == "Production":
    linhas_num = int(input("Quantas linhas de dados deseja trabalhar?"))

    for x in range(0,linhas_num): 
        itens = input("Digite os itens que deseja trabalhar separados por (/):")
        valores += itens.split('/')
else:
    itens = "400/300/330/300/330/330/430/400/380/550/350/450/280/350/450/530/500/350/420/400/350/550/450/330/380/500/480/450/450/280/450/250/250/300/280/430/420/300/520/350/380/400/450/400/480/520/450/400/450/450/300/330/380/420/420/430/480/500/480/430"
    valores = itens.split('/')

valores = map(float, valores)
val_sorted = sorted(valores)

print_valores = []
i = 0
msg = ""
for x in val_sorted:
    msg += str(x)+"/" 
    i += 1
    if i == 10:
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

msg = u"Variancia " + str(util.calc_variancia(val_sorted)) +'\n'
print(msg) 
arquivo.write(msg)

print("-------------------------------------")
arquivo.write('-------------------------------------\n')


msg = u"Desvio Padrao " + str(util.calc_devio_padrao(val_sorted)) +'\n'
print(msg) 
arquivo.write(msg)

print("-------------------------------------")
arquivo.write('-------------------------------------\n')


msg = u"Coeficiente de Variacao " + str(util.calc_coeficiente_variacao(val_sorted)) +'% \n'
print(msg) 
arquivo.write(msg)



arquivo.close()