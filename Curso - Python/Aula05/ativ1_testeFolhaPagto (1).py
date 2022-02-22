from Ativ1_Empresa import Funcionario
from Ativ1_Empresa import FolhaPagto

func1 = Funcionario('Pedro', 3000.00, 111, 'Vendedor')
func2 = Funcionario('Maria', 5000.00, 222, 'Gerente')
func3 = Funcionario('Fernando', 2000.00, 333, 'Atendente')

funcs_empresa = [func1, func2, func3]

folha = FolhaPagto(funcs_empresa)

print('--------(Folha de Pagamento)---------')
print('Funcionario 1:', func1.nome, func1.salario)
print('Funcionario 2:', func2.nome, func2.salario)
print('Funcionario 3:', func3.nome, func3.salario)
print('-------------------------------------')
print('Total da Folha de Pagamento:',folha.exibeTotalFolha())
print('-------------------------------------')
