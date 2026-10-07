# eri etsi funktioita
import random
import visuaalit

def etsi_alue1(inv):
    visuaalit.etsi_visuaali()
    print("Lähdet etsimään...")
    suunta1 = input("Mihin suuntaan lähdet etsimään? (vasemmalle, oikealle, suoraan): ").lower()
    if suunta1 == "vasemmalle":
        print("Saavut aukiolle, jonka peittää pienet sienet kauttaaltaan. Poimit yhden.")
        visuaalit.loyto_visuaali()
        input("Löysit sienen!")
        inv.append("Sieni")
    elif suunta1 == "oikealle":
        print("Huomaat valtavan kuolleen pensaan. Katkaiset yhden oksan.")
        visuaalit.loyto_visuaali()
        input("Löysit kepin!")
        inv.append("Keppi")
    elif suunta1 == "suoraan":
        print("Löysit valtavan kiven!")
        print("Kivi on liian suuri ottaa mukaan.")
        visuaalit.hukassa_visuaali()
    print("Palaat takaisin alkuun.") 


def etsi_alue2(inv):
    print("Saavut vuoristoiselle alueelle, joka on tunnettu lähteistään.")
    x = input("Lähdetkö etsimään kylästä ylä- vai alarinteeseen? (ylös, alas): ").lower()
    while x != "ylös" and x != "alas":
        input("Lähdetkö etsimään kylästä ylä- vai alarinteeseen? (ylös, alas): ").lower()

    if x == "ylös":
        arpa = random.randint(1,3)
        if arpa == 1:
            print("Saavut pulppuavalle lähteelle, joka on pienen luolan päässä.")
            visuaalit.loyto_visuaali()
            input("Saat täytettyä kaksi vesitynnyriä!")
            print("Voit vierittää tynnyrit alas kylään.")
            inv.append("Vesi")
            inv.append("Vesi")
        elif arpa == 2:
            print("Seuraat vuoristopolkuja, kunnes huomaat kiertäneesi ympyrää.")
            input("Pitää jatkaa etsimistä...")
        elif arpa == 3:
            print("Saavut lähteelle, mutta vesi haisee mädältä kananmunalta.")
            print("Pitää jatkaa etsimistä...")

    elif x == "alas":
        arpa = random.randint(1,2)
        if arpa == 1:
            print("Saavut suurehkolle lähteelle, jonka vesi on niin kirkasta, että näet pohjaan asti.")
            visuaalit.loyto_visuaali()
            input("Saat täytettyä kaksi vesitynnyriä!")
            print("Kun kiipeät rinnettä ylös takaisin kylään, huomaat ettet jaksa kantamaan kahta tynnyriä.")
            print("Joudut jättämään toisen tynnyreistä rinteeseen.")
            print("Menetit vesitynnyrin!")
            inv.append("Vesi")
        elif arpa == 2:
            print("Kuulet veden virtausta läheltä. Löydät lammikon, johon virtaa kirkaan vihreetä liejua.")
            print("Pitää jatkaa etsimistä...")


def etsi_alue3(inv, tod):
    print("Saavut avoimelle niitylle täynnä kukkia. Näet ihmisiä tekevän jotain kukkien seassa.")
    # voit etsiä tai kitkeä, jokainen kitkeminen nostaa etsimisen onnistumista

    x = input("Mitä aiot tehdä? (kitke, tutki): ").lower()
    while x != "kitke" and x != "tutki":
        x = input("Mitä aiot tehdä? (kitke, tutki): ").lower()

    if x == "kitke":
        print("Autat tutkijoita vieraslajin kitkemisessä.")
        if tod > 1:
            tod -= 1
            print(f"Nyt vieraslaji peittää {1 - 1/tod} % niitystä.")
    elif x == "tutki":
        print("Etsit niityltä kukkaa.")
        x = random.randint(1,tod)
        if x == 1:
            visuaalit.loyto_visuaali()
            input("Löysit kukan!")
            inv.append("Kukka")
        else:
            print("Et löytänyt kukkaa. Koska et auttanut tutkijoita, vieraslaji leviää niityllä.")
            input("Kitkemällä vieraslajia parannat kukan kasvumahdollisuuksia.")
            tod += 1
    input("")
    return tod

    
def etsi_alue4(inv):
    print("Tiesi haarautuu kahteen suuntaan:")
    print("punaiseksi maalattuun maatilarakennukseen ja vesivoimalla toimivaan myllyyn.")

    x = input("Mihin menet? (maatila, mylly): ").lower()
    while x != "maatila" and x != "mylly":
        x = input("Mihin menet? (maatila, mylly): ").lower()

    if x == "maatila":
        print("Tutkit maatilaa ja sen rakennuksia.")
        print("Löydät maatilan takaa pensaan, josta löytyy punaisen kuultavia marjoja.")
        visuaalit.loyto_visuaali()
        print("Löysit marjat.")
        inv.append("Marjat")
    elif x == "mylly":
        print("Myllyssä on vesivoimalla toimiva mehustin.")
        if inv.count("Marjat") >= 2:
            print("Asetat marjat mehustimeen ja käännät sen vipua.")
            visuaalit.loyto_visuaali()
            print("Löysit mehua!")
            inv.remove("Marjat")
            inv.remove("Marjat")
            inv.append("Mehu")

