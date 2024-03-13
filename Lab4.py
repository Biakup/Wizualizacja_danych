import math
import random

def zad1():
    p = round((math.e ** 4 - math.log2(34)) ** (1 / 3), 2)
    print(f'Przykład 1: {p}')
    p2 = round((math.log(20) + math.cos(math.radians(45)) + math.e) ** (1 / 3), 2)
    print(f'Przykład 2: {p2}')
    p3 = round(((math.log(20) / math.log(3)) + math.sin(math.radians(45)) * (5 / 8)) ** (1 / 4), 2)
    print(f'Przykład 3: {p3}')
    p4 = round((math.log(23) / math.log(3)) + ((math.sin(math.radians(34)) + 5) ** (1 / 3)), 2)
    print(f'Przykład 4: {p4}')
    p5 = round((math.log2(23) + math.pi + math.sin(math.radians(56))) ** (1 / 4), 2)
    print(f'Przykład 5: {p5}')

def zad2():
    x = int(input("Podaj jak wysoka ma być wieża (max 10): "))
    if x <= 10:
        for i in range(1, x+1):
            print("A" * i)
    else:
        print("Podałeś zbyt dużą liczbę!")


def zad3():
    x = int(input("Podaj jak wysoka ma być piramida (max 10): "))
    if x <= 10:
        for i in range(1, x + 1):
            print(" " * (x - i), "A" * (2 * i - 1))
    else:
        print("Podałeś zbyt dużą liczbę!")


def zad4():
    x = random.randint(1,100)
    print(f'Losowa liczba z przedziału 1-100: {x}')

    y = random.random()
    print(f'Losowa liczba od 0 do 1: {y}')


def zad5():
    def wektorki(n):
        for i in range(n):
            suma = 0
            for j in range(n):
                x = random.randint(1, 100)
                suma += x
                print(x, end=' ')
            print(f'= {suma}\n')

    n = int(input("Podaj n: "))
    print(wektorki(n))



def main():
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()


if __name__ == '__main__':
    main()
