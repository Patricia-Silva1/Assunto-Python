# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Listas)
# Atividade 2: Lista com 10 valores
#              exibe só os ímpares
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

listaNumeros = []
for i in range(10):
    numero = int(input(f'Informe o {i+1}° número: '))
    listaNumeros.append(numero)
print('Lista completa:',listaNumeros)

print('Apenas os ímpares: [',end="")
for i in listaNumeros:    
    if ((i%2) != 0):
        print(f'{i} ',end="")
print(']')

print('\n----- FIM DA EXECUÇÃO: -----\n')