#

import etsi_funktiot

class Pelaaja:
    def __init__(self,nimi,ika,sijainti="x",tod=6):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.tod = tod
        self.inventaario = []

    def kutsu_profiili(self): # kertoo pelaajan nimen ja iän, antaa muuttaa ne.
        print(f"Nimesi on {self.nimi} ja ikäsi on {self.ika}.\n")
        print(f"Sijantisi on {self.sijainti}.\n")

        x = input("Haluatko muuttaa nimesi tai ikäsi? (k/e): ")
        while x != "k" and x != "e":
            x = input("Haluatko muuttaa nimesi tai ikäsi? (k/e): ")

        if x == "k":
            self.nimi = input("Mikä on nimesi: ")
            self.ika = int(input("Kuinka vanha olet: "))

    def kutsu_loydot(self): # tulostaa inventaarion, kertoo myös esineiden määrän inventaariossa
        inv_maara = 0
        tehdyt = []

        print("Löytösi:\n")

        for i in self.inventaario: 
            #loop tulostaa jokaisen uniikin esineen kerran, ja kertoo montako niitä on
            # esim. esine1 - 3 kpl, esine2 - 5 kpl
            if i in tehdyt:
                pass
            else:
                maara = self.inventaario.count(i)
                inv_maara += maara
                print(f"{i} - {maara} kpl")
                tehdyt.append(i)

        input(f"Sinulla on {inv_maara} löytöä.") # kertoo montako esinettä inventaariossa on yhteensä
        tehdyt.clear()


    def kutsu_etsi(self):
        if self.sijainti == "metsä":
            etsi_funktiot.etsi_alue1(self.inventaario)
        elif self.sijainti == "vuoret":
            etsi_funktiot.etsi_alue2(self.inventaario)
        elif self.sijainti == "niitty":
           self.tod = etsi_funktiot.etsi_alue3(self.inventaario, self.tod)
        elif self.sijainti == "pellot":
            etsi_funktiot.etsi_alue4(self.inventaario)