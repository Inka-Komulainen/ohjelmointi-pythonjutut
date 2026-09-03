# harjoitus 3 -- kysyy kokonaisluvun, ja kertoo onko luku alkuluku

luku = int(input("Anna luku: "))

if luku > 2: # lukua 2 suuremmat luvut voivat olla alkulukuja
    for i in range(2,luku + 1):
        if i == luku:
            print(f"{luku} on alkuluku.")
        elif luku % i == 0:
            print(f"{luku} ei ole alkuluku.")
            break
elif luku == 1 or luku == 2: #luvut 1 ja 2 ovat alkulukuja
    print(f"{luku} on alkuluku.")
else: # 0 ja negatiiviset luvut eivät ole alkulukuja
    print(f"{luku} ei ole alkuluku.")