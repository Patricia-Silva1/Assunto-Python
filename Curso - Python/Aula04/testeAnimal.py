from Animal import Animal

ani1 = Animal('rex','cão')
ani2 = Animal('jumbo','elefante')

print('--------(ANTES)---------')
print('Animal 1:',ani1.nome, ani1.tipo)
print('Animal 2:',ani2.nome, ani2.tipo)
print('------------------------')

ani1.tipo = 'GALO'
ani2.tipo = 'ARANHA'

print('--------(DEPOIS de usar métodos "@")--------')
print('Animal 1:',ani1.nome, ani1.tipo)
print('Animal 2:',ani2.nome, ani2.tipo)
print('------------------------')

ani1.setNome('TOTÓ')
ani2.setNome('PERNINHAS')

print('--------(DEPOIS de usar métodos avulsos)--------')
print('Animal 1:',ani1.getNome(), ani1.getTipo())
print('Animal 2:',ani2.getNome(), ani2.getTipo())
print('------------------------')
