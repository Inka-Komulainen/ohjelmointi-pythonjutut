
class Lentokone:
    def __init__(self, nimi, tankki_max, tankki_nyt = 0):
        self.koneen_nimi = nimi
        self.koneen_tankin_maksimi = tankki_max
        self.koneen_tankki_nyt = tankki_nyt

    def tankkaa(self):
        ero = self.koneen_tankin_maksimi - self.koneen_tankki_nyt
        print(f"Koneeseen mahtui {ero} l bensaa.")

        self.koneen_tankki_nyt = self.koneen_tankin_maksimi 

    def tulosta_tiedot(self):
        print(f"Koneen nimi on {self.koneen_nimi}.")
        print(f"Koneen tankin maksimi on {self.koneen_tankin_maksimi} l.")
        print(f"Koneen tankissa on nyt {self.koneen_tankki_nyt} l.")

class Lentokentta:
    def __init__(self, nimi):
        self.kentan_nimi = nimi
        self.koneet = []

    def tulosta_koneet(self):
        for i in self.koneet:
            i.tulosta_tiedot()

    def lisaa_lentokone(self, lentokone):
        self.koneet.append(lentokone)

lentokone1 = Lentokone("nimi1", 110, 30)
lentokone2 = Lentokone("nimi2", 120)

lentokone2.tankkaa()

lentokentta1 = Lentokentta("olen lentokenttä.")

lentokentta1.lisaa_lentokone(lentokone1)
lentokentta1.lisaa_lentokone(lentokone2)

lentokentta1.tulosta_koneet()



    

