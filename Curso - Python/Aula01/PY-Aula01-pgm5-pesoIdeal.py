# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm5: Calculando o peso ideal
# ----------------------------------

# definindo a função
def calc_peso_ideal(alt,sexo='f'):
    if (sexo.lower() == 'f'):
        return (62.1 * alt) - 44.7
    else:
        return (72.7 * alt) - 58

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')
# entrando com os dados
al = float(input('Informe altura: '))
sx = input('Informe sexo: ')
# chamando a função
print('Seu peso ideal é {:.2f}'.format(calc_peso_ideal(al,sx)))

print('\n----- FIM DA EXECUÇÃO: -----\n')