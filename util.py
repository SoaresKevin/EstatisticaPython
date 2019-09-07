from decimal import Decimal
from math import ceil, floor
from Moda import Moda
import statistics   

def calc_mediana(valores):
    posicao = (len(valores) +1)/2 
    print("Posicao:",posicao)
    print("Tamanho:",len(valores))
    if Decimal(posicao) % 1 == 0:
        return valores[int(posicao)]
    else:
        posi_maior = ceil(posicao)
        posi_menor = floor(posicao)
        print(posi_maior)
        print(posi_menor)
        print(valores[posi_maior-1])
        print(valores[posi_menor-1])
        return (( valores[posi_maior-1] + valores[posi_menor-1])/2)

def list_moda(val_sorted):
    list = []
    for x in set(val_sorted): 
        list.append(Moda(x,val_sorted.count(x)))
    list.sort(key=lambda x: x.qtd, reverse=True)
    return list
    

def calc_variancia(val_sorted):
    media = round(statistics.mean(val_sorted), 6) 
    total = 0
    print("--Variancia Totais--")
    for x in set(val_sorted): 
        total += round((val_sorted.count(x) * (( x - media )**2)),6)
        print(str(x),"-",str(val_sorted.count(x)),"-",(round((val_sorted.count(x) * (( x - media )**2)),6)))
    print("--Variancia Totais--")
    return round((total/len(val_sorted)),6)

def calc_coeficiente_variacao(val_sorted):
    desvio_padrao = calc_devio_padrao(val_sorted)
    media = round(statistics.mean(val_sorted),6)

    return round( ((desvio_padrao/media) * 100),6)
    

def calc_devio_padrao(val_sorted):
    media = round(statistics.mean(val_sorted), 6) 
    total = 0
    for x in set(val_sorted): 
        total += round((val_sorted.count(x) * (( x - media )**2)),6)
    resultado = round((total/len(val_sorted)),6)
    raizQ = resultado ** (1/2)
    return raizQ

