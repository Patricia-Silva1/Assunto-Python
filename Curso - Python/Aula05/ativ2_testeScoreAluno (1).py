from Ativ2_Escola import Nota
from Ativ2_Escola import Aluno

aluno1 = Aluno('Maria',1,123,[])
aluno2 = Aluno('Paulo',2,456,[])

nota1a = Nota('Prova 1','Matemática', 8)
nota1b = Nota('Prova 1','Geografia', 6)
nota1c = Nota('Prova 2','Matemática', 7)

nota2a = Nota('Prova 1','História', 3)
nota2b = Nota('Prova 2','História', 7)
nota2c = Nota('Prova 3','História', 10)

aluno1.notas = [nota1a, nota1b, nota1c]
aluno2.notas = [nota2a, nota2b, nota2c]

print('--------(Score de Alunos)---------')
print('Aluno 1:', aluno1.nome, ' ', aluno1.score())
print('Aluno 2:', aluno2.nome, ' ', aluno2.score())
print('-------------------------------------')
