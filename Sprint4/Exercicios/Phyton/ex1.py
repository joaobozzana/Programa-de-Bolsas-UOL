with open('number.txt', 'r') as arquivo:
    numeros = list(map(int, arquivo.readlines())) # Utilizando o map

num_pares = list(filter(lambda numero: numero % 2 == 0, numeros)) # Utilizando o filter e lambda

num_pares_ordenados = sorted(num_pares, reverse=True) # Utilizando o sorted

maiores = num_pares_ordenados[:5]

soma = sum(maiores) # Utilizando o sum

print(maiores)
print(soma)

'''
Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, 
apresente os 5 maiores valores pares e a soma destes.

Você deverá aplicar as seguintes funções no exercício:
map
filter
sorted
sum

Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):
a lista dos 5 maiores números pares em ordem decrescente;
a soma destes valores.
'''