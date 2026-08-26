# harjoitus 3 -- ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l). 
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

iHemoglobiini = int(input("Kerro hemoglobiiniarvosi (g/l): "))
iSukupuoli = input("Mikä on biologinen sukupuolesi (nainen/mies): ")
iSukupuoli = iSukupuoli.lower()

if iSukupuoli == "nainen":
    if iHemoglobiini < 117:
        print("Arvosi on alhainen.")
    elif iHemoglobiini >= 117 and iHemoglobiini <= 175:
        print("Arvosi on normaali.")
    else:
        print("Arvosi on korkea.")
elif iSukupuoli == "mies":
    if iHemoglobiini < 134:
        print("Arvosi on alhainen.")
    elif iHemoglobiini >= 134 and iHemoglobiini <= 195:
        print("Arvosi on normaali.")
    else:
        print("Arvosi on korkea.")
