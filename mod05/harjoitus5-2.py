# harjoitus 2 -- ohjelma muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän

fTuuma = 0

while fTuuma >= 0:
    fTuuma = float(input("Anna positiivinen luku tuumina: "))

    fSentti = fTuuma * 2.54
    print(f"Se on sentteina: {fSentti}.")

print("Ei ollut positiivinen.")
