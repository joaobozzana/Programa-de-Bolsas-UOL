'''
Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles.
Depois imprima a soma dos valores.
A string deve ter valor  "1,3,4,6,10,76"

'''

def soma(string_com_numeros):
    numeros = string_com_numeros.split(',') #O split faz a separação por ,
    numeros_inteiros = [int(numero) for numero in numeros] #Converto para inteiro pra conseguir fazer a soma
    soma = sum(numeros_inteiros)
    return soma

string_com_numeros = "1,3,4,6,10,76"

print(soma(string_com_numeros))