# harjoitus 3 -- ohjelma kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Tulostaa syötetyistä luvuista pienimmän ja suurimman.

# ensimmäinen versio harjoituksen 3 koodista, jonka sain toimimaan, mutta halusin tiivistää

iLuku = int(input("Anna luku: "))
iMin = iLuku
iMax = iLuku

while str(iLuku) != "":
    sLuku = input("Anna luku: ")

    if sLuku != "":
        iLuku = int(sLuku)
        if iLuku < iMin: # antaa uuden minimin
            iMin = iLuku
        elif iLuku > iMax: # antaa uuden maksimin
            iMax = iLuku
    else:
        break
    
        

print(f"Maksimi on {iMax}.")
print(f"Minimi on {iMin}.")