#
# Placar de jogo
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
time1 = input('Informe o nome do time1: ')
time2 = input('Informe o nome do time2: ')
gols1 = int(input('Quantos gols fez o '+time1+'? '))
gols2 = int(input('Quantos gols fez o '+time2+'? '))
# ----- avaliando o valor informado
print ('RESPOSTA:')
if (gols1 > gols2):
    print ('     Vencedor:', time1)
elif (gols1 < gols2):
    print ('     Vencedor:', time2)
else:
    print ('     EMPATE')
print ('----- FIM DA EXECUÇÃO -----')