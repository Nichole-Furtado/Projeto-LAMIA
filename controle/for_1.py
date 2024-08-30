#!python3

for i in range (10):
   print(i, end=' ')

print ('')

#1 até 10
for i in range (1, 11):
   print(i, end=' ')

print ('')

# Pula de 7 em 7
#Início, fim, e o passo    
for i in range (1, 100, 7):
    print(i, end=' ')

print ('')

#Descrecente 
for i in range (20, 0, -3):
    
    print(i, end=' ')

print ('')

nums = (2, 4, 6, 8)

for n in nums:
    print(n, end=' ') # end vai trazer a lista

print ('')

texto = 'Python é muito massa!'

for letra in texto:
    print(letra, end =' ')# end imprimi de outra forma, ele deixa na mesma linha
    
for n in {1, 2, 3, 4, 4, 4}:
    print(n, end= ' ')# Não aceita repetição
    
produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produto: # atrib é a chave
    print(atrib, ' ==>', produto[atrib], end= ' ')# chave de valor  
    
for atrib, valor in produto.items ():
    print (atrib, '==>', valor,  end= ' ')
    
for valor in produto.values ():
    print (valor, end= ' ') # mostra o resto do cód
    
for atrib in produto.keys ():
    print (atrib, end= ' ') # vai comentar as chaves
    