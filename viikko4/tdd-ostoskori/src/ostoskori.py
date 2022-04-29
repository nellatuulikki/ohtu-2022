from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self.ostoskori:
            tavaroita += ostos.lukumaara()
        
        return tavaroita

    def hinta(self):
        yhteishinta = 0
        for ostos in self.ostoskori:
            yhteishinta += ostos.hinta()
        return yhteishinta

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostoskori:
            if lisattava.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                return 

        self.ostoskori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if poistettava.nimi() == ostos.tuotteen_nimi():
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)
                else:
                    self.ostoskori.remove(ostos)


    def tyhjenna(self):
        self.ostoskori.clear()

    def ostokset(self):
        ostokset = []
        if self.ostoskori == []:
            pass
        else:
            ostokset = []

            for ostos in self.ostoskori:
                if ostos.lukumaara() > 0:
                    ostokset.append(f"{ostos.tuotteen_nimi()} {ostos.lukumaara()} kappaletta")

        return ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
