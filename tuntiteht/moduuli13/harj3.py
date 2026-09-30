

while True:
    try:
        nimi = input("Kerro tiedoston nimi: ")
        with open(nimi, "r") as tiedosto:
            data = tiedosto.read()
            print(data)
            break
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")