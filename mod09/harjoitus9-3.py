# harjoitus 3 -- lisää tehtävän kaksi ohjelmaan kulje metodi, joka muuttaa kuljettua matkaa sen mukaan, 
# kauanko on matkattu. Ohjelmaan on asetettu esimerkkiluvut ominaisuuksille.

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
        
auto1 = Auto("ABC-123", 142, 60, 2000)

auto1.kulje(1.5)

print(f"Kuljettu matka on {auto1.kuljettu_matka} km.")

