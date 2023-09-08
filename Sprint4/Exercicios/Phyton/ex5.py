import csv
#função para calcular a media das 3 maiores notas
def calcular(notas):
    notas = sorted(notas, reverse=True)
    tres_maiores = notas[:3]
    media = round(sum(tres_maiores) / 3, 2)
    return tres_maiores, media

with open('estudantes.csv', encoding='utf-8') as arquivo:
    lista = csv.reader(arquivo)
    
    estudantes = [] #Crio vazia e ir adicionando os estudantes para no fim poder ordenar
    
    for linha in lista:
        nome_estudante = linha[0]
        notas = list(map(int, linha[1:6]))
        maiores_notas, media = calcular(notas)
        #adiciono os estudantes 
        estudante = {
            'nome': nome_estudante,
            'maiores_notas': maiores_notas,
            'media': media
        }
        #inclemento
        estudantes.append(estudante)
    #ordeno os estudandes 
    estudantes_ordenados = sorted(estudantes, key=lambda x: x['nome'])

    for estudante in estudantes_ordenados:
        print(f"Nome: {estudante['nome']} Notas: {estudante['maiores_notas']} Média: {estudante['media']}")


'''
Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. 
Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. 
É o arquivo estudantes.csv de seu exercício.

Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:
Nome do estudante
Três maiores notas, em ordem decrescente
Média das três maiores notas, com duas casas decimais de precisão
O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:

Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>

Exemplo:
Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67
Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33

Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:
round
map
sorted
'''