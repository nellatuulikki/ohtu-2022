import unittest
from int_joukko import IntJoukko


def main():
    joukko = IntJoukko()

    print(joukko)
    joukko.lisaa(1)
    print(joukko.lukujono)
    joukko.lisaa(2)
    joukko.lisaa(3)
    joukko.lisaa(2)
    joukko.lisaa(10)
    joukko.lisaa(5)
    joukko.lisaa(6)
    print(joukko.lukujono)
    joukko.poista(3)
    print(joukko.lukujono)

    print(joukko.to_int_list())
    print(joukko)


if __name__ == "__main__":
    main()
