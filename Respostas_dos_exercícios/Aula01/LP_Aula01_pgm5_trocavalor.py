#
# Trocar valor de duas variáveis
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados (neste exercício os valores são fixos)
varA = 10
varB = 20
print ('ANTES DA TROCA:')
print ('     A:', varA, 'B:', varB)
# ----- para trocar os valores das variáveis precisaremos de uma variável auxiliar
varAuxiliar = varA
varA = varB
varB = varAuxiliar
# ----- exibindo resultado
print ('DEPOIS DA TROCA:')
print ('     A:', varA, 'B:', varB)
print ('----- FIM DA EXECUÇÃO -----')
