def valor():
    valor1 = (input('Insira o primeiro valor: '))
    valor2 = (input('Insira o segundo valor: '))
    valor3 = (input('Insira o terceiro valor: '))
    
    return valor1,valor2,valor3

print('Iniciando programa...')
    
num_1,num_2,num_3 = valor()
ordem = valor()
while (num_1 < num_2 < num_3): 
    break
print('Fim.')

#dar uma olha na função "sort"#