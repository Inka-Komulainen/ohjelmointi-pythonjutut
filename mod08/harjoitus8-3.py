# harjoitus 3 -- ohjelma hakee ja tallentaa lentoasematietoja. Käyttäjä voi syöttää uuden lentoaseman,
# hakea syötetyn lentoaseman ja lopettaa ohjelman.

asematiedot = dict()

komento = "lisää"

while komento != "lopeta":
    if komento == "lisää":
        nimi = input("Anna lentoaseman nimi: ")
        koodi = input("Anna aseman ICAO-koodi: ")
        asematiedot[koodi] = nimi
    elif komento == "hae":
        koodi = input("Anna aseman ICAO-koodi: ")
        print(asematiedot[koodi])
        
        
    komento = input("Mitä haluat tehdä? (hae, lisää, lopeta): ")
    

