leve = 0
grave = 0
assintomatico = 0
 
for i in range(10):
    tipopaciente = input('informe tipo do paciêntie L/A/G :'  )

if (tipopaciente == 'L'):
    leve += 1
elif (tipopaciente == 'G'):
    grave += 1
elif (tipopaciente == 'A'):
    assintomatico +=1
    
print ("Total de paciente avaliados: 10 ")
print ("Percentual de pacientes com sintomas leves " , (leve *100/10))
print ("Percentual de pacientes assintomaticos ", (assintomatico *100/10))
print ("Percentual de pacientes com sintomas graves ", ( grave *100/10))
