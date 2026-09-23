# ensimmäinen peliprojektini

# kestävän kehityksen teema: pelaaja etenee pelissä uusille alueille, joiden resurssit ovat
# saatu enemmän tai vähemmän kestävän kehityksen perusteella
# resurssien keräämiseen on eri vaikeustasoja jne. tämän perusteella???

class Pelaaja:
    def __init__(self,nimi,ika,nykyinen_alue = 1):
        self.nimi = nimi
        self.ika = ika
        self.nykyinen_alue = nykyinen_alue
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


class Alue: # eri alueilla on eri suunnat joista löytyy eri esineitä
    def __init__(self, id, suunta_lkm): # +esineet?
        self.id = id
        self.suunta_lkm = suunta_lkm # arvot välillä 1-3
        self.suunnat = []


    #kutsu etene()


# tällä toiminolla pelaaja etenee pelin seuraavalle alueelle, jonka on tarkoitus tulevaisuudessa sekoittaa
# mitä voidaan löytää etsi toiminnolla
def kutsu_etene(self): 
    print("Jatkaessasi eteenpäin näet valtavan röllin istuvan sillalla. Kun pääset hänet luokseen, hän sanoo:")
    print("'Et pääse sillan yli, josset anna minulle kahta sientä ja keppiä. Haluan sieniä vartaalla lounaaksi!'")

    x = input("Onko sinulla 2 sientä ja keppi? (k/e): ")
    while x != "k" and x != "e":
            x = input("Onko sinulla 2 sientä ja keppi? (k/e): ")

    if x == "k":
        if self.inventaario.count("Sieni") >= 2 and self.inventaario.count("Keppi") >= 1:
            print("Annat röllille sienet ja kepin.")
            self.inventaario.remove("Sieni")
            self.inventaario.remove("Sieni")
            self.inventaario.remove("Keppi")

            self.nykyinen_alue = 2
        else:
            print("Ei ollut tarpeeksi tarvikkeita. Pakenet ennen kuin rölli ottaa sinut suihinsa.")
            return
        
        print("Anteeksi, en ole ehtinyt ohjelmoida pidemmälle.")
        return
        
    elif x == "e":
        print("Et pääse sillan yli. Palataan aiemmalle alueelle etsimään.")
        return 




def kutsu_etsi(inv, loot): # etsi toiminnon funktio, tämän kautta pelaaja löytää uusia esineitä inventaarioon
    print("Lähdet etsimään...\n")
    suunta1 = input("Mihin suuntaan lähdet etsimään? (vasemmalle, oikealle, suoraan): ").lower()
    if suunta1 == "vasemmalle":
        print("Saavut aukiolle, jonka peittää pienet sienet kauttaaltaan. Poimit yhden.")
        print("Löysit sienen!")
        inv.append(loot[0])
    elif suunta1 == "oikealle":
        print("Huomaat valtavan kuolleen pensaan. Katkaiset yhden oksan.")
        print("Löysit kepin!")
        inv.append(loot[1])
    elif suunta1 == "suoraan":
        print("Löysit valtavan kiven!")
        print("Kivi on liian suuri ottaa mukaan.")
    print("\nPalaat takaisin alkuun.\n") 
    input("") # tämä input on tässä, jotta pelaaja näkee lukemaan uuden tekstin
    return

loot_pool = ["Sieni","Keppi","Vesi","Kukka","Vehnä","Jauhot"]

alue1 = Alue("metsä", 3)



# pääohjelma alkaa tästä

pelaaja1 = Pelaaja("","")

pelaaja1.nimi = input("Mikä on nimesi: ")
pelaaja1.ika = int(input("Kuinka vanha olet: "))

print(f"Nimesi on {pelaaja1.nimi} ja ikäsi on {pelaaja1.ika}.\n")

# päävalikko alkaa tästä
toiminto = ""

if (pelaaja1.ika >= 12): # ei anna alle 12-vuotiasta päästä päävalikkoon
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
            kutsu_etene()
        elif toiminto == "etsi": # päävalikon toiminto "etsi" avulla pelaaja löytää uusia asioita, tulee muuttumaan tulevaisuudessa 
            kutsu_etsi(pelaaja1.inventaario, loot_pool)
        elif toiminto == "löydöt" or toiminto == "inventaario": # tulostaa inventaarion
            pelaaja1.inventaario.sort()
            pelaaja1.kutsu_loydot()
            
else:
    print("Et taida olla vielä tarpeeksi vanha.")

