#
# Exemplos simples de repetição contável (for)
# 
print ('----- INÍCIO DA EXECUÇÃO -----')

# Um dicionário
provasFinais = {'Marta':9,'Paulo':5,'Helena':7,'Roberto':10}

print ('Todas as provas:',provasFinais)
print ('chave [Marta]:',provasFinais['Marta'])
for aluno,nota in provasFinais.items():
    print ('A nota do(a) aluno(a)',aluno,'foi',nota)

input ('Tecle enter para continuar...\n')

# Outro dicionário
pessoas = {'Marcos':'astronauta','Ana':'médica','Eduardo':'professor','Beatriz':'médica'}
if 'Ana' in pessoas.keys():   # OBS: apenas o nome do dicionário também funciona
    print ('Existe "Ana" na coleção do dicionário')
else:
    print ('Não "Ana" na coleção do dicionário')

if 'professor' in pessoas.values():
    print ('Existe(m) professor(es) na coleção do dicionário')
else:
    print ('Não existe(m) professor(es) na coleção do dicionário')

input ('Tecle enter para continuar...\n')

print ('----- FIM DA EXECUÇÃO -----')