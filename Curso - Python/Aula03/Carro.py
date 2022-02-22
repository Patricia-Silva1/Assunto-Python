# ----------------------------------
# Este arquivo conté todas as classes
# de um carro
# # ----------------------------------
# ----------------------------------
# Classe Carro
# ----------------------------------
class Carro:
    def __init__(self, marca, modelo, ano, velocidade=120, ligado=False, automatico=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        if (velocidade > 120):
            self.velocidade = 120
        elif (velocidade < 0):
            self.velocidade = 0
        else:
            self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar(self,novaVeloc):
        if (self.ligado):
            if (novaVeloc > 120):
                self.velocidade = 120
            elif (novaVeloc < 0):
                self.velocidade = 0
            else:
                self.velocidade = novaVeloc

    def verificarMarcha(self):
        if ((self.velocidade >=0) and (self.velocidade<20)):
            return 1
        elif ((self.velocidade >=20) and (self.velocidade<30)):
            return 2
        elif ((self.velocidade >=30) and (self.velocidade<45)):
            return 3
        elif ((self.velocidade >=45) and (self.velocidade<=60)):
            return 4
        else:
            return 5