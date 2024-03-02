import sys

'''
Zadania 
Zad 1. Napisz skrypt, który pobiera od użytkownika zdanie i liczy ilość słów. Użyj funkcji input 
Zad 2. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c. 
Użyj funkcji readline() i write()). 
Zad3. Napisz skrypt, który sprawdzi czy wczytany napis jest palindromem. 
Zad4. Napisz skrypt, który sprawdzi czy wczytana liczba jest pierwsza. 
Zad5. Napisz skrypt, który sprawdzi ile jest liczb doskonałych do liczby 1000. 
Zad 6. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą użycia pętli 
for podnieś każdą liczbę do kwadratu. 
Zad 7. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby. 
Zad 8. Napisz skrypt, w którym utworzysz listę z elementami dowolnego typu. Utwórz słownik, gdzie klucze będą
poszczególnymi elementami z listy, a wartość to ilość wystąpień klucza w liście. Następnie usuń wszystkie elementy
ze słownika, które nie będą liczbami. 
'''
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
    napis = napis.lower()
    if napis == napis[::-1]:
        print('Jest to palindrom')
    else:
        print('To nie jest palindrom')

    print('Sposób drugi: ')
    dlugosc = len(napis)
    for i in range(dlugosc // 2):
        if napis[i] != napis[dlugosc - i - 1]:
            print('To nie jest palindrom')
            break
        else:
            print('Jest to palindrom')
            break

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


def zadanie6():
    lista = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]

    for i in range(len(lista)):
        lista[i] = lista[i] ** 2
    print(f'Lista po podniesieniu do kwadratu: {lista}')


def zadanie7():
    parzyste_liczby = []
    licznik = 0

    while licznik < 10:
        liczba = int(input('Podaj liczbę: '))
        if liczba % 2 == 0:
            parzyste_liczby.append(liczba)
        licznik = licznik + 1
    print(f'Gotowa liczba parzystych liczb: {parzyste_liczby}')


def zadanie8():
    lista_elementow = [1, 'a', 2, 'b', 3, 'a', 4, 'c', 5, 'b', 1, 2, 3, 'a','a']
    slownik = {}

    for element in lista_elementow:
        if element in slownik:
            slownik[element] += 1
        else:
            slownik[element] = 1

    print(f'Słownik przed: {slownik}')

    klucze_do_usuniecia = []
    for klucz in slownik:
        if not isinstance(klucz, (int, float)):
            klucze_do_usuniecia.append(klucz)

    for klucz in klucze_do_usuniecia:
        del slownik[klucz]

    print(f'Słownik po: {slownik}')



def main():
    # zad()
    # zad1()
    # zad2()
    # zad3()
    # zadanie1()
    # zadanie2()
    # zadanie3()
    # zadanie4()
    # zadanie5()
    # zadanie6()
    # zadanie7()
    zadanie8()


if __name__ == '__main__':
    main()

