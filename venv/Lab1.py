import sys


def zad():
    print('Wprowadzenie')
    lista = [1, 2, 3, 4, 2]
    print(lista)
    lista.sort()
    print(lista)
    znaki = 'abcd'
    print(znaki[0])

    slownik = {'a': 1, 'b': 2, 'c': 3}
    print(slownik)
    print(slownik['a'])
    slownik.pop('c')
    print(slownik)
    print(slownik.keys())
    print(slownik.values())

    liczba = input('Wprowadz liczbe: ')
    print(liczba + ' to wczytana wartosc')

    sys.stdout.write('Wprowadz liczbe: ')
    liczba = sys.stdin.readline()
    print(type(liczba))
    liczba = int(liczba)
    print(type(liczba))

    a = int(input('Podaj liczbe a: '))
    b = int(input('Podaj liczbe b: '))

    if a == b:
        print(a+b)
    else:
        print('Liczby nierówne')

    # If lewa_strona) & (prawa_strona):
    #   komenda
    # else:
    #   komenda


def zad1():
    a = int(input('Podaj liczbe:'))
    b = int(input('Podaj liczbe:'))
    c = int(input('Podaj liczbe:'))
    d = int(input('Podaj liczbe:'))

    if (a > b) & (c > d):
        print(a+c)
    else:
        print(b+d)


def zad2():
    lista = [1, 2, 3, 4, 5]
    for i in range(0, 6, 1):
        print(i)

    for item in lista:
        print(item)
    else:
        print('')
        print(len(lista))

    licznik = 0
    while licznik < len(lista):
        if lista[licznik] == 4:
            break
        else:
            print('')
            print(lista[licznik])
            licznik += 1
    else:
        print('Koniec listy')


def zad3():
    lista = [2, 8, 12, 7, 4, 36]
    liczba = int(input('Podaj liczbe: '))

    if liczba ** 2 in lista:
        print('Znaleziono liczbe')

    print('Zwracac uwagę na ta zaleznosc w potegach:')
    print(6**2)
    print(6**1/2)
    print(6**(1/2))
    print(pow(6, 2))

def zadanie1():
    def licz_slowa(zdanie):
        ile_slow = len(zdanie.split())
        return ile_slow

    zdanie = str(input('Napisz swoje zdanie: '))
    print(f'Zdanie: {zdanie}')
    print(f'Zdanie: {licz_slowa(zdanie)}')



def zadanie2():
    sys.stdout.write('Wprowadz pierwszą liczbe: ')
    a = sys.stdin.readline()
    a = int(a)
    sys.stdout.write('Wprowadz drugą liczbe: ')
    b = sys.stdin.readline()
    b = int(b)
    sys.stdout.write('Wprowadz trzecią liczbe: ')
    c = sys.stdin.readline()
    c = int(c)
    d = (a ** b) + c
    print(f'Wynik to {d}')


def zadanie3():
    print('Sposób pierwszy: ')
    napis = str(input('Podaj napis: '))
    if napis == napis[::-1]:
        print('Jest to palindrom')
    else:
        print('To nie jest palindrom')

    print('Sposób drugi: ')
def zadanie4():
    liczba = int(input('Podaj liczbe: '))

    if liczba > 1:
        for i in range(2, int(liczba/2)+1):
            if (liczba % i) == 0:
                print(f'{liczba} nie jest liczba pierwsza')
                break
            else:
                print(f'{liczba} jest liczba pierwszą')
                break
    else:
        print(f'{liczba} nie jest liczba pierwsza')


def zadanie5():
    def czy_liczba(liczba):
        suma_dzielnikow = sum([dzielnik for dzielnik in range(1, liczba) if liczba % dzielnik == 0])
        return suma_dzielnikow == liczba

    ilosc = sum(1 for liczba in range(2, 1001) if czy_liczba(liczba))
    print(f'Ilosc liczb doskonalych do 100 to: {ilosc}')











def main():
    # zad()
    # zad1()
    # zad2()
    # zad3()
    # zadanie1()
    # zadanie2()
    # zadanie3()
    # zadanie4()
    zadanie5()


if __name__ == '__main__':
    main()