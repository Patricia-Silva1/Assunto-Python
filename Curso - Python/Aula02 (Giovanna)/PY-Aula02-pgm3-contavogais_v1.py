# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Dicionário)
# Atividade 1: dicionário contendo vogais de um texto
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

contaVogais = {'a':0,'e':0,'i':0,'o':0,'u':0}
texto = input('Texto para avaliar:')

for letra in texto:
    if (letra.lower() =='a'):
        contaVogais['a'] += 1
    elif (letra.lower() =='e'):
        contaVogais['e'] += 1
    elif (letra.lower() =='i'):
        contaVogais['i'] += 1
    elif (letra.lower() =='o'):
        contaVogais['o'] += 1
    elif (letra.lower() =='u'):
        contaVogais['u'] += 1

print(contaVogais)

print('\n----- FIM DA EXECUÇÃO: -----\n')