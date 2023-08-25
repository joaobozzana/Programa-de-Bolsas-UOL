'''
Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. 
Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.

Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.
'''
# Tem varios comentario nesse codigo pq fui fazendo pra ir entendendo a ideia pq estava tendo dificuldades em elaborar.

def my_map(lista, f): #lista é a entrada; f é a potencia de 2
    resultado = [] #crio vazia para receber os novos valores
    for elemento in lista: # percorro tudo
        resultado.append(f(elemento))#aplico a função f nos elementos
    return resultado

#faço a potencia aqui
def potencia_de_2(x):
    return x ** 2

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(entrada, potencia_de_2) #Chamo o my_map passando a entrada, mais a funcao de potencia
print(resultado)
