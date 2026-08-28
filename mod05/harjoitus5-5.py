# harjoitus 5 -- ohjelma kysyy käyttäjätunnusta ja salasanaa, kunnes molemmat on oikein.
# Jos väärät tiedot annetaan viidesti

i = 1
sKayttaja = input("Käyttäjätunnus: ")
sSalasana = input("Salasana: ")

while sKayttaja != "python" or sSalasana != "rules":
    if i >= 5: # lähtee while loopista jos viides yritys on väärin
        print("Pääsy evätty.")
        break

    sKayttaja = input("Käyttäjätunnus: ")
    sSalasana = input("Salasana: ")

    i +=1
else:
    print("Tervetuloa!")