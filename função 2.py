#calculando a velocidade média#
#def = comando para abrir uma função; nomeie a função (parâmetros, variáveis): 
#   (identação) diga o que vc quer que a função faça
#   return = retorna o resultado da sua função 

def funcVeloc (distfin, distin, tempo):
    veloc = (distfin-distin)/tempo
    return veloc


#código escrito referenciando a função acima
ponto_b = float(input('Distancia final: '))
ponto_a = float(input('Distancia inicial: '))
tempo = int(input('Qual o tempo percorrido? '))
vel_media = funcVeloc(ponto_b, ponto_a, tempo)
print('A velocidade média é', vel_media)