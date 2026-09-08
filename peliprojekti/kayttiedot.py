# ensimmäinen peliprojektini

def kutsu_profiili(nimi, ika): # kertoo pelaajan nimen ja iän, antaa muuttaa ne.
    print(f"Nimesi on {nimi} ja ikäsi on {ika}.\n")

    x = input("Haluatko muuttaa nimesi tai ikäsi? (k/e): ")
    while x != "k" and x != "e":
        x = input("Haluatko muuttaa nimesi tai ikäsi? (k/e): ")

    if x == "k":
        nimi = input("Mikä on nimesi: ")
        ika = int(input("Kuinka vanha olet: "))
        return nimi, ika
    elif x == "e":
        return nimi, ika

# tällä toiminolla pelaaja etenee pelin seuraavalle alueelle, jonka on tarkoitus tulevaisuudessa sekoittaa
# mitä voit löytää etsi toiminnolla
def kutsu_etene(): 
    print("Jatkaessasi eteenpäin näet valtavan röllin istuvan sillalla. Kun pääset hänet luokseen, hän sanoo:")
    print("'Et pääse sillan yli, josset anna minulle kahta sientä ja keppiä. Haluan sieniä vartaalla lounaaksi!'")

    x = input("Onko sinulla 2 sientä ja keppi? (k/e): ")
    while x != "k" and x != "e":
            x = input("Onko sinulla 2 sientä ja keppi? (k/e): ")

    if x == "k":
        print("Anteeksi, en ole ehtinyt ohjelmoida näin pitkälle!")
        return 
    elif x == "e":
        print("Et pääse sillan yli. Palataan aiemmalle alueelle etsimään.")
        return 




def kutsu_etsi(inv): # etsi toiminnon funktio, tämän kautta pelaaja löytää uusia esineitä inventaarioon
    print("\nLähdet etsimään...")
    suunta1 = input("Mihin suuntaan lähdet etsimään? (vasemmalle, oikealle, suoraan): ").lower()
    if suunta1 == "vasemmalle":
        print("Löysit sienen!")
        inv.append("Sieni")
    elif suunta1 == "oikealle":
        print("Löysit kepin!")
        inv.append("Keppi")
    elif suunta1 == "suoraan":
        print("Löysit valtavan kiven!")
        print("Kivi on liian suuri ottaa mukaan.")
    print("Palaat takaisin alkuun.\n") 
    return

def kutsu_loydot(inv): # tulostaa inventaarion, kertoo myös asoiden määrän inventaariossa
    kerrat = 0
    for i in inv:
        print(i)
        kerrat += 1
    print(f"Sinulla on {kerrat} löytöä.")
    return

# pääohjelma alkaa tästä

pelaajan_nimi = input("Mikä on nimesi: ")
pelaajan_ika = int(input("Kuinka vanha olet: "))

print(f"Nimesi on {pelaajan_nimi} ja ikäsi on {pelaajan_ika}.\n")

#luodaan inventaario:
inventaario = list()

# päävalikko alkaa tästä
toiminto = ""

if (pelaajan_ika >= 12): # ei anna alle 12-vuotiasta päästä päävalikkoon
    while toiminto != "lopeta":
        print(f"Tervetuloa päävalikkoon, {pelaajan_nimi}!")
        print("\nEtene\nProfiili\nEtsi\nLöydöt (inventaario)\nLopeta\n")

        toiminto = input("Mitä haluat tehdä: ").lower()
        if toiminto == "profiili": # päävalikon toiminto "profiili" kertoo pelaajan tiedot, ja antaa päivittää niitä
            pelaajan_nimi, pelaajan_ika = kutsu_profiili(pelaajan_nimi, pelaajan_ika)
            if pelaajan_ika < 12: # pelaaja voi muuttaa ikänsä alle 12 vuotiaaksi, jolloin peli ei anna pelaajan jatkaa
                print("Hei! Olet liian nuori! Älä yritä huijata!")
                break
        elif toiminto == "etene":
            kutsu_etene()
        elif toiminto == "etsi": #päävalikon toiminto "etsi" avulla pelaaja löytää uusia asioita, tulee muuttumaan tulevaisuudessa 
            kutsu_etsi(inventaario)
        elif toiminto == "löydöt" or toiminto == "inventaario": # tulostaa inventaarion
            inventaario.sort()
            kutsu_loydot(inventaario)
            
else:
    print("Et taida olla vielä tarpeeksi vanha.")

