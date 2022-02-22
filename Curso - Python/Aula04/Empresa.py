class Funcionario:
    def __init__(self, nm, sl, mt, fu):
        self.nome = nm
        self.salario = sl
        self.matricula = mt
        self.funcao = fu

    def getSalario(self):
        return self.salario
    
    def setSalario(self, novoSal):
        salMax = self.salario * 1.20
        if (novoSal > salMax) or (novoSal<=self.salario):
            return False
        else:
            self.salario = novoSal
            return True