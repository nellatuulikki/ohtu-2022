import unittest
from int_joukko import IntJoukko

def main():
    joukko = IntJoukko()
    joukko2 = IntJoukko()

    joukko.lisaa(1)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko2.lisaa(1)
    joukko2.lisaa(5)
    print(joukko.erotus(joukko, joukko2))
    testi = joukko.erotus(joukko, joukko2)

    print(testi.to_int_list())
    print(joukko)

if __name__ == "__main__":
    main()
