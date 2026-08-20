# kirjoita joka kertoo syötetyn päivä lkm sekunteina
paiva = input("Kuinka monta päivää: ")
iPaiva = int(paiva)
sekunti = iPaiva * 24 * 60 * 60

print("Annettu määrä päiviä sekunteina: " + str(sekunti))