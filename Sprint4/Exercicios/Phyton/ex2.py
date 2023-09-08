def conta_vogais(texto: str) -> int:
    
    vogal = "aeiouAEIOU" # Aqui eu defini oque é vogal, como nao tem acentos eu nao tratei isso

    vogais = filter(lambda char: char in vogal, texto) # Utilizando o filter e o lambda

    quant_vogais = len(list(vogais)) # Utilizando o len 

    return quant_vogais

texto = "Vou so dar nota maxima pra esse aluno"
quantidade = conta_vogais(texto)
print(f"O texto possui {quantidade} vogais.")

'''
Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado
deverá ser a contagem de vogais presentes em seu conteúdo.

É obrigatório aplicar as seguintes funções:
len
filter
lambda

Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
'''