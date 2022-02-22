# ----------------------------------
# Infinity - Dev Full Stack
# Módulo: Python / Aula 01 (Funções)
# Pgm6: Função retornando mais de um valor
# ----------------------------------

# definindo a função
def cadastro():
    nome = input('Qual o seu nome: ')
    age = int(input('Idade: '))
    return nome, age

# --- programa executando a função ---
print ('\n----- INÍCIO DA EXECUÇÃO -----\n')

print('Iniciando o cadastro...')
nom,ida = cadastro()

print('Cadastro realizado com sucesso:')
print('Seu nome é {} e você tem {} anos de idade.'.format(nom,ida))

print('\n----- FIM DA EXECUÇÃO: -----\n')