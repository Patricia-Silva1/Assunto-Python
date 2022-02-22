from Empresa import Funcionario
func = Funcionario('Xavier', 30000.00, 666, 'professor')
print ('Funcionario antes:',func.nome, func.salario)
result = func.setSalario(32000.00)
if (result):
    print ('Valor do salário alterado com sucesso')
else:
    print ('Valor do salário não foi alterado')
print ('Funcionario depois:',func.nome, func.salario)
