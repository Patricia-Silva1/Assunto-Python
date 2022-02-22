#
# Verifica quantidade de respiradores do hospital
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
print ('HOSPITAL 1')
resp1 = float(input('Informe a quantidade de respiradores: '))
ocup1 = float(input('Informe a porcentagem de ocupação: '))
print ('HOSPITAL 2')
resp2 = float(input('Informe a quantidade de respiradores: '))
ocup2 = float(input('Informe a porcentagem de ocupação: '))
print ('HOSPITAL 3')
resp3 = float(input('Informe a quantidade de respiradores: '))
ocup3 = float(input('Informe a porcentagem de ocupação: '))
print ('HOSPITAL 4')
resp4 = float(input('Informe a quantidade de respiradores: '))
ocup4 = float(input('Informe a porcentagem de ocupação: '))
print ('HOSPITAL 5')
resp5 = float(input('Informe a quantidade de respiradores: '))
ocup5 = float(input('Informe a porcentagem de ocupação: '))
# ----- avaliando o valor informado
if ((resp1 < 50) and (ocup1 > 60)):
    resp1 = resp1 +5
if ((resp2 < 50) and (ocup2 > 60)):
    resp2 = resp2 +5
if ((resp3 < 50) and (ocup3 > 60)):
    resp3 = resp3 +5
if ((resp4 < 50) and (ocup4 > 60)):
    resp4 = resp4 +5
if ((resp5 < 50) and (ocup5 > 60)):
    resp5 = resp5 +5
print ('RESPOSTA:')
print ('     Hospital 1 -> respiradores:', resp1,'ocupação:',ocup1 )
print ('     Hospital 2 -> respiradores:', resp2,'ocupação:',ocup2 )
print ('     Hospital 3 -> respiradores:', resp3,'ocupação:',ocup3 )
print ('     Hospital 4 -> respiradores:', resp4,'ocupação:',ocup4 )
print ('     Hospital 5 -> respiradores:', resp5,'ocupação:',ocup5 )
print ('----- FIM DA EXECUÇÃO -----')