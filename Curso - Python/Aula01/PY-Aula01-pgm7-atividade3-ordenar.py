# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm7: Atividade 3
#       Função recebe 3 valores inteiros
#       e devolve valores ordenados
# ----------------------------------

# definindo a função
def ordenar(val1,val2,val3):
    # armazenando os valores recebidos em um array (lista)
    valores = [val1,val2,val3]
    # retornando lista ordenada 
    valores.sort()
    return valores
    #
    # IMPORTANTE: a função embutida "sort()" altera a ordem da lista original
    # armazenada na variável "valores". Para gerar uma lista ordenada sem 
    # alterar as posições da lista original, seria preciso usar a função 
    # "sorted()" e guardar seu resultado em outra variável. 
    # Exemplo: valoresOrdenados = valores.sorted()
    #
# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

v1 = int(input('Entre com o primeiro valor: '))
v2 = int(input('Entre com o segundo  valor: '))
v3 = int(input('Entre com o terceiro valor: '))

print('Valores ordenados :',ordenar(v1,v2,v3))

print('\n----- FIM DA EXECUÇÃO: -----\n')