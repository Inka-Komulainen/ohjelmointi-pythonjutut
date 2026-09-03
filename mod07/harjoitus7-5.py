# harjoitus 5 -- funktio poistaa listasta parittomat luvut, pääohjelma tulostaa uuden listan

def poista_parittomat(lista):
    uusi_lista = []
    for i in lista:
        if i % 2 == 0:
            uusi_lista.append(i)

    return uusi_lista

lukulista = [1, 2, 3, 4, 5]
print(lukulista)

lukulista = poista_parittomat(lukulista)

print("Uusi lista:", end=" ")
print(lukulista)