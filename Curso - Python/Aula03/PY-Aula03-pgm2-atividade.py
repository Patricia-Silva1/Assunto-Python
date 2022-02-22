# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 03 (Classes)
# Testando métodos
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

from Carro import Carro

c1 = Carro('Jeep','Renegade',2021,0)

print('Carro criado:\n',c1.marca,c1.modelo,c1.ano,c1.velocidade,c1.ligado,c1.automatico)

c1.acelerar(50)
print('Carro desligado:\n',c1.marca,c1.modelo,c1.ano,c1.velocidade,c1.ligado,c1.automatico)

c1.ligar()
c1.acelerar(50)
print('Carro ligado:\n',c1.marca,c1.modelo,c1.ano,c1.velocidade,c1.ligado,c1.automatico)

print('\n----- FIM DA EXECUÇÃO: -----\n')