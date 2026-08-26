# pieni tarina, johon käyttäjän valinta muuttaa jotakin

sNimi = input("Mikä on nimesi: ")
sSieni = "1"

print(f"{sNimi} otti reppunsa ja lähti metsään. Metsässä hän löysi punaisen ja valkoisen sienen.")

while sSieni != "punainen" or sSieni != "valkoinen":
    sSieni = input(f"Kumman sienen {sNimi} ottaa? (vastaa punainen tai valkoinen): ")
    

if sSieni == "punainen":
    print(f"Koskettaessaan punaista sientä {sNimi} halvaantuu kauttaaltaan.")
elif sSieni == "valkoinen":
    print(f"Valkoinen sieni tuntuu pehmeältä ja kostealta kädessä.")
