#
# Aposentadoria
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
codEmp = int(input('Informe o código do empregado: '))
anoNasc = int(input('Informe o ano de nascimento do empregado: '))
anoIngresso = int(input('Informe o ano de ingresso do empregado na empresa: '))
# OBS: As próximas duas linhas de código são para obter o ano atual de forma
#      dinâmica e não são obrigatoriamente parte da solução do problema proposto
#      na aula. Caso prefira, o aluno pode simplesmente definir uma variável 
#      que contenha o ano atual fixo (mas isso torna a solução menos elegante).
import datetime
anoAtual = datetime.datetime.now().year
# ----- agora vamos calcular se o empregado pode se aposentar
idade = (anoAtual - anoNasc)
tempServ = (anoAtual - anoIngresso)
print ('RESPOSTA:')
print ('     Idade do Empregado:', idade,'Tempo de serviço:', tempServ)
if (idade >= 65):                          # empregado tem 65 anos ou mais
    print ('     Requerer aposentadoria')
elif (tempServ >= 30):                     # empregado trabalhou 30 anos ou mais
    print ('     Requerer aposentadoria')
elif (idade >= 60) and (tempServ >= 25):   # empregado tem 60 anos ou mais e trabalhou 25 anos ou mais
    print ('     Requerer aposentadoria')
else:
    print ('     Não requerer')
print ('----- FIM DA EXECUÇÃO -----')