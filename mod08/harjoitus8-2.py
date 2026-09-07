# harjoitus 2 -- kysyy käyttäjältä nimia, kunnes käyttäjä painaa enteriä. Kertoo, onko syötetty nimi uusi vai
# onko se jo syötetty. Lopuksi tulostaa kaikki nimet mielivaltaisessa järjestyksessä.

nimet = set()
nimi = input("Kerro nimi: ")
nimet.add(nimi)

while nimi != "":
    nimi = input("Kerro nimi: ")
    if nimi in nimet:
        print("Aiemmin syötetty nimi.")
    else:
        nimet.add(nimi)
        print("Uusi nimi.")

for i in nimet:
    print(i)
