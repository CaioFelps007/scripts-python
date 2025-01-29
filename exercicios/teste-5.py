n1 = int(input("Digite o número da sua escolha: "))
print(' o antecessor desse número é: {}, o número é: {}, e o sucessor é: {}'.format(n1-1,n1,n1+1))

# Conta
n2 = int(input("Digite outro número: "))
print("O seu dobro é: {}, o seu triplo é: {}, e sua raiz quadrada é: {}".format(n2*2,n2*3,n2**(1/2)))

# Média
nota1 = float(input(' A nota desse aluno foi: '))
nota2 = float(input('A segunda nota desse aluno foi: '))
print('A média desse aluno é de: {}'.format((nota1+nota2)/2))

#Conversao metros em cm e mm
Metro = float(input("Informe quantos metros você quer: "))
ConversaoCM = Metro * 100
ConversaoMM = Metro * 1000 
print('O valor em centimentro é de: {} e em milímetro é de {}'.format(ConversaoCM,ConversaoMM))

#Tabuada
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(numero, i,numero * i))

#conversaoDL
valor = float(input("Digite quantos R$BRL você tem: "))
cotacao = valor / 5.86
print('{:.4} é o valor que você tem em Dólar'.format(cotacao))

#Pintando a Parede
largura = int(input('Digite a largura da sua parede: '))
altura = int(input('Digite a altura da sua parede: '))
m2 = largura * altura
print(f'Sua parede tem {m2} metros quadrados')
# Litros de tinta
metrosQuadrados = int(input('Digite quantos metros quadrados tem sua parede: '))
litros_tinta = metrosQuadrados / 2
print(f'É necessário {litros_tinta} litros de tinta para pintar sua parede!')

# Desconto do preço

preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.05
valorFinal = preco - desconto
print('o valor do produto com desconto é de: {}'.format(valorFinal))

#Salario
Salario = float(input('Digite seu salário: '))
porcentagem = Salario * 0.15

print('O valor do aumento é de: {}'.format(Salario + porcentagem))