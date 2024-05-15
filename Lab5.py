import numpy as np


def wprowadzenie():
    print('Lab 5')
    # Inicjalizowanie tablicy
    a = np.array([0, 1])
    print(a)
    # Drugi sposob
    p = np.arange(2)
    print(p)
    # Wypisanie typu zmiennej tablicy
    print(type(a))
    # Sprawdzenie typu danych tablicy
    print(a.dtype)
    # Inicjowanie tablicy z konkretnym typem danych
    k = np.arange(2, dtype='int64')
    print(k.dtype)
    # Zapisywanie kopii tsblicy jako tablicy z innym typem
    b = a.astype('float')
    print(b)
    print(b.dtype)
    # Wypisywanie rozmiaru tablicy
    print(b.shape)
    # Ilość wymiaró tablicy
    print(a.ndim)
    # Tworzenie tablicy wielowymiarowej
    m = np.array([np.arange(2), np.arange(2)])
    print(m.shape)
    print(type(m))


def macierze():
    # Macierz wypelniona zerami
    zera = np.zeros((5, 5))
    print(zera)
    print(zera.dtype)
    # Macierz wypelniona jedynkami
    jedynki = np.ones((4, 4))
    print(jedynki)
    print(jedynki.dtype)
    # Macierz z wartosciami losowymi
    pusta = np.empty((2, 2))
    print(pusta)
    # Odwolanie do elementow tablicy


def zad1():
    print('Zadanie 1')
    a = np.arange(3, 3 * 15 + 1, 3)
    print(a)


def zad2():
    print('Zadanie 2')
    lista = [1.2, 2.1, 5.2, 2.5, 1.5, 5.1]
    tablica = np.array(lista)
    tablica_int = tablica.astype(np.int64)
    print(tablica)
    print(tablica_int)


def zad3():
    n = int(input('Podaj liczbe całkowitą: '))
    tablica = np.arange(1, n * n + 1).reshape(n, n)
    print(tablica)


def zad4():
    def generuj(n, m):
        tablica = np.logspace(1, m, num=m, base=n, dtype=int)
        return tablica
    a = int(input('Podaj pierwszą liczbę: '))
    b = int(input('Podaj drugą liczbę: '))
    print(generuj(a, b))


def zad5():

    def wektor(dlugosc):
        odwrocony = np.arange(dlugosc, 0, -1)
        macierz = np.diag(odwrocony)
        return macierz

    x = int(input('Podaj dlugosc wektora: '))
    print('Macierz digonalna: ')
    print(wektor(x))


def zad6():
    def wykreslanka(slowo):
        dlugosc = max(len(word) for word in slowo)
        macierz = np.zeros((dlugosc, dlugosc), dtype='U1')

        for i, char in enumerate(slowo[0]):
            macierz[i, 0] = char
        for j, char in enumerate(reversed(slowo[1])):
            macierz[0, j+1] = char
        for i in range(len(slowo[2])):
            macierz[i+2, i+1] = slowo[2][i]
        return macierz

    slowa = ['KOLUMNA', 'WIERSZ', 'UKOS']
    krzyzowka = wykreslanka(slowa)
    print("Macierz wykreślanki:")
    for row in krzyzowka:
        print(row)


def zad7():
    def generuj_macierz(n):
        macierz = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    macierz[i][j] = 2
                else:
                    macierz[i][j] = 2 * (abs(i - j) + 1)
        return macierz

    n = int(input('Podaj liczbę: '))
    macierze = generuj_macierz(n)
    for i in macierze:
        print(i)


def zad8():








def zad9():
    print('Zadanie 9')

    def fiboacci(n):
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

    wymair = 5 * 5
    wartosci = fiboacci(wymair)

    macierz = np.array(wartosci).reshape(5, 5)

    print("Macierz 5x5 zawierająca kolejne wartości ciągu Fibonacciego:")
    print(macierz)



def main():
    # wprowadzenie()
    # macierze()
    # zad1()
    # zad2()
    # zad3()
    # zad4()
    # zad5()
    # zad6()
    # zad7()
    zad8()
    # zad9()


if __name__ == '__main__':
    main()
