'''
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. 
Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

Utilize os valores abaixo para testar seu exercício:
x = 4 
y = 5
imprima:

Somando: 4+5 = 9
Subtraindo: 4-5 = -1
'''

class Calculo:
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
x = 4 
y = 5

operacao = Calculo()

print(f'Somando: {x} + {y} = {operacao.soma(x, y)}')
print(f'Subtraindo: {x} - {y} = {operacao.subtracao(x, y)}')