#harjoitus 4 - ohjelma kysyy kolme kokonaislukua, ja tulostaa lukujen summan, tulon ja keskiarvon

luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo}")