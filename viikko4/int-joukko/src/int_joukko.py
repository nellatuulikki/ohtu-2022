KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")  # heitin vaan jotain :D
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("kapasiteetti2")  # heitin vaan jotain :D
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lukumäärä = 0

    def kuuluu(self, luku):
        if luku in self.lukujono:
            return True
        else:
            return False

    def lisaa(self, n):
        ei_ole = 0

        if self.alkioiden_lukumäärä == 0:
            self.lukujono[0] = n
            self.alkioiden_lukumäärä += 1
            return True
            
        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lukumäärä] = n
            self.alkioiden_lukumäärä += 1

            if self.alkioiden_lukumäärä % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lukumäärä + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0


        for i in range(0, self.alkioiden_lukumäärä):
            if n == self.lukujono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[kohta] = 0
                break

        #if 

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lukumäärä - 1):
                apu = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apu

            self.alkioiden_lukumäärä = self.alkioiden_lukumäärä - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lukumäärä

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lukumäärä

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        merkkijono = "{"
        for alkio in range(0, self.alkioiden_lukumäärä):
            if alkio == self.alkioiden_lukumäärä - 1:
                merkkijono += f" {self.lukujono[alkio]}"
            elif alkio == 0:
                merkkijono += f"{self.lukujono[alkio]},"
            else:
                merkkijono += f" {self.lukujono[alkio]},"
        merkkijono += "}"
        return merkkijono
