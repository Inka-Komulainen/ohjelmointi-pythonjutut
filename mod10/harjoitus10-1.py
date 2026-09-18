# harjoitus 1 -- ohjelmassa on hissi luokka, jonka hissi-oliolla on ylin ja alin kerros. Hissiä voi liikuttaa
# mihin vain sillä olevaaan kerrokseen

class Hissi:
    def __init__(self, nykyinen_kerros, ylin_kerros, alin_kerros):
        self.nykyinen_kerros = nykyinen_kerros
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros

    def kerros_ylos(self): # liikuttaa hissia kerroksen ylöspäin
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
        print(f"Nykyinen kerros on {self.nykyinen_kerros}.")

    def kerros_alas(self): # liikuttaa hissia kerroksen alaspäin
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
        print(f"Nykyinen kerros on {self.nykyinen_kerros}.")

    def siirry_kerrokseen(self, kerros):
        if kerros > self.nykyinen_kerros: # nostaa hissiä ylöspäin kunnes se on halutussa kerroksessa
            while self.nykyinen_kerros != kerros:
                self.kerros_ylos()
        elif kerros < self.nykyinen_kerros: # laskee hissiä alaspäin kunnes se on halutussa kerroksessa
            while self.nykyinen_kerros != kerros:
                self.kerros_alas()
        print("---")

h = Hissi(0,9,0) # luodaan hissi, jolla on kerrokset 0-9.

h.siirry_kerrokseen(5) # kerrokseen 5
h.siirry_kerrokseen(0) # alimpaan kerrokseen

