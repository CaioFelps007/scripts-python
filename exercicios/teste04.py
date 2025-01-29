n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo numero: "))

di = n1/n2
soma = n1+n2
potencia = n1**n2

print(' A soma entre {} e {} é {} '.format(n1,n2,n1+n2), end=" ")
#print('{} é um numerico? {}'.format(n1+n2, str(n1+n2).isnumeric()))
print("E a divisão é {:.3f} , e a potencia é {}".format(di, potencia))