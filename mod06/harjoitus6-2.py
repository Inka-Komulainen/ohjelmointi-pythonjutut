# harjoitus 2 -- kysyy käyttäjältä lukuja kunnes hän painaa enter, tulostaa 5 suurinta lukua

luvut = []

luku = input("Anna luku: ") 
while luku != "": # kysyy lukuja kunnes painaa enter
    luvut.append(int(luku))
    luku = input("Anna luku: ")

luvut.sort(reverse=True) #järjestää luvut suurimmasta pienimpään
print(luvut[0:4]) #tulostaa viisi ensimmäistä