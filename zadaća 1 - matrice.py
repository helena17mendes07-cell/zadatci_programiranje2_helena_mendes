#Napisati program koji generira kvadratnu matricu dimenzija 7x7.
#Elementi su nasumični brojevi od 1 do 9.
#Zatim napisati program koji računa zbroj elemenata na rubovima matrice.

import random

matrica=[]

for i in range(7):
    red=[]
    for j in range(7):
        red.append(random.randint(1,9))
    matrica.append(red)

zbroj=0

for i in range(7):
    print(matrica[i])
    for j in range(7):
        if i==0 or i==6 or j==0 or j==6:
            zbroj +=matrica[i][j]

print("Zbroj rubova=",zbroj)
