dias = int(input("Quantos dias você alugou o carro?: "))
kms = float(input("Quantos quilômetros você rodou com o carro:? "))
valorFinal = (dias * 60) + (kms * 0.15)
print('O valor final a pagar pelo alguel será de: {:.2f}'.format(valorFinal) ) 

grausC = float(input("Quantos graus C está?: "))
grausF = grausC * 1.8 + 32
print(" A temperatura convertida de C para F é de: {:.2f}".format(grausF)) 