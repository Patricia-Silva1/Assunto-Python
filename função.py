def funcSoma (parm1, parm2):
    soma = parm1 + parm2
    return soma

x = int(input('valor 1: '))
y = int(input('valor 2: '))

resultado = funcSoma(x,y)
print ('somando: ', resultado)