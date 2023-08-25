'''
Escreva um código Python para verificar se três números digitados na entrada padrão são pares ou ímpares. 
Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).

Importante: Aplique a função range() em seu código.
'''
numeros = []

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        print(f"Par: {numero}")
    else:
        print(f"Ímpar: {numero}")

