# harjoitus 1 -- funtio, joka heittää noppaa. pääohjelma heittää noppaa kunnes saadan 6

import random

def heita_noppaa():
    i = random.randint(1,6)
    return i

luku = 0
while luku != 6:
    luku = heita_noppaa()
    print(luku)