#
# Calcular custo final de veículo
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados (custo de fábricação do carro)
custoFab = float(input('Informe o custo de fabricação do veículo: '))
# ----- processamento dos cálculos
percDist = custoFab * 0.28     # calculando percentual do distribuidor (28%)
imposto = custoFab * 0.45      # calculando impostos (45%)
custoFinal = custoFab + percDist + imposto   #calculando custo final ao consumidor
# ----- exibindo resultado
print ('RESPOSTA:')
print ('     Custo final do veículo:', custoFinal)
print ('----- FIM DA EXECUÇÃO -----')
