#
# Calculando percentuais de covid-19
# OBS:  percentual = (valor*100)/quantidade_de_valores)
#
print ('----- INÍCIO DA EXECUÇÃO -----')

# p ... Pacientes com sintomas leves da doença;
# a ... Pacientes assintomáticos;
# g ... Pacientes com sintomas graves da doença.
qtdLeves = 0
qtdAssint = 0
qtdGraves = 0

for np in range(10):
    paciente = input('Informe o tipo do paciente (l/a/g):')
    if (paciente == 'l'):
        qtdLeves += 1
    elif (paciente == 'a'):
        qtdAssint += 1
    elif (paciente == 'g'):
        qtdGraves += 1
    else:
        print ('===> Este paciente não entrará na estatística')

print ('....................')
print ('Percentual de sintomas leves :', (qtdLeves*100)/10 , '%')
print ('Percentual de assintomáticos :', (qtdAssint*100)/10 , '%')
print ('Percentual de sintomas graves:', (qtdGraves*100)/10 , '%')

print ('----- FIM DA EXECUÇÃO -----')