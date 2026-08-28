#luo laskin, joka tekee kahden luvun välisiä yhteen-, erotus- ja kertolaskuja.
#laskin kysyy uutta laskua, kunnes käyttäjä haluaa lopettaa

sToiminto = input("Valitse laskimen toiminto (+, -, *, lopeta): ")

while sToiminto != "lopeta":
    
    iLuku1 = int(input("Anna luku: "))
    iLuku2 = int(input("Anna toinen luku: "))

    if sToiminto == "+":
        print(f"{iLuku1} + {iLuku2} = {iLuku1 + iLuku2}")
    elif sToiminto == "-":
        print(f"{iLuku1} - {iLuku2} = {iLuku1 - iLuku2}")
    elif sToiminto == "*":
        print(f"{iLuku1} * {iLuku2} = {iLuku1 * iLuku2}")

    sToiminto = input("Valitse laskimen toiminto (+, -, *, lopeta): ")
