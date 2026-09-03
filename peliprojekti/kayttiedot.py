# ohjelma kysyy pelaajan nimen ja iän

sPelaajaNimi = input("Mikä on nimesi: ")
iPelaajaIka = int(input("Kuinka vanha olet: "))
sToiminto = ""

print(f"Nimesi on {sPelaajaNimi} ja ikäsi on {iPelaajaIka}.\n")

# päävalikko alkaa tästä

if (iPelaajaIka >= 12): # ei anna alle 12-vuotiasta päästä päävalikkoon
    while sToiminto != "lopeta":
        print(f"Tervetuloa päävalikkoon, {sPelaajaNimi}!")
        print("\nEtene\nProfiili\nEtsi\nLöydöt (inventaario)\nLopeta\n")

        sToiminto = input("Mitä haluat tehdä: ").lower()
        if sToiminto == "profiili": # päävalikon toiminto "profiili" kertoo pelaajan tiedot
            print(f"Nimesi on {sPelaajaNimi} ja ikäsi on {iPelaajaIka}.\n")
        elif sToiminto == "etsi": #päävalikon toiminto "etsi" avulla pelaaja löytää uusia asioita, tulee muuttumaan tulevaisuudessa 
            print("\nLähdet etsimään...")
            sSuunta = input("Mihin suuntaan lähdet etsimään? (vasemmalle, oikealle, suoraan): ").lower()
            if sSuunta == "vasemmalle":
                print("Löysit sienen!")
            elif sSuunta == "oikealle":
                print("Löysit kepin!")
            elif sSuunta == "suoraan":
                print("Löysit valtavan kiven!")
            print("Palaat takaisin alkuun.\n")       
else:
    print("Et taida olla vielä tarpeeksi vanha.")

