#
# Calcule o valor mensal da carga dos caminhões
# 
print ('----- INÍCIO DA EXECUÇÃO -----')

valTon = float(input('Informe o valor da tonelada:'))
total = 0
fim = 'nao'

while (fim != 'sim'):
    qtd = float(input('Qtd. de toneladas do caminhão? (0 para sair)'))
    if (qtd == 0):
        fim = 'sim'
    else:
        total = total + (qtd * valTon)

print ('Total mensal faturado:', total)

print ('----- FIM DA EXECUÇÃO -----')