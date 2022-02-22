# ----------------------------------
# Este arquivo conté todas as classes
# de uma empresa
# ----------------------------------
# ----------------------------------
# Classe funcionario
# ----------------------------------
class Funcionario:
    def __init__(self, nm, se='a definir', cg='a definir',sl=1000):
        self.nome = nm
        self.setor = se
        self.cargo = cg
        self.salario = sl
