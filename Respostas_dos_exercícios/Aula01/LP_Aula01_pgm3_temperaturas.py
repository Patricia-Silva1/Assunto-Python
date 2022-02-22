#
# Conversor de Temperatura (de Farenheit para Celcius)
#
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
tempF= float(input('Informe a temperatura (em Farenheit): '))
# ----- convertendo para Celcius
tempC = 5 * ((tempF - 32)/9)
# ----- exibindo resultado
print ('RESPOSTA:', tempF, 'Farenheit equivalem a', tempC, 'Celcius')
print ('----- FIM DA EXECUÇÃO -----')