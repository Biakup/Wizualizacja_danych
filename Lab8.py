import pandas as pd


def main():
    print('Zadanie 1')
    df = pd.read_excel('/datasets/datasets/imiona.xlsx')
    print(df.head())

    print('Zadanie 2')
    print('Zadanie 2.1')
    df_1000 = df[df['Liczba'] > 1000]
    print('Liczba nadanych imion była większa niż 1000 w danym roku')
    print(df_1000)

    print('Zadanie 2.2')
    df_zuzanna = df[df['Imie'] == 'ZUZANNA']
    print('Tylko rekordy, gdzie nadane jest moje imie')
    print(df_zuzanna)

    print('Zadanie 2.3')
    df_urodzenia = df['Liczba'].sum()
    print('Suma wszystkich urodzonych dzieci w całym danym okresie')
    print(df_urodzenia)

    print('Zadanie 2.4')
    df_2000_2005 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum()
    print('Suma dzieci urodzonych w latach 2000-2005: ')
    print(df_2000_2005)

    print('Zadanie 2.5')
    df_chlopcy = df[df['Plec'] == 'M']['Liczba'].sum()
    df_dziewczyny = df[df['Plec'] == 'K']['Liczba'].sum()
    print('Suma urodzonych chłopców i dziewczynek: ')
    print(f'Chłopcy: {df_chlopcy}')
    print(f'Dziewczynki: {df_dziewczyny}')

    print('Zadanie 2.6')
    df_popularne = df.groupby(['Rok', 'Plec']).apply(lambda x: x.nlargest(1, 'Liczba'))
    print('Najbardziej popularne imię dziewczynki i chłopca w danym roku')
    print(df_popularne)

    print('Zadanie 2.7')
    grupowanie = df.groupby(['Imie', 'Plec'])['Liczba'].sum().reset_index()
    df_najpop = grupowanie.loc[grupowanie.groupby('Plec')['Liczba'].idxmax()]
    print('Najbardziej popularne imię dziewczynki i chłopca w całym danym okresie')
    print(df_najpop)

    print('Zadanie 3')

    df2 = pd.read_csv('/datasets/datasets/zamowienia.csv', sep=';', parse_dates=['Data zamowienia'])
    print(df2.head())

    print('Zadanie 3.1')
    u_sprzedawca = df2['Sprzedawca'].unique()
    print("Lista unikalnych nazwisk sprzedawców:")
    print(u_sprzedawca)

    print('Zadanie 3.2')
    top_5 = df2.nlargest(5, 'Utarg')
    print("5 najwyższych wartości zamówień:")
    print(top_5)

    print('Zadanie 3.3')
    ilosc_zamownien = df2['Sprzedawca'].value_counts()
    print("Ilość zamówień złożonych przez każdego sprzedawcę:")
    print(ilosc_zamownien)

    print('Zadanie 3.4')
    zamowienia_kraju = df2.groupby('Kraj')['Utarg'].sum()
    print('Suma zamówień dl każdego kraju: ')
    print(zamowienia_kraju)

    print('Zadanie 3.5')
    suma_2005pl = df2[(df2['Data zamowienia'].dt.year == 2005) & (df2['Kraj'] == 'Polska')]['Utarg'].sum()
    print("Suma zamówień dla roku 2005, dla sprzedawców z Polski:")
    print(suma_2005pl)

    print('Zadanie 3.6')
    srednia_2004 = df2[(df2['Data zamowienia'].dt.year == 2004)]['Utarg'].mean()
    print('Średnia kwota zamówienia w 2004: ')
    print(round(srednia_2004, 2))

    print('Zadanie 3.7')
    zamowieni_2004 = df2[df2['Data zamowienia'].dt.year == 2004]
    zamowieni_2004.to_csv('zamowienia_2004.csv', index=False)

    zamowieni_2005 = df2[df2['Data zamowienia'].dt.year == 2005]
    zamowieni_2005.to_csv('zamowienia_2005.csv', index=False)


if __name__ == '__main__':
    main()
