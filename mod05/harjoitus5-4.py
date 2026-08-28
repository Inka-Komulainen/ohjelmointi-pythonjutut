# harjoitus 4 -- ohjelma arpoo luvun 1-10 väliltä, käyttäjä arvaa lukua kunnes hän saa sen oikein
# ohjelma myös kertoo, onko väärä arvaus liian pieni tai suuri.

import random

iLuku = random.randint(1,10) # arpoo luvun
iArvaus = 0

while iArvaus != iLuku: # while loppuu, kun luku on arvattu oikein.
    iArvaus = int(input("Arvaa luku 1 ja 10 välillä: "))

    #kertoo onko arvaus liian suuri tai pieni
    if iArvaus > iLuku:
        print("Liian suuri arvaus.")
    elif iArvaus < iLuku:
        print("Liian pieni arvaus.")

print("Oikein!")