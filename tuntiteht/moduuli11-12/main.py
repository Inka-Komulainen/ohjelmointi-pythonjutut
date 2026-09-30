
from hahmoluokat import Pelaajahahmo
from hahmoluokat import Hirvio


merihirvio = Hirvio("Merihirviö", "Lits läts, aion syödä sinut!")
p_hahmo = Pelaajahahmo(input("Anna hahmon nimi: "))

print("Peli alkaa.")
p_hahmo.tulosta_tiedot()
input()

print(f"{p_hahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön. Hirviö huutaa:")
print(merihirvio.repliikki)
merihirvio.tulosta_tiedot()

input()
p_hahmo.taistelu(merihirvio)
input()
print(f"Peli ohi.")