from tuote import Tuote
from ostoskori import Ostoskori

def main():

    maito = Tuote('maito',3)
    leipä = Tuote('leipä',2)

    ostoskori = Ostoskori()
    ostoskori.lisaa_tuote(maito)
    ostoskori.lisaa_tuote(leipä)
    ostoskori.lisaa_tuote(leipä)
    ostoskori.ostokset()

    ostoskori.poista_tuote(leipä)
    ostoskori.ostokset()
    
    ostoskori.tyhjenna()
    ostoskori.ostokset()

if __name__ == "__main__":
    main()

