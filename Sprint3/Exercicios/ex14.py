'''
Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.
Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

'''
#*args recebe parametros não nomeados; **kwargs recebe de parametros nomeados

def parametros(*args, **kwargs): #Passa os 2
    for arg in args: #nao nomeados
        print(arg)

    for value in kwargs.values():#nomeados
        print(value)

parametros(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)