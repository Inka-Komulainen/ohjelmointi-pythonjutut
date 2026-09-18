# harjoitus 4 -- muunnetaan moodulin 9 tehtävä 4 niin, että kilpailu on oma luokkansa. Tällöin voidaan
# luoda kilpailuja, joilla on eri nimiä ja pituuksia.

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

class Kilpailu:
    def __init__(self, nimi, pituus):
        self.nimi = nimi
        self.pituus = pituus
        self.kilpailevat_autot = {}
        
        for i in range(10): # tämä loop luo auto-oliot, luo niiden rekisterinumeron ja arpoo huippunopeuden
            rekisteri_n = "ABC-" + str(i+1)
            avain = "auto" + str(i+1)
            self.kilpailevat_autot[avain] = Auto(rekisteri_n, random.randint(100,200))

    def tunti_kuluu(self):
        for i in self.kilpailevat_autot.values(): # kiihdyttää autot arpomalla muutoksia -10 - 15km/h 
            arvottu_muutos = random.randint(-10, 15)
            i.kiihdyta(arvottu_muutos)

        for i in self.kilpailevat_autot.values(): # kertoo matkan tunnissa aiemmin arvottujen nopeuksien perusteella
             i.kulje(1)

    def tulosta_tilanne(self):
        print("Rekisterinumero:\tHuippunopeus:\tNykyinen nopeus:\tKulkettu matka:")
        for i in self.kilpailevat_autot.values():
            print(i.rekisterinumero,"\t\t\t", i.huippunopeus," km/h\t", i.nykyinen_nopeus, " km/h\t\t", i.kuljettu_matka,"km")
        print("---")

    def kilpailu_ohi(self):

        for i in self.kilpailevat_autot.values():
            if i.kuljettu_matka >= self.pituus:
                return True

        return False
                
ekakilpailu = Kilpailu("Suuri romuralli", 8000)

tehdyt_kerrat = 1

while ekakilpailu.kilpailu_ohi() == False:
    ekakilpailu.tunti_kuluu()

    if tehdyt_kerrat % 10 == 0:
        print(f"{tehdyt_kerrat} tuntia kulunut.")
        ekakilpailu.tulosta_tilanne()

    tehdyt_kerrat += 1

print("Lopputulokset:")
ekakilpailu.tulosta_tilanne()