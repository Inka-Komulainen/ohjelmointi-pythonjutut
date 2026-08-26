# harjoitus 2 - ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen.

#LUX on parvekkeellinen hytti yläkannella.
#A on ikkunallinen hytti autokannen yläpuolella.
#B on ikkunaton hytti autokannen yläpuolella.
#C on ikkunaton hytti autokannen alapuolella.

sHytti = input("Kerro hyttisi luokka (LUX, A, B, C): ")
sHytti = sHytti.upper()

if sHytti == "LUX":
    print("Hyttisi on autokannen yllä ja siinä on parveke.")
elif sHytti == "A":
    print("Hyttisi on autokannen yllä, ja siinä on ikkuna.")
elif sHytti == "B":
    print("Hyttisi on autokannen yllä, ja siinä ei ole ikkunaa.")
elif sHytti == "C":
    print("Hyttisi on autokannen alla.")
else:
    print("Virheellinen hyttiluokka")