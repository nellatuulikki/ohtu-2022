KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteettia ei annettu oikeassa muodossa")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kasvatuskokoa ei annettu oikeassa muodossa")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lukumäärä = 0

    def kuuluu(self, luku):
        if luku in self.lukujono:
            return True
        else:
            return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lukujono[self.alkioiden_lukumäärä] = luku
            self.alkioiden_lukumäärä += 1

        if self.alkioiden_lukumäärä == len(self.lukujono) :
            self.lukujono += self.kasvatuskoko * [0]

    def poista(self, luku):

        if self.kuuluu(luku):
            self.lukujono.remove(luku)
            self.lukujono.append(0)
            self.alkioiden_lukumäärä -= 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumäärä

    def to_int_list(self):
        return self.lukujono[0:self.alkioiden_lukumäärä]

    @staticmethod
    def yhdiste(taulukko_a, taulukko_b):
        yhdistetty_lista = IntJoukko()

        for alkio in taulukko_a.to_int_list() + taulukko_b.to_int_list():
            yhdistetty_lista.lisaa(alkio)

        return yhdistetty_lista

    @staticmethod
    def leikkaus(taulukko_a, taulukko_b):
        leikattu_lista = IntJoukko()

        for alkio in taulukko_a.to_int_list():
            if alkio in taulukko_b.to_int_list():
                leikattu_lista.lisaa(alkio)

        return leikattu_lista

    @staticmethod
    def erotus(taulukko_a, taulukko_b):
        erotettu_lista = IntJoukko()

        for alkio in taulukko_a.to_int_list():
            if alkio not in taulukko_b.to_int_list():
                erotettu_lista.lisaa(alkio)

        return erotettu_lista

    def __str__(self):
        merkkijono = ', '.join(str(x) for x in self.lukujono if x != 0)
        return "{" + merkkijono + "}"
