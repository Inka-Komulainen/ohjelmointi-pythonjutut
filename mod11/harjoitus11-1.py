# harjoitus 1 -- Luo aliluokat kirja ja lehti, joilla on yliluokka julkaisu. Aliluokat perivät yliluokalta
# ominaisuuden ja metodin. Yläluokan metodi ylikirjoitetaan aliluokissa

class Julkaisu: # yliluokka
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
    
class Kirja(Julkaisu): #aliluokka 1
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu): # aliluokka 2
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi) 

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.paatoimittaja}")

# pääohjelma alkaa tästä

lehti1 = Lehti("Aku Ankka", "Aki Hyyppä") 
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti1.tulosta_tiedot()
print("---")
kirja1.tulosta_tiedot()