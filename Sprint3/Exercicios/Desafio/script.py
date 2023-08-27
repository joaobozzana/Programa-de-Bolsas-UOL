# Função para tratar problemas com " "
def tratamento(line):
    campos = []
    campo = ''
    apas = False

    for char in line:
        if char == '"':
            apas = not apas
        elif char == ',' and not apas:
            campos.append(campo)
            campo = ''
        else:
            campo += char
    
    campos.append(campo.strip())
    return campos

# Variaveis para lidar com a questão 1
maior_numero_filmes = 0
ator_maior_numero = ''

# Variaveis para lidar com a questão 2
gross_total = 0
count = 0

# Variaveis para lidar com a questão 3
maior_receita_bilheteria = 0
ator_bilheteria = ''

# Variaveis para lidar com a questão 4
filmes_contagem = {}

# Variaveis para lidar com a questão 5
receita_total_bruta = {}

with open('actors.csv', 'r') as arquivo:

    cabecalho = arquivo.readline().split(',') # Divide o cabeçalho em colunas
    cabecalho_nome = {}   
    
    #Eu fiz um esquema pra em vez de pegar pelo indice a coluna eu ter pelo nome elas, assim trabalhar melhor
    for indice, coluna in enumerate(cabecalho):
        cabecalho_nome[coluna.strip()] = indice

    actor = cabecalho_nome.get('Actor') # Obtém o índice da coluna 'Actor'
    number_of_movies = cabecalho_nome.get('Number of Movies') # Obtém o índice da coluna 'Number of Movies'
    gross = cabecalho_nome.get('Gross') # Obtém o índice da coluna 'Gross'
    average_per_movie = cabecalho_nome.get('Average per Movie') # Obtém o índice da coluna 'Average per Movie'
    movie = cabecalho_nome.get('#1 Movie') # Obtém o índice da coluna '#1 Movie'
    total_gross = cabecalho_nome.get('Total Gross') # Obtém o índice da coluna 'Total Gross'
    
    for linha in arquivo:
        campos = tratamento(linha) #  Chama a função para tratar o caso das " "
        
        # Lidando com a questão 1
        nome_ator = campos[actor]
        numero_filmes = int(campos[number_of_movies])

        if numero_filmes > maior_numero_filmes:
            maior_numero_filmes = numero_filmes
            ator_maior_numero = nome_ator

        # Lidando com a questão 2
        valor_gross = float(campos[gross])  
        gross_total += valor_gross
        count += 1
        media_gross = format(gross_total / count, '2f').rstrip('0') # Formatei o valor para que só ficasse 2 casas decimais
        
        # Lidando com a questão 3
        receita_bilheteria = float(campos[average_per_movie])
        
        if receita_bilheteria > maior_receita_bilheteria:
            maior_receita_bilheteria = receita_bilheteria
            ator_bilheteria = nome_ator
            
        # Lidando com a questão 4
        nome_filme = campos[movie]
        
        if nome_filme in filmes_contagem:
            filmes_contagem[nome_filme] += 1
        else:
            filmes_contagem[nome_filme] = 1

        # Aqui to criando tubla pra receber nome do filme, + um count pra saber quantas X ele passou
        # utilizando do conceito de list comprehension 
        filmes_contagem_list = [(filme, count) for filme, count in filmes_contagem.items()]
        
        filmes_contagem_list.sort(key=lambda x: (-x[1], x[0]))
        
        # Lidando com a questão 5
        receita = float(campos[total_gross])
        
        if nome_ator in receita_total_bruta:
            receita_total_bruta[nome_ator] += receita
        else:
            receita_total_bruta[nome_ator] = receita
        
        atores_ordenados = sorted(receita_total_bruta.items(), key=lambda x: x[1], reverse=True)
        
    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-1
    with open('etapa-1.txt', 'w') as arquivo:
        print(ator_maior_numero, file=arquivo)

    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-2
    with open('etapa-2.txt', 'w') as arquivo:
        print(media_gross, file=arquivo)
        
    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-3
    with open('etapa-3.txt', 'w') as arquivo:
        print(ator_bilheteria, file=arquivo)

    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-4
    with open('etapa-4.txt', 'w') as arquivo:
        for sequencia, (filme, count) in enumerate(filmes_contagem_list, start=1):
            print(f"{sequencia} - O filme {filme} aparece {count} vez(es) no dataset", file=arquivo)
          
    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-5  
    with open('etapa-5.txt', 'w') as arquivo:
        for ator, receita in atores_ordenados:
            print(f"{ator} - {receita:.2f}", file=arquivo)

# Impressões 

# Imprime a 1
print(f"O ator/atriz com o maior número de filmes é: {ator_maior_numero} com {maior_numero_filmes}")
print(' ')

# Imprime a 2
print(f"A média de receita de bilheteria bruta dos principais filmes é: {media_gross}") 
print(' ')

# Imprime a 3
print(f"Ator/atriz com a maior média de receita de bilheteria bruta por filmes é: {ator_bilheteria} com {maior_receita_bilheteria}") 
print(' ')

# Imprime a 4
for sequencia, (filme, count) in enumerate(filmes_contagem_list, start=1):
    print(f"{sequencia} - O filme {filme} aparece {count} vez(es) no dataset") 
print(' ')

# Imprime a 5
for ator, receita in atores_ordenados:
    print(f"{ator} - {receita:.2f}") 