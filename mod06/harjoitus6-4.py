# harjoitus 4 -- kysyy 5 kaupungin nimen, tallentaa ne listaan ja tulostaa ne syöttöjärjestyksessä

kaupunkilista = []

for i in range(1,6):
    kaupunkilista.append(input(f"Anna #{i} kaupunki: "))

for kaupunki in kaupunkilista:
    print(kaupunki)