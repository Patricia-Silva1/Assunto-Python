# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 02 (Dicionário)
# Atividade 2: calcula médias de alunos
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

aluno = {}

def mediaNotas(nm):
    return sum(aluno[nm])/2

while (True):
    nome = input('Nome do aluno:')
    if (nome == ''):
        break;
    n1 = float(input ('Nota 1:'))
    n2 = float(input ('Nota 2:'))
    aluno[nome] = [n1,n2]

print('#####',aluno)

for a in aluno:
    print('A média do aluno {} é {}'.format(a,mediaNotas(a)))

print('\n----- FIM DA EXECUÇÃO: -----\n')