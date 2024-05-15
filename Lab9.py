import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def wprowadzenie():
    print('Wykres liniowy')
    ts = pd.Series(np.random.randn(1000))
    # Generuje skumulowana ilosc elementow

    ts = ts.cumsum()
    print(ts)
    ts.plot()
    plt.show()

    print('Wykres kolumnowy')

    dane = {
        'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]
    }

    df1 = pd.DataFrame(dane)
    print(df1)

    grupa = df1.groupby(['Kontynent']).agg({'Populacja': 'sum'})
    print(grupa)

    wykres1 = grupa.plot.bar()
    wykres1.set_ylabel('Populacja')
    wykres1.set_xlabel('Kontynent')
    wykres1.tick_params(axis='x', labelrotation=0)
    wykres1.legend()
    wykres1.set_title('Populacja z podziałem na kontynenty')

    plt.savefig('wykres1.png')
    plt.show()

    # Wczytanie danych z pliku i Wyświetlanie wartości

    # Wczytanie danych z pliku CSV
    df2 = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
    print(df2)

    # Grupowanie danych
    grupa2 = df2.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia': 'sum'})
    print(grupa2)

    # Generowanie wykresu kołowego
    fig, ax = plt.subplots()
    grupa2.plot(kind='pie', y='Wartość zamówienia', autopct='%.2f%%', fontsize=20, figsize=(6, 6),
                colors=['red', 'green'], ax=ax)
    plt.legend(loc="lower right")
    plt.title('Suma zamówienia dla sprzedawcy')
    plt.show()

    # dodatkowy wykres
    ts2 = pd.Series(np.random.randn(1000))
    ts2 = ts2.cumsum()
    df3 = pd.DataFrame(ts2, columns=['wartości'])
    print(df3)
    df3['Średnia krocząca'] = df3['wartości'].rolling(window=50).mean()
    df3.plot()
    plt.legend()
    plt.show()


def zad1():
    print('Zadanie 1')
    data = pd.read_excel('/datasets/datasets/imiona.xlsx')
    df = pd.DataFrame(data)
    print(df)
    grupa_roczna = df.groupby('Rok')['Liczba'].sum()
    print(grupa_roczna)
    plt.figure(figsize=(10, 6))
    grupa_roczna.plot(kind='line', marker='o', color='pink')

    plt.title('Liczba urodzonych dzieci dla każdego roku')
    plt.xlabel('Rok')
    plt.ylabel('Liczba urodzeń')
    plt.grid(True)
    plt.xticks(grupa_roczna.index)
    plt.tight_layout()
    plt.show()


def zad2():
    print('Zadanie 2')
    data = pd.read_excel('/datasets/datasets/imiona.xlsx')
    df = pd.DataFrame(data)
    print(df)

    grupa_plec = df.groupby('Plec')['Liczba'].sum()
    print(grupa_plec)
    plt.figure(figsize=(10, 6))
    grupa_plec.plot(kind='bar', color=['pink', 'cyan'])

    plt.title('Liczba urodzonych chłopców i dziewczynek')
    plt.xlabel('Płeć')
    plt.ylabel('Liczba urodzeń')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def zad3():
    data = pd.read_excel('/datasets/datasets/imiona.xlsx')
    df = pd.DataFrame(data)

    print(df)
    df_ostatnie_5_lat = df[(df['Rok'] >= 2013) & (df['Rok'] <= 2017)]
    grupa_plec_ostatnie_5_lat = df_ostatnie_5_lat.groupby('Plec')['Liczba'].sum()
    print(grupa_plec_ostatnie_5_lat)
    plt.figure(figsize=(8, 8))
    grupa_plec_ostatnie_5_lat.plot(kind='pie', autopct='%.2f%%', colors=['pink', 'cyan'])
    plt.title('Procentowy udział urodzeń chłopców i dziewczynek w latach 2013-2017')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()


def zad4():
    df = pd.read_csv('/datasets/datasets/zamowienia.csv', sep=';')
    print(df)

    grupa_sprzedawca = df.groupby('Sprzedawca').size()
    print(grupa_sprzedawca)
    plt.figure(figsize=(10, 6))
    grupa_sprzedawca.plot(kind='bar', color=['plum', 'lightpink', 'lavender', 'skyblue', 'hotpink',
                                             'lightskyblue', 'lightsteelblue', 'orchid', 'palevioletred'])
    plt.title('Ilość złożonych zamówień przez poszczególnych sprzedawców')
    plt.xlabel('Sprzedawca')
    plt.ylabel('Ilość zamówień')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    # wprowadzenie()
    zad1()
    zad2()
    zad3()
    zad4()


if __name__ == '__main__':
    main()
