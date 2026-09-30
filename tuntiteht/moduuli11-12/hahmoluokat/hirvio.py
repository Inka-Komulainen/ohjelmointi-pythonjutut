from .hahmot import Hahmo

class Hirvio(Hahmo):
    def __init__(self, nimi, repliikki):
        self.repliikki = repliikki
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Repliikki: {self.repliikki}")