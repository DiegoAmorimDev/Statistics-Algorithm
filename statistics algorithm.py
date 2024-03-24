import math

# exemplo 1 atividade estatistica
# desvio medio e media

tempo_resposta = 100, 150, 200, 250, 300
tempo_respostas_med = sum(tempo_resposta) / len(tempo_resposta)
print('a media é : ', tempo_respostas_med)
resul = sum(abs(x - tempo_respostas_med) for x in tempo_resposta) / len(tempo_resposta)
print('o desvio médio é:' , resul)

# variancia

resul2 = sum((x - tempo_respostas_med) ** 2 for x in tempo_resposta) / len(tempo_resposta) - 1
print('a variancia é', resul2)

# desvio padrao

resul3 = sum((x - tempo_respostas_med) ** 2 for x in tempo_resposta) / len(tempo_resposta) - 1 
resul3r = math.sqrt(resul3)
print('o desvio padrao é é', resul3r)

# exemplo 2 atividade estatistica
# desvio medio e media

tempo_resposta2 = 100, 120, 110, 130, 125, 115
tempo_respostas_med2 = sum(tempo_resposta) / len(tempo_resposta)
print('a segunda media é : ', tempo_respostas_med2)
result = sum(abs(x - tempo_respostas_med2) for x in tempo_resposta2) / len(tempo_resposta2)
print('o segundo desvio médio é:' , result)

# variancia

result2 = sum((x - tempo_respostas_med2) ** 2 for x in tempo_resposta2) / len(tempo_resposta2) - 1
print('a segunda variancia é', result2)

# desvio padrao

result3 = sum((x - tempo_respostas_med2) ** 2 for x in tempo_resposta2) / len(tempo_resposta2) - 1 
result3r = math.sqrt(result3)
print('o segundo desvio padrao é é', result3r)

# exemplo 3 atividade estatistica
# desvio medio e media

tempo_resposta3 = 50, 55, 60, 65, 70
tempo_respostas_med3 = sum(tempo_resposta3) / len(tempo_resposta3)
print('a terceira media é : ', tempo_respostas_med3)
resultd = sum(abs(x - tempo_respostas_med3) for x in tempo_resposta3) / len(tempo_resposta3)
print('o terceiro desvio médio é:' , resultd)

# variancia

result3 = sum((x - tempo_respostas_med3) ** 2 for x in tempo_resposta3) / len(tempo_resposta3) - 1
print('a terceira variancia é', result3)

# desvio padrao

result3e = sum((x - tempo_respostas_med3) ** 2 for x in tempo_resposta3) / len(tempo_resposta3) - 1 
result3ra = math.sqrt(result3e)
print('o terceiro desvio padrao é é', result3ra)

# exemplo 4 atividade estatistica
# desvio medio e media

tempo_resposta4 = 100, 150, 200, 250, 300, 350, 400, 450, 500
tempo_respostas_med4 = sum(tempo_resposta4) / len(tempo_resposta4)
print('a quarta media é : ', tempo_respostas_med4)
resultdo = sum(abs(x - tempo_respostas_med4) for x in tempo_resposta4) / len(tempo_resposta4)
print('o quarto desvio médio é:' , resultdo)

# variancia

result3f = sum((x - tempo_respostas_med4) ** 2 for x in tempo_resposta4) / len(tempo_resposta4) - 1
print('a quarta variancia é', result3f)

# desvio padrao

result3g = sum((x - tempo_respostas_med4) ** 2 for x in tempo_resposta4) / len(tempo_resposta4) - 1 
result3ras = math.sqrt(result3g)
print('o quarto desvio padrao é é', result3ras)