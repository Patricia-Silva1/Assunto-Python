# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm9: Atividade 5
#       Função recebe 1 valor inteiro e positivo
#       e devolve o fatorial deste valor
# ----------------------------------

# definindo a função
def fatorial(valor):
    # Utilizaremos um FOR com a função RANGE()
    # Lembre-se: o fatorial de um número inteiro é o
    # resultado da multiplicação de todos os inteiros 
    # maiores que zero e menores ou iguais a este número.
    # Exemplo: o fatorial de 5 é igual a
    # fatorial = 1 x 2 x 3 x 4 x 5
    fat = 1 
    for num in range(valor):
        fat *= (num+1)
        print ('multiplicando',num+1,'... fat=', fat)
    return fat

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

v = int(input('Entre com o valor: '))

print('Fatorial de',v,' :',fatorial(v))

print('\n----- FIM DA EXECUÇÃO: -----\n')