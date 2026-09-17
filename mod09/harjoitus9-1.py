# harjoitus 1 -- tehdään luokka auto, jonka oliolla on rekisterinumero, huippunopeus, nykyinen nopeus
# ja kuljettu matka. Tulostetaan luokkaan luodun auto1 olion kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisterinumero, huippunopeus, nykyinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = nykyinen_nopeus
        self.kuljettu_matka = kuljettu_matka

auto1 = Auto("ABC-123", 142) 

print(f"Auton rekisterinumero on {auto1.rekisterinumero}.")
print(f"Auton huippunopeus on {auto1.huippunopeus} km/h.")
print(f"Auton nykyinen nopeus on {auto1.nykyinen_nopeus} km/h.")
print(f"Auton kulkema matka on {auto1.kuljettu_matka} km.")



