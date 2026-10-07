# ensimmäinen peliprojektini

# kestävän kehityksen teema: pelaaja etenee pelissä uusille alueille, joissa hänen täytyy
# auttaa ihmisiä. Jokaisen alueen ongelma edustaa jotakin kestävän kehityksen teemaa.
import sys
import os
import json
from alue_luokka import Alue
from pelaaja_luokka import Pelaaja
import visuaalit

def kutsu_paavalikko():
    while True:
        print(f"\nTervetuloa päävalikkoon, {pelaaja1.nimi}!")
        print("\nEtene\nProfiili\nEtsi\nLöydöt (inventaario)\nLopeta\n")
    
        toiminto = input("Mitä haluat tehdä: ").lower()
        if toiminto == "profiili": # päävalikon toiminto "profiili" kertoo pelaajan tiedot, ja antaa päivittää niitä
            pelaaja1.kutsu_profiili()
            if pelaaja1.ika < 12: # pelaaja voi muuttaa ikänsä myöhemmin alle 12 vuotiaaksi, jolloin peli ei anna pelaajan jatkaa
                print("Hei! Olet liian nuori! Älä yritä huijata!")
                sys.exit()
    
        elif toiminto == "etene": # pääsee pelin uudelle alueelle
            onnistuminen = ""
            if pelaaja1.sijainti == "metsä":
                onnistuminen, pelaaja1.sijainti = alue1.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
            elif pelaaja1.sijainti == "vuoret":
                onnistuminen, pelaaja1.sijainti = alue2.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
            elif pelaaja1.sijainti == "niitty":
                onnistuminen, pelaaja1.sijainti = alue3.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
            elif pelaaja1.sijainti == "pellot":
                onnistuminen, pelaaja1.sijainti = alue4.kutsu_etene(pelaaja1.inventaario, pelaaja1.sijainti)
    
            if onnistuminen == True:
                return
    
        elif toiminto == "etsi": # päävalikon toiminto "etsi" avulla pelaaja löytää uusia esineitä
            pelaaja1.kutsu_etsi()
    
        elif toiminto == "löydöt" or toiminto == "inventaario": # tulostaa inventaarion
            pelaaja1.inventaario.sort()
            pelaaja1.kutsu_loydot()
    
        elif toiminto == "lopeta": # lopettaa pelin ja tallentaa tilanteen
            data = [pelaaja1.nimi,pelaaja1.ika,pelaaja1.sijainti,pelaaja1.inventaario,Alue.alueet]
            with open("tallennus.json", "w") as tiedosto:
                json.dump(data, tiedosto)
            sys.exit()

def kutsu_kuvaus():
    if pelaaja1.sijainti == "metsä": # hakee oikean kuvauksen, oikealle alueelle
        polku = alue1.kuvaus
    elif pelaaja1.sijainti == "vuoret":
        polku = alue2.kuvaus
    elif pelaaja1.sijainti == "niitty":
        polku = alue3.kuvaus
    elif pelaaja1.sijainti == "pellot":
        polku = alue4.kuvaus

    with open(polku, "r", encoding="utf-8") as tiedosto:
        teksti = tiedosto.read()
        print(teksti)
        input()



# pääohjelma alkaa tästä
pelaaja1 = Pelaaja("",0)

alue1 = Alue("metsä","peliprojekti/kuvaukset/kuvaus1.txt",["Sieni","Sieni","Keppi"])
alue2 = Alue("vuoret","peliprojekti/kuvaukset/kuvaus2.txt",["Vesi","Vesi","Vesi","Vesi","Vesi"])
alue3 = Alue("niitty","peliprojekti/kuvaukset/kuvaus3.txt",["Kukka"])
alue4 = Alue("pellot","peliprojekti/kuvaukset/kuvaus4.txt",["Mehu"])

try: # hakee pelaajan tallennetut tiedot, jos peliä pelaataan ekaa kertaa kysyy tiedot
    with open("tallennus.json","r") as tiedosto:
        data = json.load(tiedosto)
        pelaaja1.nimi = data[0]
        pelaaja1.ika = data[1]
        pelaaja1.sijainti = data[2]
        pelaaja1.inventaario = data[3]
        Alue.alueet = data[4]
except FileNotFoundError:
    
    while True:
        try:
            pelaaja1.nimi = input("Kerro nimesi: ")
            pelaaja1.ika = int(input("Kerro ikäsi: "))
            break
        except ValueError:
            print("Ilmoita ikäsi numerona.")


print(f"Nimesi on {pelaaja1.nimi} ja ikäsi on {pelaaja1.ika}.\n")

if (pelaaja1.ika >= 12): # ei anna alle 12-vuotiasta päästä päävalikkoon
    pass
else:
    print("Et taida olla vielä tarpeeksi vanha.")
    sys.exit()

toiminto = ""

while len(Alue.alueet) > 0: #while loop loppuu, kun pelin voittaa
    #ennen päävalikkoon pääsyä pelaajan tulee valita alue, jonka hän aikoo pelastaa
    while pelaaja1.sijainti != "metsä" and pelaaja1.sijainti != "vuoret" and pelaaja1.sijainti != "niitty" and pelaaja1.sijainti != "pellot":
        print("Mitä aluetta haluat auttaa?\n")
        for i in Alue.alueet:
            print(i)
        print("")
        pelaaja1.sijainti = input("Valitse: ").lower()

    kutsu_kuvaus()
    kutsu_paavalikko()


print("Voitit pelin!")
visuaalit.loppu_visuaali()

# tähän extraa jos ehdin

if os.path.exists("tallennus.json"): # poistaa tallennuksen, kun peli on ohi.
    os.remove("tallennus.json")

