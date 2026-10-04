#etene funktio - pääsee seuraavalle alueelle tämän kautta, jos täyttää alueen lähtöehdon.
from pelaaja_luokka import Pelaaja


class Alue: 
    alueet = []
    tehdyt_alueet = 0
    def __init__(self, nimi, kuvaus, lahtoehto): # +esineet?
        self.nimi = nimi
        self.kuvaus = kuvaus
        self.lahtoehto = lahtoehto
        Alue.alueet.append(self.nimi)

    def kutsu_etene(self,inv,pel): 
        print(self.kuvaus)

        poistot = 0
        for i in self.lahtoehto: #tarkistaa, onko pyydetyt esineet listassa ja poistaa ne
            for j in inv:
                if i == j:
                    inv.remove(i)
                    poistot += 1
                    break

        if len(self.lahtoehto) == poistot: # tarkistaa, että
            self.tehdyt_alueet += 1
            self.alueet.remove(pel)
            print("Annat pyydetyt esineet, ja voit jatkaa seuraavalle alueelle.")
            return True
        else:
            print("Ei ollut tarpeeksi tarvikkeita. Pakenet ennen kuin rölli ottaa sinut suihinsa.")
            return False