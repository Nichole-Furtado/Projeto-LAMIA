numeros = [1,2,3]
print (type(numeros))
# demonstra o tipo de varíavel, tipo list 

#numeração das listas 
# A lista aceita repetição, da para ver o tamanho da lista; Indice começa apartir de 0, no caso a variavel numeros, vai até 5
numeros.append (3)
numeros.append (4)
numeros.append (500)
print (len(numeros))

print(2 in numeros)

#aqui, qual for o número que vc colocar, embaixo colocar o valor, ele irá representar conforme a ordem, ex: 3
numeros[3] = 100
#Da para fazer dessa forma, onde vc colocar a ordem, a quantidade 
numeros.insert(0,-200)
#Dessa forma abaixo, vc faz ao contrátrio, coloca a ordem embaixo e aquantidade la em cima, que é as listas
print(numeros[6])
# -1 significa que vc está indo de trás para frente , o ultimo
print(numeros[-1])
print(numeros[-2])
print(numeros)