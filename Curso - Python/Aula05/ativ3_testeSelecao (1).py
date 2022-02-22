from Ativ3_Selecao import Prova
from Ativ3_Selecao import Candidato
from Ativ3_Selecao import ProcessoSeletivo

prv1 = Prova('07/01/2022',6)
prv2 = Prova('07/01/2022',9)
prv3 = Prova('07/01/2022',8)
prv4 = Prova('07/01/2022',4)
prv5 = Prova('07/01/2022',8)
prv6 = Prova('07/01/2022',10)

cand1 = Candidato('João', 'Rua Abc, num. 12', 3, 'experiente', prv1)
cand2 = Candidato('Roberta', 'Av. da Praia, num. 114', 1, 'interessada', prv2)
cand3 = Candidato('Luiz', 'Rua das Casas, num. 2', 1, 'atento', prv3)
cand4 = Candidato('Márcia', 'Rua Alta, num. 432', 0, 'iniciante', prv4)
cand5 = Candidato('Jorge', 'Alameda Xisto, num. 73', 2, 'distraído', prv5)
cand6 = Candidato('Raul', 'Rua das Flores, num. 88', 4, 'inseguro', prv6)

candidatos_do_processo = [cand1, cand2, cand3, cand4, cand5, cand6]
processo = ProcessoSeletivo(candidatos_do_processo)

print('--------(Processo Seletivo)---------')
print('Lista de aprovados:')
print(processo.listaAprovados())
print('-------------------------------------')
