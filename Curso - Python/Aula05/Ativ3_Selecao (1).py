# ------------------------------------
# Este arquivo contém todas as classes
# referentes a um processo seletivo
# ------------------------------------
# -------------------------------
# Classe Prova
# -------------------------------
class Prova:
    def __init__(self, dt, nt):
        self.data = dt
        self.nota = nt
# -------------------------------
# Classe Candidato
# -------------------------------
class Candidato:
    def __init__(self, nome, endereco, anosExperiencia, descricao, prova):
        self.nome = nome
        self.endereco = endereco
        self.anosExp = anosExperiencia
        self.descricao = descricao
        self.prova = prova

# -------------------------------
# Classe ProcessoSeletivo
# -------------------------------
class ProcessoSeletivo:
    def __init__(self, candidatos):
        self.candidatos = candidatos

    def listaAprovados(self):
        aprovados = []
        for c in self.candidatos:
            if (c.prova.nota >= 8):
                aprovados.append(c.nome)
        return aprovados
