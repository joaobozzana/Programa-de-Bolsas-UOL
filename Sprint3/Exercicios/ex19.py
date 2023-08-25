'''
Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:
Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!

import random 
# amostra aleatoriamente 50 números do intervalo 0...500
random_list = random.sample(range(500),50)

Use as variáveis abaixo para representar cada operação matemática:
mediana
media
valor_minimo 
valor_maximo 

Importante: Esperamos que você utilize as funções abaixo em seu código:
random
max
min
sum
'''

import random

def achar_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 1:
        indice_mediana = tamanho // 2
        mediana = lista_ordenada[indice_mediana]
    else:
        indice_superior = tamanho // 2
        indice_inferior = indice_superior - 1
        mediana = (lista_ordenada[indice_inferior] + lista_ordenada[indice_superior]) / 2

    return mediana

random_list = random.sample(range(500), 50)

mediana = achar_mediana(random_list)
media = sum(random_list) / len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
