# harjoitus 1 -- kysyy noppien lukumäärän, heittää kerran kaikki nopat ja tulostaa niiden summan

import random

i = 1
silmäluvut = []
nopat = int(input("Montako noppaa heitetään: "))

while i <= nopat: # arpoo kysytyn määrän noppia, ja lisää ne listaan
    silmäluvut.append(random.randint(1,6))
    i += 1

summa = 0

for luku in silmäluvut: #tulostaa jokaisen listaan lisätyn nopanheiton ja lisää ne yhteen
    print(luku)
    summa += luku

print("Summa: " + str(summa))