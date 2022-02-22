# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Listas)
# Testes
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

aluno = {'Ana':[3,5,8],'Pedro':[7,5,5],'Joao':[6,9,8],'Edu':[7,6,10]}

for a in aluno:
    media = sum(aluno[a])/len(aluno)
    print('{} teve media {}'.format(a,media))

print('\n----- FIM DA EXECUÇÃO: -----\n')