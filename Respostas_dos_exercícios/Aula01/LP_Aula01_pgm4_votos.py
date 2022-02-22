#
# Calcular percentuais de votação
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
totalVotos = float(input('Informe o número total de votos: '))
qtdBrancos = float(input('Informe o número votos em branco: '))
qtdNulos = float(input('Informe o número votos nulos: '))
qtdValidos = float(input('Informe o número votos válidos: '))
# ----- calculanso a área
percBra = (qtdBrancos * 100) / totalVotos
percNul = (qtdNulos * 100) / totalVotos
percVal = (qtdValidos * 100) / totalVotos
# ----- exibindo resultado
print ('RESPOSTA:')
print ('     Total de Votos:', totalVotos)
print ('     Votos em branco:', qtdBrancos, 'votos (', percBra, '% do total)')
print ('     Votos em branco:', qtdNulos, 'votos (', percNul, '% do total)')
print ('     Votos em branco:', qtdValidos, 'votos (', percVal, '% do total)')
print ('----- FIM DA EXECUÇÃO -----')