# ohjelma kysyy pelaajan nimen ja iän

sPelaajaNimi = input("Mikä on nimesi: ")
iPelaajaIka = int(input("Kuinka vanha olet: "))
sToiminto = ""

print(f"Nimesi on {sPelaajaNimi} ja ikäsi on {iPelaajaIka}.\n")

if (iPelaajaIka >= 12):
    while sToiminto != "lopeta":
        print(f"Tervetuloa päävalikkoon, {sPelaajaNimi}!")
        print("\nAloita\nProfiili\nEtsi\nLöydöt (inventaario)\nLopeta\n")

        sToiminto = input("Mitä haluat tehdä: ").lower()
        if sToiminto == "profiili":
            print(f"Nimesi on {sPelaajaNimi} ja ikäsi on {iPelaajaIka}.\n")
        elif sToiminto == "etsi":
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

