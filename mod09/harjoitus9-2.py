# harjoitus 2 -- lisätään edelliseen tehtävän luokkaan kiihdytä funktio, jolla audon nykyistä
# nopeutta voi muuttaa

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
        
auto1 = Auto("ABC-123", 142)

auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(str(auto1.nykyinen_nopeus) + " km/h")

auto1.kiihdyta(-200)

print(str(auto1.nykyinen_nopeus) + " km/h")