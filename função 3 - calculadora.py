#aqui é onde a ação é definida, mas não executada#
def calculadora (n1, n2, op):
    if (op == "somar"):
        return n1+n2 
    elif (op == "subtrair"):
        return n1-n2
    elif (op == "multiplicar"):
        return n1*n2
    elif (op == "dividir"):
        return n1/n2
    else: 
        return 'Operação inválida'
#aqui são onde as variáveis são definidas#     
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
acao = input('Informe a ação da calculadora por extenso: ')
#e logo aqui é onde a execução acontece de fato#
print ('resultado da operação ',acao,'=',calculadora(a,b,acao))
