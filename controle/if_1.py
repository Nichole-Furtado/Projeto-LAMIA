nota = float(input (' Informe a nota do aluno '))
comportado = True if input ('Comportado? (s/n): ') == 's'else False # Se o usuário digital y, aparece que o é comportado se não,
# não aparecerá no código.

#Se essa função for verdadeira executa o bloco, se não não executa
if nota >= 9:
    print('Duas palavras: para bens! :)')
    print ('Quadro de Honra')
#bloco tem apertar TAB
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print ('Recuperação')
elif nota >= 3.5:
    print('Recuperação + Trabalho')
else:
    print('Reprovado')
    
print (nota)
#Ele entra em desses blocos, elif intermediários