#
# contador de vogais
# 
print ('----- INÍCIO DA EXECUÇÃO -----')

texto = input ('Entre com o texto que será avaliado:')

# primeira solução
qtd = 0
for letra in texto:
    if (letra != 'a') and (letra != 'e') and (letra != 'i') and (letra != 'o') and (letra != 'u'):
        continue
    qtd += 1
print ('Total de vogais no texto:',qtd)

input ('Tecle enter para continuar...\n')

# segunda solução
qtd = 0
vogais = 'aeiou'
for letra in texto:
    if (vogais.count(letra) == 0):
        continue
    qtd += 1
print ('Total de vogais no texto:',qtd)

input ('Tecle enter para continuar...\n')

# terceira solução
qtd = texto.count('a')
qtd = qtd + texto.count('e')
qtd = qtd + texto.count('i')
qtd = qtd + texto.count('o')
qtd = qtd + texto.count('u')

print ('Total de vogais no texto:',qtd)

print ('----- FIM DA EXECUÇÃO -----')