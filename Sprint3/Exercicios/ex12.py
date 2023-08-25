'''
Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json

https://docs.python.org/3/library/json.html
'''

import json

with open("person.json", "r") as arquivo:
    conteudo = arquivo.read()

dados = json.loads(conteudo) #parsing
print(dados)
