#
# Determina se um número é positivo ou negativo
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
num = float(input('Informe o número que será avaliado: '))
# ----- avaliando o valor informado
print ('RESPOSTA:')

if (num > 0):
    print ('     O número', num, 'é POSITIVO')
if (num < 0):
    print ('     O número', num, 'é NEGATIVO')
if (num = 0):
    print ('     O número', num, 'é zero (NEUTRO)')
print ('----- FIM DA EXECUÇÃO -----')