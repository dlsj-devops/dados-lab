def testePrint(flag):
    if (flag):
        print("Dentro do if")
    else:
        print("Dentro do else")

entrou = True
testePrint(entrou)
testePrint(not entrou)

resposta = int(input("Qual o número correto?\nR: "))
if resposta != 42:
    print("Errou, tente novamente!")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Pode dirigir no Brasil")
if idade < 18:
    print("Não pode dirigir no Brasil")
if idade > 15:
    print("Pode dirigir nos EUA")
#uso de parenteses melhora legibilidade do código
if (idade >= 16) and (idade < 21):
    print("Pode dirigir, mas não pode comprar álcool nos EUA")

#elif
#imprimir o maior dentre dois números

a = int(input("digite valor de 'A': "))
b = int(input("digite o valor de 'B': "))
if (a > b):
    print("A é maior do que B ({} > {})".format(a, b))
else:
    print("B é maior do que A ({} > {})".format(b, a))