pessoas = ['Gui'], ['Rebeca']
adjs = ['Sapeca', 'Inteligente']

#for dentro do outro
for p in pessoas:
    for a in adjs:
        print (f'{p} é {a}!')

#laço vazio        
for i in [1, 2, 3]:
    pass

for i in range (1, 11):
    if i % 2:
        continue
    print(i, end=' ')

#break = Sai do laço, do programa e vai para o fim, sai do bloco
for i in range (1, 11):
    if i == 5:
        break
    print(i)
    
print('FIM!')
        