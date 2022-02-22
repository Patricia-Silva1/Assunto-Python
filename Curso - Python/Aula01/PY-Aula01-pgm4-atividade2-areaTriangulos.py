# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm4: Resolução da Atividade 2
#       Calculando área de diversos triângulos
# ----------------------------------

# definindo a função
def calcula_triangulo(base,altura):
    return (base * altura) / 2

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')
# como o enunciado da atividade estabelece que o programa
# deve calcular quantos triângulos o usuário desejar, é 
# preciso criar uma estrutura de repetição
while (True):
    print('\nCalculando a área do triângulo:')
    print('(informe 0 (zero) no valor da base para encerrar o programa)')
    b = float(input('   Informe tamanho da base: '))
    if (b == 0): 
        break
    a = float(input('   Informe a altura: '))
    # chamando a função
    print('   ===> Resultado: {:.2f}'.format(calcula_triangulo(b,a)))

print('\n----- FIM DA EXECUÇÃO: -----\n')