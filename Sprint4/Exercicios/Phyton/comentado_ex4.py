def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    #Explicando a linha, foi mais pra eu entender a contrução dela
    #op[0] = pra pegar o 1 elemento da tubla, que seria o sinal
    #op[1][0] e op[1][1] a ideia seria tipo o 1 pra falar que é o 2 elemento da trupla que seria
    #dos operandos e o [0] e [1] depois é pra pegar o 1 e 2 numero dos operandos
     
    #Com isso o lambda vai pegar a operador e jogar la na função de cima para realizar as operações
    resultados = map(lambda op: operacoes[op[0]](op[1][0], op[1][1]), zip(operadores, operandos))

    #Ver todos os resultados (OBS: subtituir resultados por resultados_lista no valor_max)
    #resultados_lista = list(resultados)
    #for resultado in resultados_lista:
    #    print(resultado)
        
    valor_max = max(resultados)
    return valor_max

# Exemplo de entrada
operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

valor_max = calcular_valor_maximo(operadores, operandos)
print(f"O maior valor é: {valor_max}")
