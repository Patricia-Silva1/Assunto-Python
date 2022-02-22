#
# Calculando média de notas de um aluno
# OBS:  média = (soma_de_valores / quantidade_de_valores)
#
print ('----- INÍCIO DA EXECUÇÃO -----')

qtdNotas = int(input('Quantas notas o aluno possui? '))
somaNotas = 0

for i in range(qtdNotas):
    nota = float(input('Informe nota do aluno: '))
    somaNotas += nota

print ('Média de notas do aluno:', somaNotas/qtdNotas)

print ('----- FIM DA EXECUÇÃO -----')