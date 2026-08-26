# harjoitus 4 -- ohjelma kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. 
# Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia 
# vain jos ne ovat jaollisia myös neljälläsadalla.

iVuosi = int(input("Kerro vuosiluku: "))

if iVuosi % 100 == 0:
    if iVuosi % 4 == 0 and iVuosi % 400 == 0:
        print(f"{iVuosi} on karkausvuosi.")
    else:
        print(f"{iVuosi} ei ole karkausvuosi.")
else:
    if iVuosi % 4 == 0:
        print(f"{iVuosi} on karkausvuosi.") 
    else:
        print(f"{iVuosi} ei ole karkausvuosi.")        