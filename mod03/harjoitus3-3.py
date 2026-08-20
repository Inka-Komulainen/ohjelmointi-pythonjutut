#harjoitus 3 - kysyy suorakulmion kannan ja korkeuden, tulostaa piirin ja pinta-alan

kanta = float(input("Kerro suorakulmion kannan pituus: "))
korkeus = float(input("Kerro suorakulmion korkeus: "))


piiri = 2 * kanta + 2 * korkeus
ala = kanta * korkeus

print(f"Suorakulmion pinta-ala on {ala}, ja piiri on {piiri}.")