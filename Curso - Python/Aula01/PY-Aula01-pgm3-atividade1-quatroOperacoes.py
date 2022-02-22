# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm3: Resolução da Atividade 1
#       Execução das quatro operações
# ----------------------------------

# definindo a função
def quatroOp(num1,num2,operacao):
    if (operacao == '+'):
        return (num1 + num2)
    elif (operacao == '-'):
        return (num1 - num2)
    elif (operacao == '*'):
        return (num1 * num2)
    elif (operacao == '/'):
        return (num1 / num2)
    else:
        return 'Operacao inválida'

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')
# entrada de dados
x = float(input('Informe o primeiro número: '))
y = float(input('Informe o segundo número: '))
o = input('Informe a operação: ')
# chamando a função
print('\nResultado: ',quatroOp(x,y,o))

print('\n----- FIM DA EXECUÇÃO: -----\n')