# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Listas)
# Atividade 1: Lista com 5 nomes
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

listaNomes = []
for i in range(5):
    nome = input(f'Informe o {i+1}° nome: ')
    listaNomes.append(nome)
print(listaNomes)

print('\n----- FIM DA EXECUÇÃO: -----\n')