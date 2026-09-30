# eri etsi funktioita
import random

def etsi_alue1(inv):
    print("Lähdet etsimään...\n")
    suunta1 = input("Mihin suuntaan lähdet etsimään? (vasemmalle, oikealle, suoraan): ").lower()
    if suunta1 == "vasemmalle":
        print("Saavut aukiolle, jonka peittää pienet sienet kauttaaltaan. Poimit yhden.")
        print("Löysit sienen!")
        inv.append("Sieni")
    elif suunta1 == "oikealle":
        print("Huomaat valtavan kuolleen pensaan. Katkaiset yhden oksan.")
        print("Löysit kepin!")
        inv.append("Keppi")
    elif suunta1 == "suoraan":
        print("Löysit valtavan kiven!")
        print("Kivi on liian suuri ottaa mukaan.")
    print("\nPalaat takaisin alkuun.\n") 
    input("") 

def etsi_alue2(inv):
    print("Saavut vuoristoiselle alueelle, joka on tunnettu lähteistään.")
    input("Lähde etsimään painamalla mitä tahansa nappia.")
    arpa = random.randint(1,3)
    if arpa == 1:
        print("Saavut lähteelle, jonka vesi on niin kirkasta, että näet pohjaan asti. Täytät vesipullon.")
        print("Löysit vesipullon!")
        inv.append("Vesi")
    elif arpa == 2:
        print("Kuulet veden virtausta läheltä. Löydät lammikon, johon virtaa kirkaan vihreetä liejua.")
        print("Pitää jatkaa etsimistä...")
    elif arpa == 3:
        print("Saavut lähteelle, mutta vesi haisee mädältä kananmunalta.")
        print("Pitää jatkaa etsimistä...")

def etsi_alue3(inv):
    print("Saavut avoimelle niitylle täynnä kukkia. Näet ihmisiä tekevän jotain kukkien seassa.")
    # voit etsiä tai kitkeä
    # jokainen kitkeminen nostaa etsimisen onnistumista
    tod = 6

    x = input("Mitä aiot tehdä? (kitke, tutki)").lower
    if x != "kitke" and x != "tutki":
        x = input("Mihin menet? (kitke, tutki)").lower

    if x == "auta":
        print("Autat tutkijoita.")
        tod -= 1
    elif x == "tutki":
        arpa = random.randint(1,tod)
        if arpa == 1:
            print("Löysit kukan!")
            inv.append("Kukka")
        else:
            print("Et löytänyt kukkaa. Kitkemällä vieraslajia parannat kukan kasvumahdollisuuksia.")
    input("")

    
def etsi_alue4(inv):
    print("Saavut pelloille, jossa vihertävät istutukset jatkuvat silmänkantamattomiin, ja silloin")
    print("tällöin peltojen seassa on ihmisten asutuksia ja aittoja.")
    print("Tiesi haarautuu kahteen suuntaan: punaiseksi maalattuun maatilarakennukseen")
    print("ja vesivoimalla toimivaan myllyyn.")

    x = input("Mihin menet? (maatila, mylly)").lower
    if x != "maatila" and x != "mylly":
        x = input("Mihin menet? (maatila, mylly)").lower

    if x == "maatila":
        print("Tutkit maatilaa ja sen rakennuksia.")
        print("Löydät maatilan takaa pensaan, josta löytyy punaisen kuultavia marjoja.")
        print("Löysit marjat.")
        inv.append("Marjat")
    elif x == "mylly":
        print("Myllyssä on vesivoimalla toimiva mehustin.")
        if inv.count("Marjat") >= 1:
            print("Asetat marjat mehustimeen ja käännät sen vipua.")
            print("Löysit mehua!")
            inv.remove("Marjat")
            inv.append("Mehu")

