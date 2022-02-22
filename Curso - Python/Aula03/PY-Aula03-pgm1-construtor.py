# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 03 (Classes)
# Demosntrando contrutores
# ----------------------------------

print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

from Empresa import Funcionario

fu1 = Funcionario('Pedro','estoque','estoquista')
fu2 = Funcionario('Maria','estoque')
fu3 = Funcionario('Paulo')

print(fu1.nome, fu1.setor, fu1.cargo)
print(fu2.nome, fu2.setor, fu2.cargo)
print(fu3.nome, fu3.setor, fu3.cargo)

print('\n----- FIM DA EXECUÇÃO: -----\n')