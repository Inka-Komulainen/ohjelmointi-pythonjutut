# ensimmäinen peliprojektini

# kestävän kehityksen teema: pelaaja etenee pelissä uusille alueille, joiden resurssit ovat
# saatu enemmän tai vähemmän kestävän kehityksen perusteella
# resurssien keräämiseen on eri vaikeustasoja jne. tämän perusteella???

import etsi_funktiot

class Pelaaja:
    def __init__(self,nimi,ika,sijainti=""):
        self.nimi = nimi
        self.ika = ika
        self.sijainti = sijainti
        self.inventaario = []

    def kutsu_profiili(self): # kertoo pelaajan nimen ja iän, antaa muuttaa ne.
        print(f"Nimesi on {self.nimi} ja ikäsi on {self.ika}.\n")

        x = input("Haluatko muuttaa nimesi tai ikäsi? (k/e): ")
        while x != "k" and x != "e":
            x = input("Haluatko muuttaa nimesi tai ikäsi? (k/e): ")

        if x == "k":
            self.nimi = input("Mikä on nimesi: ")
            self.ika = int(input("Kuinka vanha olet: "))

    def kutsu_loydot(self): # tulostaa inventaarion, kertoo myös esineiden määrän inventaariossa
        inv_maara = 0
        tehdyt = []

        for i in self.inventaario: 
            #loop tulostaa jokaisen uniikin esineen kerran, ja kertoo montako niitä on
            # esim. esine1 - 3 kpl, esine2 - 5 kpl
            if i in tehdyt:
                break
            else:
                maara = self.inventaario.count(i)
                inv_maara += maara
                print(f"{i} - {maara} kpl")
                tehdyt.append(i)

        print(f"Sinulla on {inv_maara} löytöä.") # kertoo montako esinettä inventaariossa on yhteensä
        print("")

    def kutsu_etsi(self):
        if self.sijainti == "metsä":
            etsi_funktiot.etsi_alue1(self.inventaario)
        elif self.sijainti == "vuoret":
            etsi_funktiot.etsi_alue2(self.inventaario)
        elif self.sijainti == "niitty":
            etsi_funktiot.etsi_alue3(self.inventaario)
        elif self.sijainti == "pelto":
            etsi_funktiot.etsi_alue4(self.inventaario)


class Alue: 
    alueet = []
    tehdyt_alueet = 0
    def __init__(self, nimi, kuvaus, lahtoehto): # +esineet?
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.lahtoehto = lahtoehto
        Alue.alueet.append(self.nimi)


#etene funktio - pääsee seuraavalle alueelle tämän kautta
def kutsu_etene(inv): 
    print("Jatkaessasi eteenpäin näet valtavan röllin istuvan sillalla. Kun pääset hänet luokseen, hän sanoo:")
    print("'Et pääse sillan yli, josset anna minulle kahta sientä ja keppiä. Haluan sieniä vartaalla lounaaksi!'")

    poistot = 0
    for i in alue1.lahtoehto: #tarkistaa, onko pyydetyt esineet listassa ja poistaa ne
        for j in inv:
            if i == j:
                inv.remove(i)
                poistot += 1
                break

    if len(alue1.lahtoehto) == poistot: # tarkistaa, että
        Alue.tehdyt_alueet += 1
        Alue.alueet.remove(pelaaja1.sijainti)
        print("Annat pyydetyt esineet, ja voit jatkaa seuraavalle alueelle.")
    else:
        print("Ei ollut tarpeeksi tarvikkeita. Pakenet ennen kuin rölli ottaa sinut suihinsa.")
        

# pääohjelma alkaa tästä

alue1 = Alue("metsä","kaunis metsä",["Sieni","Sieni","Keppi"])
alue2 = Alue("vuoret","kaunis metsä",["sieni","sieni","keppi"])
alue3 = Alue("niitty","kaunis metsä",["sieni","sieni","keppi"])
alue4 = Alue("pelto","kaunis metsä",["sieni","sieni","keppi"])

pelaaja1 = Pelaaja(input("Mikä on nimesi: "), int(input("Kuinka vanha olet: ")))

print(f"Nimesi on {pelaaja1.nimi} ja ikäsi on {pelaaja1.ika}.\n")

if (pelaaja1.ika >= 12): # ei anna alle 12-vuotiasta päästä päävalikkoon
    pass
else:
    print("Et taida olla vielä tarpeeksi vanha.")

#aluevalikko tähän?

toiminto = ""

while Alue.tehdyt_alueet < 4 and toiminto != "lopeta":
    print("Mitä aluetta haluat auttaa?\n")
    for i in Alue.alueet:
        print(i)
    print("")
    pelaaja1.sijainti = input("Valitse: ")

    while toiminto != "lopeta":
        print(f"Tervetuloa päävalikkoon, {pelaaja1.nimi}!")
        print("\nEtene\nProfiili\nEtsi\nLöydöt (inventaario)\nLopeta\n")

        toiminto = input("Mitä haluat tehdä: ").lower()
        if toiminto == "profiili": # päävalikon toiminto "profiili" kertoo pelaajan tiedot, ja antaa päivittää niitä
            pelaaja1.kutsu_profiili()
            if pelaaja1.ika < 12: # pelaaja voi muuttaa ikänsä myöhemmin alle 12 vuotiaaksi, jolloin peli ei anna pelaajan jatkaa
                print("Hei! Olet liian nuori! Älä yritä huijata!")
                break
        elif toiminto == "etene":
            kutsu_etene(pelaaja1.inventaario)
            break
        elif toiminto == "etsi": # päävalikon toiminto "etsi" avulla pelaaja löytää uusia asioita, tulee muuttumaan tulevaisuudessa 
            pelaaja1.kutsu_etsi()
        elif toiminto == "löydöt" or toiminto == "inventaario": # tulostaa inventaarion
            pelaaja1.inventaario.sort()
            pelaaja1.kutsu_loydot()
            


