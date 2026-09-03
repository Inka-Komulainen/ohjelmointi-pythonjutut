# harjoitus 6 -- ohjelma kysyy kahden pitsan halkaisijan ja hinnan, funktio vertailee kummalla on suurempi €/m^2

import math

def laske_yh(d, eur):
    #ympyrän pinta-ala on A = (pi * d^2)/4, jolloin yksikköhinta on yh = eur * 4 / pi * d^2
    yh = eur * 4 /(math.pi * (d * 0.01)**2)  # 0.01 on yksikkömuunnos cm --> m
    return yh
                                                                
# pääohjelma alkaa tästä 
    
halkaisija = float(input("Ensimmäisen pitsan halkaisija (cm): "))
hinta = float(input("Ensimmäisen pitsan hinta: "))

yksikko_hinta1 = laske_yh(halkaisija, hinta)

halkaisija = float(input("Toisen pitsan halkaisija (cm): "))
hinta = float(input("Toisen pitsan hinta: "))

yksikko_hinta2 = laske_yh(halkaisija, hinta)

print(f"Ensimmäinen pitsa on {yksikko_hinta1:.2f} €/m^2, ja toinen pitsa on {yksikko_hinta2:.2f} €/m^2.")

if yksikko_hinta1 < yksikko_hinta2: # vertailee kumpi pitsa on halvempi
    voittaja = 1
elif yksikko_hinta1 > yksikko_hinta2:
    voittaja = 2
else:
    voittaja = "Pitsat ovat yhtä halpoja."

if voittaja == 1 or voittaja ==2:
    print(f"Pitsalla {voittaja} saa enemmän pitsaa samalla hinnalla.")
else:
    print(voittaja)