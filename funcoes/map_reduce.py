#A função reduce faz parte do módulo functools e é 
# usada para aplicar uma função cumulativa a todos os itens de uma lista, ou qualquer iterável, de modo que se reduz a um único valor.
from functools import reduce

# Aquilo q somar com a nota
def somar_nota(delta):
    def somar (nota):
    #def calc (nota):
        return nota + delta
    return somar
        #return nota + 1,5
    # return calc
# lista
notas = [6.4, 7.2, 5.4, 8.4]
notas_finais_1 = map(somar_nota(1.5), notas)
notas_finais_2 = map(somar_nota(1.6), notas)
print(notas_finais_1)
print(notas_finais_2)

total = 0
for n in notas:
    total += n

 
def soma(a, b):
    return a + b

total = reduce(soma, notas, 0)
print (total)
#Trabalho ganhe 1.5 na nota final
# ou os 4 alunos entregam no prazo no mesmo dia
# ou se algum aluno nao entregar tal dia, ninguem ganha nota

# for i, nota in enumerate (notas):
#     #  demonstra o indice e a nota
#     # print(i, nota)
#     notas [i] = nota + 1.5
 
# Len = Retrona o numero de elementos em um iterável, como uma lista.
# outra forma de realizar    
# for i in range (len(notas)):
#      notas [i] = notas [i] + 1.5
# # Vai adicionar automaticamente para todas as notas
# print (notas)

# map = vai pegar uma lista que vai converter para uma outra lista, so que vai ter uma mapeamento de uma informação para outra

