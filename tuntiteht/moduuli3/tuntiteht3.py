#harjoitus 3 - esittää grammoina kysytyn luvun kilogrammoina grammoina

luku = float(input("Kerro monta grammoina: "))
kilo = luku / 1000
gramma = luku % 1000

print(f"Määrä kiloina ja grammoina: {kilo:.0f} kg {gramma:.0f} g")