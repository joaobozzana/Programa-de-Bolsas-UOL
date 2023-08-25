'''
Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.

['abc', 'abc', 'abc', '123', 'abc', '123', '123']
'''

lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

conjunto = set(lista) #Converte em conjunto que automaticamente ja tira os repetidos
lista_sem_repeticao = list(conjunto) # Volta pra lista ja filtrado por conta do conjunto

print(lista_sem_repeticao)