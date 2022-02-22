#
# Libera ou proibe a entrada de acordo com a temperatura da pessoa
# OBS: Esta é a solução mais simples para o problema da atividade 2
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
temp = float(input('Informe temperatura: '))
# ----- avaliando o valor informado
abrir = False
if (temp <= 37):
    abrir = True
print ('RESPOSTA:', abrir)
print ('----- FIM DA EXECUÇÃO -----')