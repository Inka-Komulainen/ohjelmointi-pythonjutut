# harjoitus 3 -- lisätään palohälytys metodi, joka kutsuu hissit pohjakerrokseen

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

class Talo:
    def __init__(self, ylin_kerros, alin_kerros, hissien_maara):
        self.ylin_kerros = ylin_kerros
        self.alin_kerros = alin_kerros
        self.hissien_maara = hissien_maara
        self.hissit = {}

        for i in range(0,self.hissien_maara): # luo hissit talo-oliolle
            self.hissit[i+1] = Hissi(self.ylin_kerros, self.ylin_kerros, self.alin_kerros)

    def aja_hissia(self, nimi, kerros): # liikuttaa haluttua hissiä haluttuun kerrokseen
        self.hissit[nimi].siirry_kerrokseen(kerros)

    def palohalytys(self):
        for i in self.hissit.values():
            i.siirry_kerrokseen(0)


mytalo = Talo(9, 0, 2)
mytalo.aja_hissia(1,5)
mytalo.palohalytys()
