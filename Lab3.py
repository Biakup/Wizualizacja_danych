import random


def zad1():
    a = [1 - x for x in range(1, 11)]
    print(f'Zbior A to: {a}')

    b = [x**2 for x in range(1, 8)]
    print(f'Zbior B to: {b}')

    c = [x for x in b if x % 2 == 0]
    print(f'Zbior C to: {c}')


def zad2():
    lista1 = [random.randint(1, 100) for _ in range(10)]
    print(f'Lista 1: {lista1}')
    lista2 = [x for x in lista1 if x % 2 == 0]
    print(f'Lista tylko z parzystymi elementami: {lista2}')


def zad3():
    produkty = {"jabłka": "kg", "jajka": "sztuki", "pomarańcze": "kg", "cola": "sztuki", "bułka słodka": "sztuki"}
    print(f'Produkty: {produkty}')
    sztuki = [produkt for produkt, jednostka in produkty.items() if jednostka == "sztuki"]
    print(f'Produkty na sztuki: {sztuki}')


def zad4():
    a = float(input('Podaj długość pierwszego boku: '))
    b = float(input('Podaj długość drugiego boku: '))
    c = float(input('Podaj długość trzeciego boku: '))

    def trojkat_prostokatny(x, y, z):
        najdluzszy = max(x, y, z)
        suma_mniejszych = (x ** 2) + (y ** 2) + (z ** 2) - (najdluzszy ** 2)
        if suma_mniejszych == najdluzszy ** 2:
            return True
        else:
            return False

    odpowiedz = trojkat_prostokatny(a, b, c)

    if odpowiedz is True:
        print('Podany trókąt jest prostokątny')
    else:
        print('Podany trókąt nie jest prostokątny')


def zad5():
    def pole_tarpezu(a, b, h):
        p = ((a+b) * h)/2
        return p

    pole = pole_tarpezu(6, 5, 4)
    print(f'Pole trapezu wynosi: {pole}')


def zad6():
    def iloczyn_elementow(a, b, ile):
        iloczyn = 1
        for i in range(ile):
            iloczyn = iloczyn * a
            a = a*b
        return iloczyn

    wynik = iloczyn_elementow(1, 4, 10)
    print(f'Iloczyn elementów ciągu wynosi: {wynik}')


def zad7():
    liczba = float(input('Podaj liczbe: '))

    if liczba >= 0:
        pierwiatsek = liczba ** 0.5
        print(f'Pierwiastek z {liczba} to {pierwiatsek}')
    else:
        print('To liczba ujemna!!!')


def main():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()
    zad7()


if __name__ == '__main__':
    main()
