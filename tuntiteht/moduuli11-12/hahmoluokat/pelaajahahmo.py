from .hahmot import Hahmo

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, tavaralista = ["miekka","kilpi"]):
        self.tavaralista = tavaralista
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tavaraluettelo: {self.tavaralista.copy()}")
    