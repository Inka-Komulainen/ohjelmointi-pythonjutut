# harjoitus 3 -- ohjelma kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää
# tyhjän merkkijonon lopetusmerkiksi. Tulostaa syötetyistä luvuista pienimmän ja suurimman.

sLuku = input("Anna luku: ")
iMin = int(sLuku)
iMax = int(sLuku)

while sLuku != "":
   
    if int(sLuku) < iMin: # antaa uuden minimin
        iMin = int(sLuku)
    elif int(sLuku) > iMax: # antaa uuden maksimin
        iMax = int(sLuku)

    sLuku = input("Anna luku: ")
    
print(f"Maksimi on {iMax}.")
print(f"Minimi on {iMin}.")