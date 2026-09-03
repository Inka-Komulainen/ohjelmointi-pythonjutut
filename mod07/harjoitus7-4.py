# harjoitus 4 -- funktio laskee taulukon lukujen summan, jonka pääohjelma tulostaa

def laske_summa(lista):
    sum = 0
    for i in lista:
        sum += i
    return sum

lukulista = [1, 2, 3, 4, 5]
print(lukulista)

summa = laske_summa(lukulista)

print("Summa:", end=" ")
print(summa)