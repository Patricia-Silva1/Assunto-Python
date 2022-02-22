# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm1: Velocidade Média
# ----------------------------------

# definindo a função
def calc_velocidade_media(distancia,tempo):
    return distancia/tempo

# programa executando a função
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

d = float(input('Informe a distância percorrida em quilômetros:'))
t = int(input('informe o tempo percorrido em horas:'))
# chamando a função
r = calc_velocidade_media(d,t)
print('\nA velocidade média foi de {:.2f}'.format(r))

print('\n----- FIM DA EXECUÇÃO: -----\n')