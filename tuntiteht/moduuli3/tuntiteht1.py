#input eli syöte
#merkkijono eli string eli  "..." tai '...'

#int eli kokonaisluku, float eli desimaali, complex eli kompleksiluku, boolean true/false
#lista eli list, tuple eli monikko, sanakirja eli dictionary

#kirjoita tarina johon lisätään useampi muuttuja
nimi = input("tarinan päähenkilön nimi: ")
adjektiivi = input("kerro jokin tunne: ")
juhlapaiva = input("minä juhlapäivänä tarina tapahtuu: ")

print("Olipa kerran", nimi, ", joka etsi koiraansa. Hän etsi ja etsi kunnes löysi sen", juhlapaiva, ".")
print(nimi + " oli hyvin " + adjektiivi + ".")