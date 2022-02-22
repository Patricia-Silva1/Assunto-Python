#
# Dois exemplos simples de repetição (while)
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ------- exemplo 1 --------
numero = int(input('Informe um valor:'))

while (numero > 0):                     # repete o bloco de comandos enquanto o teste for verdadeiro
    print(numero)                       # exibe o valor de num
    numero -= 1                         # subtrai 1 do valor de num
# ------- exemplo 2 --------
nome = input ('Informe um nome:')
while (nome):                           # repete o bloco de comandos enquanto nome não for vazio
    print(nome)                         # exibe o valor de num
    nome = input ('Informe um nome:')    # entra com um novo nome

print ('----- FIM DA EXECUÇÃO -----')