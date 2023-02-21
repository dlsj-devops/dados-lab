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
elif (a < b):
    print("B é maior do que A ({} > {})".format(b, a))
else:
    print("A e B são iguais")

#calculo de preços de acrodo com a forma de pagamento
forma_pagamento = input("Forma de pagamento [c|d|b|o]: ")

if (forma_pagamento == 'c'):
    print("Pagamento no crédito sem desconto.")

elif (forma_pagamento == 'd'):
    print("Pagamento no débito com 3% de desconto.")

elif (forma_pagamento == 'b'):
    print("Pagamento no boleto com 5% de desconto")

elif (forma_pagamento == 'o'):
    print("Pagamento no dinheiro com 10% de desconto")

else:
    print("Opção '{}' não cadastrada".format(forma_pagamento))

#testes dentro de outros teste
idade = int(input("Digite sua idade: "))

if (idade >= 16):
    print("Você já pode votar se tiver título de eleitor.")
    if (idade >= 18) and (idade <= 70):
        print("Se voĉe é alfabetizado,seu voto é obrigatório.")
    else:
        print("Seu voto é facultativo.")
else:
    print("Você ainda não pode votar...")


