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

# Lidando com a questão 1
maior_numero_filmes = 0
ator_maior_numero = ''

# Lidando com a questão 2
total_gross = 0
count = 0

with open('actors.csv', 'r') as arquivo:

    cabecalho = arquivo.readline().split(',') # Divide o cabeçalho em colunas
    cabecalho_nome = {}   
    
     #Eu fiz um esquema pra em vez de pegar pelo indice a coluna eu ter pelo nome elas, assim trabalhar melhor
    for indice, coluna in enumerate(cabecalho):
        cabecalho_nome[coluna.strip()] = indice

    actor = cabecalho_nome.get('Actor') # Obtém o índice da coluna 'Actor'
    number_of_movies = cabecalho_nome.get('Number of Movies') # Obtém o índice da coluna 'Number of Movies'
    gross = cabecalho_nome.get('Gross') # Obtém o índice da coluna 'Gross'
    
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
        total_gross += valor_gross
        count += 1
        media_gross = format(total_gross / count, '2f').rstrip('0') # Formatei o valor para que só ficasse 2 casas decimais
        


    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-1
    with open('etapa-1.txt', 'w') as arquivo:
        print(ator_maior_numero, file=arquivo)

    # Joga a resposta obtida para o arquivo txt, essa é a resposta da etapa-2
    with open('etapa-2.txt', 'w') as arquivo:
        print(media_gross, file=arquivo)


print(f"A média de receita de bilheteria bruta dos principais filmes é: {media_gross}")
print(f"O ator/atriza com o maior número de filmes é: {ator_maior_numero}")

