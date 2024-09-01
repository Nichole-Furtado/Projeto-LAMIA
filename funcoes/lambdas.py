from functools import reduce

alunos = [ # lista dicionário
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]
# Critério do aluno aprovado, lambda é uma função anônima, vai definir uma função em única linha, função anônima para atribuir uma 
#função sem nome para varíavel onde vc consiga chamar a função depois.
aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b
# filter vai passar por todos os alunos, vai pegar essa função e vai chamar todos os alunos
# vai transformar o dicionário em valor 
alunos_aprovados = list(filter(aluno_aprovado, alunos))
#Vai passar somente as notas dos alunos aprovados.
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
# soma tudo 
total = reduce(somar, notas_alunos_aprovados,0)
# lista de alunos aprovados n foi mudada
# média
print(total / len(alunos_aprovados))
# print(notas_alunos_aprovados)
# print (obter_nota(alunos[2]))# vai mostrar a nota do aluno indíce 2
# print(alunos)
# print(list(alunos_aprovados))