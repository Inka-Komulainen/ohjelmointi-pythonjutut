#etene funktio - pääsee seuraavalle alueelle tämän kautta, jos täyttää alueen lähtöehdon.

class Alue: 
    alueet = [] # tekemättömät alueet
    def __init__(self, nimi, kuvaus, lahtoehto): # +esineet?
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.lahtoehto = lahtoehto
        Alue.alueet.append(self.nimi)

# tarkistaa että pelaaja on kerännyt tarvittavat esineet seuraavalle alueelle etenemiseen
    def kutsu_etene(self,inv,sij): 

        poistot = 0
        for i in self.lahtoehto: #tarkistaa, onko pyydetyt esineet listassa ja poistaa ne
            for j in inv:
                if i == j:
                    inv.remove(i)
                    poistot += 1
                    break

        if len(self.lahtoehto) == poistot: # tarkistaa, että poistettu määrä esineitä on sama kuin pyydettyjen esineiden määrä
            self.alueet.remove(sij)
            sij = ""
            print("Annat pyydetyt esineet, ja voit jatkaa seuraavalle alueelle.")
            return True, sij
        else:
            print("Ei ollut tarpeeksi tarvikkeita.")
            input("Kaikki tällä alueella keräämäsi esineet katoavat inventaariostasi!")
            return False, sij