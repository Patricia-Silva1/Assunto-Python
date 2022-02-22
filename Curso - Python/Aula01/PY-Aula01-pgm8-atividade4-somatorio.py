# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm8: Atividade 4
#       Função recebe 1 valor inteiro e positivo
#       e devolve o somatório deste valor
# ----------------------------------

# definindo a função
def somatorio(valor):
    soma = 0
    # Utilizaremos um FOR com a função RANGE()
    # Lembre-se: a função range varia de 0 (zero) até o valor, 
    # mas para ao chegar neste valor (ele não entra no processamento
    # das instruções que estão dentro do loop), por isso, faremos 
    # um ajuste no valor (somando 1) 
    for num in range(valor):
        print ('somando',num+1,'...')
        soma += num+1
    return soma

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

v = int(input('Entre com o valor: '))

print('Somatório do valor :',somatorio(v))

print('\n----- FIM DA EXECUÇÃO: -----\n')