# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm10: Atividade 6 (desafio)
#       Função recebe 1 data e informa
#       há quantos dias atrás aconteceu a data
# ----------------------------------

# Primeiramente vamos importar uma bilioteca
# contendo funções que manipulam datas
from datetime import datetime

# definindo a função
def quantosDias(dataInformada):
    # convertendo a string informada em um formato de data válido para calcular
    dtInf = datetime.strptime(dataInformada,'%d/%m/%Y')
    # obtendo a data atual
    dtAtu = datetime.today()
    
    # calculando a diferença de dias entre datas
    diferenca = abs((dtAtu - dtInf).days)
    
    return diferenca

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

# solicitando a data ao usuário
dt = input('Entre com a data (DD/MM/AAAA): ')
#exibindo a diferença
print('Diferença (em dias) para a data atual:',quantosDias(dt))

print('\n----- FIM DA EXECUÇÃO: -----\n')