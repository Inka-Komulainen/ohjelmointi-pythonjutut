# ensimmäinen peliprojektini

# kestävän kehityksen teema: pelaaja etenee pelissä uusille alueille, joissa hänen täytyy
# auttaa ihmisiä. Jokaisen alueen ongelma edustaa jotakin kestävän kehityksen teemaa.
import sys
from alue_luokka import Alue
from pelaaja_luokka import Pelaaja


# pääohjelma alkaa tästä

alue1 = Alue("metsä","kuvaus1.txt",["Sieni","Sieni","Keppi"])
alue2 = Alue("vuoret","kauniit vuoret",["Vesi"])
alue3 = Alue("niitty","kaunis niitty",["Kukka"])
alue4 = Alue("pellot","kaunis pelto",["Mehu"])

pelaaja1 = Pelaaja(input("Mikä on nimesi: "), int(input("Kuinka vanha olet: ")))

print(f"Nimesi on {pelaaja1.nimi} ja ikäsi on {pelaaja1.ika}.\n")

if (pelaaja1.ika >= 12): # ei anna alle 12-vuotiasta päästä päävalikkoon
    pass
else:
    print("Et taida olla vielä tarpeeksi vanha.")
    sys.exit()

toiminto = ""

while Alue.tehdyt_alueet < 4 and toiminto != "lopeta":
    while pelaaja1.sijainti != "metsä" and pelaaja1.sijainti != "vuoret" and pelaaja1.sijainti != "niitty" and pelaaja1.sijainti != "pellot":
        print("Mitä aluetta haluat auttaa?\n")
        for i in Alue.alueet:
            print(i)
        print("")
        pelaaja1.sijainti = input("Valitse: ").lower()

    with open("kuvaus1.txt", "r") as tiedosto:
        teksti = tiedosto.read()
        print(teksti)
        input()

    while toiminto != "lopeta":
        print(f"\nTervetuloa päävalikkoon, {pelaaja1.nimi}!")
        print("\nEtene\nProfiili\nEtsi\nLöydöt (inventaario)\nLopeta\n")

        toiminto = input("Mitä haluat tehdä: ").lower()
        if toiminto == "profiili": # päävalikon toiminto "profiili" kertoo pelaajan tiedot, ja antaa päivittää niitä
            pelaaja1.kutsu_profiili()
            if pelaaja1.ika < 12: # pelaaja voi muuttaa ikänsä myöhemmin alle 12 vuotiaaksi, jolloin peli ei anna pelaajan jatkaa
                print("Hei! Olet liian nuori! Älä yritä huijata!")
                sys.exit()
        elif toiminto == "etene":
            onnistuminen = ""
            if pelaaja1.sijainti == "metsä":
                onnistuminen = alue1.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
            elif pelaaja1.sijainti == "vuoret":
                onnistuminen = alue2.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
            elif pelaaja1.sijainti == "niitty":
                onnistuminen = alue3.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
            elif pelaaja1.sijainti == "pellot":
                onnistuminen = alue4.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)

            if onnistuminen == True:
                break

        elif toiminto == "etsi": # päävalikon toiminto "etsi" avulla pelaaja löytää uusia asioita, tulee muuttumaan tulevaisuudessa 
            pelaaja1.kutsu_etsi()
        elif toiminto == "löydöt" or toiminto == "inventaario": # tulostaa inventaarion
            pelaaja1.inventaario.sort()
            pelaaja1.kutsu_loydot()

if Alue.tehdyt_alueet == 4:

    print("Voitit pelin!")
