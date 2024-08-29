#Aceita repetição 
nomes = ('Ana', 'Bia', 'Gui', 'Leo','Ana')
# True se fosse bia minúscula, false
print('Bia' in nomes)
#Acessar o primeiro elemento e o segundo
print(nomes[0])
print(nomes[1:3])
# -1 vai trazer o penultimo, de trás para frente, "Gui"
print(nomes[1:-1])
# trazer do 2 para frente
print(nomes[2:])
# do "leo" para trás vai aparecer os nomes "ana""bia""gui"
print(nomes[:-2])
# mesmo se tratando de um complemente, se trata de um tupla
# n necessariamente somente com os parênteses se torna uma tupla, mas sim a ","
#x = ('Bia',)
#print(type(x))
#LEN = para contar quantos elementos tem na lista
print(len(nomes))
print(type(nomes))
print(nomes)    