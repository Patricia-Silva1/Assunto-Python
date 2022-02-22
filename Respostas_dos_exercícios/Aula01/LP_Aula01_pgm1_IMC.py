#
# Calcular IMC (Índice de Massa Corporal)
#
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
# ----- calculando IMC
imc = peso/(altura**2)
# ----- exibindo resultado
print (imc)
print ('----- FIM DA EXECUÇÃO -----')