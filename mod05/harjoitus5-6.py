# harjoitus 6 -- ohjelma laskee piin likiarvon arpomalla yksikköympyrää sivuavaan neliöön pisteitä
# (4 * n/N) kertoo piin likiarvon, jossa n on ympyrän sisällä olevat pisteet, ja N kaikki pisteet

import random

i = 1
iYmpyraN = 0 # aiemman kaavan n
iKaikkiN = int(input("Monella pisteellä piin likiarvo lasketaan: ")) # aiemman kaavan N

while i <= iKaikkiN:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    #print(x, y, sep = " ")  #käytettiin testauksessa, että saatiin pisteitä oikealta väliltä

    if x ** 2 + y ** 2 < 1: #suurentaa n yhdellä, aina kun piste on ympyrän sisällä
        iYmpyraN +=1

    i +=1

fPii = 4 * iYmpyraN / iKaikkiN # laskee piin likiarvon
print(f"Piin likiarvo: {fPii:.3f}")