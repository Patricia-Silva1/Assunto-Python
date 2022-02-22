#
# Adivinhando um número
# 
print ('----- INÍCIO DA EXECUÇÃO -----')

import random    # isso permite o sorteio de números randômicos

x = random.randrange(1,10)   # sorteando um número entre 1 e 10

numero = 0

while (numero != x):    
    numero = int(input('Informe um número:'))
    if (numero > x):
        print('Seu número (', numero,') é maior que o valor sorteado')
    elif (numero < x):
        print('Seu número (', numero,') é menor que o valor sorteado')
    else:
        print('parabéns! Você acertou.')
  
print ('----- FIM DA EXECUÇÃO -----')