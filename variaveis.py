
a = 3
b = 4.4

print(a +b)

texto = 'Sua idade é ...'
idade = 23
#print (texto + str(idade))
print(f'{texto}{idade}')
#variaveis
#f' interpola valores, ler algo que está fora do texto e interpreta como se tivesse dentro do texto
# string pode converter para valor inteiro
# pode utilzar essa para comentário e ese """ e fechar no final"""
saudacao = 'bom dia '
print(3*saudacao )

PI = 3.14
# Constante não tem no python
# Convenção por isso maiuscula que vai definir constante
raio = float(input(" Informa o raio da circuferência: \n"))
# area = PI * raio * raio
# pode usar dessa forma tbm
area = PI * pow( raio, 2) 
print(f'A area é:{area} m2. ')
#se deixar o raio sem tipo ele fica string <class 'str'> por isso colocou float acima