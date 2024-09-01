#sintase é def, uma palavra reservada da linguagem, o nome da função, 
# os parênteses para definir o parâmetros da função.
# Recebe Parâmetros de entradas e processamento da saída 
# Esse que criamos, não possui parâmetro, e não vai retornar a chamada
# toda vez q a função é vazia, incluir o pass 
def saudacao(nome = 'Pessoa', idade = '20'): #nomenclatura de funcao
    print(f'Bom dia!{nome}!\n Você nem aparece ter {idade} anos')# f string

# def saudacao(): #nomenclatura de funcao
#     print ('Boa tarde!')

# #vira um môdulo main
# print (__name__)

def soma_e_multi (a, b, x):
    #retorna o resultado dessa operação
 # multi prio para soma
    return a + b * x
 #lá no aritmeticos, tem precedência
 
 
if __name__ == '__main__':
    saudacao ('Nichole', idade = 30)
    