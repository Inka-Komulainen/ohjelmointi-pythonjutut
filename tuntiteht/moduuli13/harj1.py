
with open("ostoslista.txt","w") as tiedosto:
    tiedosto.write("maito\nleipä\nkananmunat")

with open("ostoslista.txt", "a") as tiedosto:
    tiedosto.write("\nneljäs")