# harjoitus 1 -- kysyy kuukauden luvun ja tulostaa sen mukaisen vuodenajan. 

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

kuukausi = int(input("Kerro monesko kuukausi: "))

print(f"Kuukauden vuodenaika on {vuodenajat[kuukausi-1]}.")