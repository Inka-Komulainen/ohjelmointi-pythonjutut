# harjoitus 3 -- ohjelma kysyy lukumäärä gallonoina, ja muuntaa sen funktiossa litroiksi

def muunna_litroiksi(luku):
    i = luku * 3.785
    return i

gallona = float(input("Montako gallonaa: "))

while gallona >= 0:
    litra = muunna_litroiksi(gallona)
    print(f"Se on litroina {litra}.")

    gallona = float(input("Montako gallonaa: "))