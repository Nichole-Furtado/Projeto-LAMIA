from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 8.7},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7},
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b
# Gera uma lista na notas dos alunos, pode colocar um teste e filtrando conforme requisito
alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
# apenas nota do aluno aprovados
notas_alunos_aprovados = [aluno ['nota'] for aluno in alunos_aprovados]
print (alunos_aprovados)
# aqui reduz conforme soma de todos os alunos
total = reduce(somar, notas_alunos_aprovados,0)
# Média dos alunos aprovados
print(total / len(alunos_aprovados))
# print(notas_alunos_aprovados)
# print (obter_nota(alunos[2]))
# print(alunos)
# print(list(alunos_aprovados))