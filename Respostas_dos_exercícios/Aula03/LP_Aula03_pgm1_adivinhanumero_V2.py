#
# Adivinhando um número
# 
print ('----- INÍCIO DA EXECUÇÃO -----')

import random    # isso permite o sorteio de números randômicos

x = random.randrange(1,10)   # sorteando um número entre 1 e 10

continua = True

while (continua):    
    numero = int(input('Informe um número:'))
    if (numero > x):
        print('Seu número é maior que o valor sorteado')
    elif (numero < x):
        print('Seu número é menor que o valor sorteado')
    else:
        continua = False
        print('parabéns! Você acertou.')
  
print ('----- FIM DA EXECUÇÃO -----')