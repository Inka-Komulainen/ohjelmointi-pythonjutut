# harjoitus 3 -- ohjelma hakee ja tallentaa lentoasematietoja. Käyttäjä voi syöttää uuden lentoaseman,
# hakea syötetyn lentoaseman ja lopettaa ohjelman.

asematiedot = dict()

komento = "lisää"

while komento != "lopeta":
    if komento == "lisää":
        nimi = input("Anna lentoaseman nimi: ")
        koodi = input("Anna aseman ICAO-koodi: ")
        asematiedot[nimi] = koodi
    elif komento == "hae":
        hae_koodi = input("Anna aseman ICAO-koodi: ")
        for nimi, koodi in asematiedot.items():
            if koodi == hae_koodi:
                print(nimi)
        
    komento = input("Mitä haluat tehdä? (hae, lisää, lopeta): ")
    

