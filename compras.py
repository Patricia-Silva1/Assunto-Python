print('Produto 1')
produ1 = float(input('Qual o valor desse produto? '))
print('Produto 2')
produ2 = float(input('Qual o valor desse produto? '))
print('Produto 3')
produ3 = float(input('Qual o valor desse produto? '))
if(produ1 <= produ2) and (produ1 <= produ3):
    print('Preço 1 é o mais barato.')
elif(produ2 <= produ3) and (produ3 <= produ1):
    print('Preço 2 é o mais barato.')
elif(produ3 <= produ2):
    print('Produto 3 é o mais barato.')
else:('O produto é o mais barato.')    
           
        