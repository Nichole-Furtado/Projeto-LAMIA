#!#!python3
# termo
# PEP
# É uma proposta de melhoria do Python, codificação do python, te dando dicas e melhorias

def soma (*nums): #print (type(nums))
    total = 0 # cada número de nums vou somar com o total e retornar com o total
    for n in nums:
        total += n
    return total
# kwargs= Argumentos nomeados, um dicionário
def resultado_final(**kwargs):
    # print (type(kwargs)) só para mostrar tipo dicionário
    status = 'aprovado(a)' if kwargs ['nota'] >= 7 else 'reprovado (a)' 
    return f'{kwargs ["nome"]} foi {status}'
    # print (kwargs['nome'])
    # print (kwargs['nota'])