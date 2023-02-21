import copy

import pandas as pd
import matplotlib.pyplot as plt

m1 = [ [0, 0], [1, 1], [2, 2] ]

m2 = copy.deepcopy(m1)

m1[0][0] = 5

m1[1] = [-9, -9]

print(m2)

print(m1)

lista = ["Orozimbo Maia", "Alferes Poli", "Anita Garibaldi", "Claudio Torres Junior", "Anne Frank", "Daisy Lucy Berno"]

qtd_letra_o = 0

for item in lista:
    linha = item;
    print(linha)
    for letra in linha:
        print(letra)
        if letra == 'o' or letra == 'O':
            qtd_letra_o = qtd_letra_o + 1
print("Quantidade de letras o/O: ", qtd_letra_o)

print("lista: ", lista)
lista.sort()
print("ordenado ", lista)

dados = {'T1': [1, 0, 2], 'T2': [0, 3, 0], 'T3': [1, 1, 1]}

df = pd.DataFrame(dados)

df.plot(kind = 'bar')
plt.show()