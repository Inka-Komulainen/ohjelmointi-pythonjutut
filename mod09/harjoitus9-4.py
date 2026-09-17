# harjoitus 4 -- 

import random

class Auto:
    def __init__(self, rekisterinumero, huippunopeus, nykyinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdyta(self, muutos):
        self.nykyinen_nopeus += muutos
        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif self.nykyinen_nopeus < 0:
            self.nykyinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nykyinen_nopeus * tunnit
        
kilpailevat_autot = dict() # pelin autot luodaan sanakirjaan

for i in range(10): # tämä loop luo auto-oliot, luo niiden rekisterinumeron ja arpoo huippunopeuden
    nimi = "ABC-" + str(i+1)
    avain = "auto" + str(i+1)
    kilpailevat_autot.update({avain : Auto(nimi, random.randint(100,200))})

voittaja_auto = 0

while voittaja_auto < 10000:

    for i in kilpailevat_autot.values(): # kiihdyttää autot arpomalla muutoksia -10 - 15km/h 
        arvottu_muutos = random.randint(-10, 15)
        i.kiihdyta(arvottu_muutos)

    for i in kilpailevat_autot.values(): # kertoo matkan tunnissa aiemmin arvottujen nopeuksien perusteella
        i.kulje(1)

    for i in kilpailevat_autot.values():
        if i.kuljettu_matka > voittaja_auto:
            voittaja_auto = i.kuljettu_matka

print("Rekisterinumero:\tHuippunopeus:\tNykyinen nopeus:\tKulkettu matka:")

for i in kilpailevat_autot.values():
    print(i.rekisterinumero,"\t\t\t", i.huippunopeus,"\t\t", i.nykyinen_nopeus, "\t\t\t", i.kuljettu_matka)
