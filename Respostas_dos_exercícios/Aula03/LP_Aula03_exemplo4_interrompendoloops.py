#
# Exemplos simples de repetição contável (for)
# 
print ('----- INÍCIO DA EXECUÇÃO -----')

for num in (1,2,3,4,5):
    if (num == 4):
        break
    print (num)

input ('Tecle enter para continuar...\n')

for num in (1,2,3,4,5):
    if (num == 2) or (num == 4):
        continue
    print (num)

print ('----- FIM DA EXECUÇÃO -----')