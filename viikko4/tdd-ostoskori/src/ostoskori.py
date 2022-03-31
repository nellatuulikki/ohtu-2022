from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        pass
      # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostoskori = []

    def tavaroita_korissa(self):
        tavaroita = 0
        for ostos in self.ostoskori:
            tavaroita += ostos.lukumaara
        
        return tavaroita
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        yhteishinta = 0
        for ostos in self.ostoskori:
            yhteishinta += ostos.hinta
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

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
        # tyhjentää ostoskorin

    def ostokset(self):
        if self.ostoskori == []:
            print('ostoskori on tyhjä')
            pass

        for ostos in self.ostoskori:
            print(f"{ostos.tuotteen_nimi()} {ostos.lukumaara()} kappaletta")
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
