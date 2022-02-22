# ------------------------------------
# Este arquivo contém todas as classes
# referentes a animais
# ------------------------------------
# -------------------------------
# Classe Animal
# -------------------------------
class Animal:
    def __init__(self, nomeAni, tipoAni):
        self._nome = nomeAni
        self._tipo = tipoAni
    # getter de nome
    @property
    def nome(self):
        return self._nome
    # setter de nome
    @nome.setter
    def nome(self,nm):
        self._nome = nm
    # getter de tipo
    @property
    def tipo(self):
        return self._tipo
    # setter de tipo
    @tipo.setter
    def tipo(self,tp):
        self._tipo = tp
    # métodos avulsos
    def getNome(self): return self._nome
    def setNome(self,nm): self._nome = nm
    def getTipo(self): return self._tipo
    def setTipo(self,tp): self._tipo = tp   