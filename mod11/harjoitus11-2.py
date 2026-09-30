# harjoitus 2 -- 9 ja 10 moduulin auto tehtäviin perustuva ohjelma, jossa autolla on aliluokat
#sähköauto ja polttomoottoriauto.

class Auto: # yliluokka
    def __init__(self, rekisterinumero, huippunopeus):
        self.rekisterinumero = rekisterinumero
        self.huippunopeus = huippunopeus
        self.nykyinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nykyinen_nopeus += muutos
        if self.nykyinen_nopeus > self.huippunopeus:
            self.nykyinen_nopeus = self.huippunopeus
        elif self.nykyinen_nopeus < 0: 
            self.nykyinen_nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nykyinen_nopeus * tunnit

class Sahkoauto(Auto): # aliluokka1
    def __init__(self, rekisterinumero, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisterinumero, huippunopeus)

class Polttomoottoriauto(Auto): # aliluokka2
    def __init__(self, rekisterinumero, huippunopeus, tankin_koko):
        self.tankin_koko = tankin_koko
        super().__init__(rekisterinumero, huippunopeus)

def tulosta_tilanne(auto): # tulosta_tilanne on muutettu aiemmista tehtävistä yksinkertaisemmiksi, koska sillä on pienempi rooli tehtävässä
    print(auto.rekisterinumero,"\t\t", auto.kuljettu_matka,"km")
    

s_auto1 = Sahkoauto("ABC-15 ", 180, 52.5)
p_auto1 = Polttomoottoriauto("ACD-123", 165, 32.3)

s_auto1.kiihdyta(30)
p_auto1.kiihdyta(35)

s_auto1.kulje(3)
p_auto1.kulje(3)

print("Rekisterinumero:\t Kulkettu matka:")
tulosta_tilanne(s_auto1)
tulosta_tilanne(p_auto1)
print("---")