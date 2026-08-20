#harjoitus 2 - ohjelma tulostaa ympyrän pinta-alan, jos sille syöttää ympyrän säteen
import math

sade = input("Anna ympyrän säde: ")
fSade = float(sade) # muuntaa float muotoon
ala = math.pi * fSade**2

print("Ympyrän pinta-ala on: " + str(ala))