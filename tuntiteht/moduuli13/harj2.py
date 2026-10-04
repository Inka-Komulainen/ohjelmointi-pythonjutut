
with open("ostoslista.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)

with open("ostoslista.txt","r") as tiedosto:
    data = tiedosto.readlines()
    print(f"Tuotteita listassa: {len(data)}")