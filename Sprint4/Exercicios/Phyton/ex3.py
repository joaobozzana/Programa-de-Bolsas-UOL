from functools import reduce

def calcula_saldo(lancamentos) -> float:
    # Utilizando o lambda, aqui na função ja faço o if pra ver se vai somar ou nao tendo como parametro o C
    cal_lancamentos = lambda saldo, lancamento: saldo + lancamento[0] if lancamento[1] == 'C' else saldo - lancamento[0]

    saldo = map(cal_lancamentos, [0] * len(lancamentos), lancamentos) # Utilizando o map 

    valor_final = reduce(lambda x, y: x + y, saldo) # Utilizando o reduce

    return valor_final

# Exemplo de entrada
lancamentos = [(200, 'D'), (300, 'C'), (100, 'C')]

saldo = calcula_saldo(lancamentos)
print(f"O valor final é: {saldo}")


'''
A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. 
Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função.
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]
A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. 
Na lista anterior, por exemplo, teríamos como resultado final 200.

Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:
reduce (módulo functools)
map
'''    