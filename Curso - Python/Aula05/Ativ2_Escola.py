# ------------------------------------
# Este arquivo contém todas as classes
# referentes a uma escola
# ------------------------------------
# -------------------------------
# Classe Nota
# -------------------------------
class Nota:
    def __init__(self, nome, disciplina, valor):
        self.nome = nome
        self.disciplina = disciplina
        self.valor = valor
# -------------------------------
# Classe Aluno
# -------------------------------
class Aluno:
    def __init__(self, nome, semestre, matricula, notas):
        self.nome = nome
        self.semestre = semestre
        self.matricula = matricula
        self.notas = notas

    def score(self):
        totalPontos = 0
        for n in self.notas:
            totalPontos += n.valor
        return totalPontos