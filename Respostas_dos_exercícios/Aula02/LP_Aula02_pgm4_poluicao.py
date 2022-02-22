#
# Testa índice de pouição
# 
print ('----- INÍCIO DA EXECUÇÃO -----')
# ----- entrada de dados
indice = float(input('Informe o índice de poluição: '))
# ----- avaliando o valor informado
print ('RESPOSTA:')
if (indice >= 0.5):
    print ('     Índice de polição > 0,5. Fechar Grupos 1, 2 e 3.')
else:
    if (indice >= 0.4):
        print ('     Índice de polição > 0,4. Fechar Grupos 1 e 2.')
    else:
        if (indice >= 0.3):
            print ('     Índice de polição > 0,3. Fechar Grupo 1.')
        else:
            if ((indice >= 0.05) and (indice <= 0.25)):
                print ('     Índice de poluição aceitavel.')
            else:
                print ('     Índice de poluição não está em nenhuma das faixas previstas!')
print ('----- FIM DA EXECUÇÃO -----')