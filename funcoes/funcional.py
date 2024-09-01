def soma (a, b):
    return a + b 

def sub (a, b):
    return a - b 

#armazenar uma função dentro de uma varíavel

somar = soma

print (somar(3, 4))

def operacao_aritmetica(fn, op1, op2): #funcao fn
    return fn (op1, op2) # vai receber duas operações

resultado = operacao_aritmetica (soma, 13, 48)
print (resultado)

resultado = operacao_aritmetica (sub, 13, 48)
print (resultado)

def soma_parcial (a):
    # processamento pesado 1 - 10s
    # processamento pesado 2 - 10s
    # processamento pesado 3 - 40s
    def concluir_soma (b):
        return a + b #10s
    return concluir_soma
# valor total vai processa trÊs vezes o processamento pesado, mesmo  que vc tem o msm valor
#r1 = soma_total (1, 2 )=> 1mim10 s
#r2 =  soma_total (1, 3)=> 1mim10 s
#r3 =  soma_total (1, 4)=> 1mim10 s
# Em baixo, seria soma parcial, onde é mais rápido o processamento de operação
soma_1 = soma_parcial (1)# 1 m
r1 = soma_1 (2) # 10 s
r2 = soma_1 (3) # 10 s
r3 = soma_1 (4) # 10 s
# Executar só em uma linha
resultado_final = soma_parcial(10)(12)
#fn = soma_parcial(10)
#resultado_final = fn(12)
print (resultado_final, r1, r2, r3)