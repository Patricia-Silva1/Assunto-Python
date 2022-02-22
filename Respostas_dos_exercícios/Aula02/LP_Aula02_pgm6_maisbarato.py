#
# Decide qual o produto mais barato
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
prod1 = float(input('Informe o preço do produto 1: '))
prod2 = float(input('Informe o preço do produto 2: '))
prod3 = float(input('Informe o preço do produto 3: '))
# ----- descobrir qual o produto mais barato
print ('RESPOSTA:')
if (prod1 <= prod2) and (prod1 <= prod3):     # Produto 1 é o mais barato
    print ('     Compre o Produto 1 (é o mais barato)')
elif (prod2 <= prod1) and (prod2 <= prod3):     # Produto 2 é o mais barato
    print ('     Compre o Produto 2 (é o mais barato)')
elif (prod3 <= prod1) and (prod3 <= prod2):     # Produto 3 é o mais barato
    print ('     Compre o Produto 3 (é o mais barato)')
print ('----- FIM DA EXECUÇÃO -----')