import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import seaborn as sns


def przyklad1():
    plt.plot([1, 2, 3, 4])
    plt.ylabel('jakies liczby')
    plt.show()


# noinspection PyTypeChecker
def przyklad2():
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro--')
    plt.axis([0, 6, 0, 20])
    plt.show()

    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
    plt.axis([0, 6, 0, 20])
    plt.show()


def przyklad3():
    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
    plt.show()


def przyklad4():
    x = np.linspace(0, 2, 100)

    plt.plot(x, x, label='liniowa')
    plt.plot(x, x**2, label='kwadratowa')
    plt.plot(x, x**3, label='sześcienna')

    plt.xlabel('etykieta x')
    plt.ylabel('etykieta y')
    plt.title('Prosty wykres')
    plt.legend()
    plt.savefig('wykres matplot.png')

    # zapisywanie wykresu
    plt.show()
    im1 = Image.open('wykres matplot.png')
    im1 = im1.convert('RGB')
    im1.save('nowy.jpg')


def przyklad5():
    x = np.arange(0, 10, 0.1)
    s = np.sin(x)
    plt.plot(x, s, label='sin(x)', color='plum')

    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.title('Wykres funkcji sin(x)')
    plt.legend()
    plt.show()


def przyklad6():
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100  # Corrected this line

    print(f'a={data["a"][0]}, b={data["b"][0]}, c={data["c"][0]}, d={data["d"][0]}')
    plt.scatter('a', 'b', c='c', s=np.abs(data['d']), data=data)  # Use np.abs to ensure sizes are positive
    plt.xlabel('wartość a')
    plt.ylabel('wartość b')
    plt.show()


def przykald7():
    x1 = np.arange(0, 2, 0.02)
    x2 = np.arange(0, 2, 0.02)
    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)
    plt.subplot(2, 1, 1, )
    plt.plot(x1, y1, '-')
    plt.title('wykres sin(x)')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    _ = plt.subplot(2, 1, 2)
    plt.plot(x2, y2, 'r-')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.title('wykres cos(x)')
    plt.subplots_adjust(hspace=0.5)
    plt.show()


def przykald8():
    x1 = np.arange(0.0, 2.0, 0.02)
    x2 = np.arange(0.0, 2.0, 0.02)
    y1 = np.sin(2 * np.pi * x1)
    y2 = np.cos(2 * np.pi * x2)
    fig, axs = plt.subplots(3, 2, )
    axs[0, 0].plot(x1, y1, '-')
    axs[0, 0].set_title('wykres sin(x)')
    axs[0, 0].set_xlabel('x')
    axs[0, 0].set_ylabel('sin(x)')
    axs[1, 1].plot(x2, y2, 'r-')
    axs[1, 1].set_title('wykres cos(x)')
    axs[1, 1].set_xlabel('x')
    axs[1, 1].set_ylabel('cos(x)')
    axs[2, 0].plot(x2, y2, 'r-')
    axs[2, 0].set_title('wykres cos(x)')
    axs[2, 0].set_xlabel('x')
    axs[2, 0].set_ylabel('cos(x)')
    fig.delaxes(axs[0, 1])
    fig.delaxes(axs[1, 0])
    fig.delaxes(axs[2, 1])
    plt.show()


# noinspection PyTypeChecker
def przyklad9():
    data = {'Kraj': ['Belgia', 'Indie', 'Brazylia',
                     'polska'],
            'Stolica': ['Bruksela', 'New Delhi',
                        'Brasilia', 'Warszawa'],
            'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa',
                          'Europa'],
            'Populacja': [11190846, 1303171035, 207847528, 38675467]}
    df = pd.DataFrame(data)
    print(df)
    grupa = df.groupby('Kontynent')
    etykiety = list(grupa.groups.keys())
    wartosci = list(grupa.agg('Populacja').sum())
    plt.bar(x=etykiety, height=wartosci, color=['yellow', 'green', 'red'])
    plt.xlabel('Kontynenty')
    plt.ylabel('Populacja w mld')
    plt.show()


def przyklad10():
    x = np.random.randn(10000)
    plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Wartości')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid()
    plt.show()


def przyklad11():
    df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
    print(df)
    seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()

    _, texts, autotexts = plt.pie(
        x=seria,
        labels=seria.index,
        autopct=lambda pct: "{:.1f}%".format(pct),
        textprops=dict(color="black"),
        colors=['red', 'green']
    )

    plt.title('Suma zamówień dla sprzedawców')
    plt.legend(loc='lower right')
    plt.ylabel('Procentowy wynik wartości zamówienia')
    plt.show()


def zad1():
    x = np.linspace(1, 20, 100)
    y = 1 / x
    plt.plot(x, y, label='f(x) = 1/x')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim(1, 20)
    plt.ylim(0, 1)
    plt.legend()
    plt.show()


def zad2():
    x = np.linspace(1, 19, 20)
    f = 1 / x
    plt.plot(x, f, ':g>', label='f(x) = 1/x', color='green')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.xlim(0, 20)
    plt.ylim(0, 1)
    plt.title('Wykres funkcji f(x) dla x[1, 20]')
    plt.legend()
    plt.show()


def zad3():
    x = np.arange(0, 30, 0.1)
    sin_x = np.sin(x)
    cos_x = np.cos(x)
    plt.plot(x, sin_x, label='sin(x)', color='pink')
    plt.plot(x, cos_x, label='cos(x)', color='skyblue')

    plt.xlabel('x')
    plt.ylabel('Wartość funkcji')
    plt.legend()
    plt.show()


def zad5():
    file_path = 'datasets/datasets/imiona.xlsx'
    df = pd.read_excel(file_path)

    print(df.head())
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    total_gender = df.groupby('Plec')['Liczba'].sum()
    total_gender.plot(kind='bar', ax=axes[0], color=['pink', 'skyblue'])
    axes[0].set_title('Ilość narodzonych dziewczynek i chłopców')
    axes[0].set_xlabel('Płeć')
    axes[0].set_ylabel('Liczba narodzin')
    yearly_gender = df.groupby(['Rok', 'Plec'])['Liczba'].sum().unstack()
    yearly_gender.plot(ax=axes[1], color=['pink', 'skyblue'])
    axes[1].set_title('Ilość urodzonych kobiet i mężczyzn w każdym roku')
    axes[1].set_xlabel('Rok')
    axes[1].set_ylabel('Liczba narodzin')
    axes[1].legend(['Kobiety', 'Mężczyźni'])
    yearly_total = df.groupby('Rok')['Liczba'].sum()
    yearly_total.plot(kind='bar', ax=axes[2], color='plum')
    axes[2].set_title('Suma urodzonych dzieci w każdym roku')
    axes[2].set_xlabel('Rok')
    axes[2].set_ylabel('Liczba narodzin')
    plt.tight_layout()
    plt.show()


def zad6():
    file_path = 'datasets/datasets/zamowienia.csv'
    df = pd.read_csv(file_path, delimiter=';')
    sums = df.groupby('Sprzedawca')['Utarg'].sum()
    explode = [0.1 if sprzedawca == sums.idxmax() else 0 for sprzedawca in sums.index]
    fig, ax = plt.subplots()
    ax.pie(sums, labels=sums.index, autopct='%1.1f%%', shadow=True, explode=explode)
    plt.title('Procentowy udział sprzedawców w ogólnej sumie zamówień')
    plt.show()


def zad4():
    # Wczytanie danych Iris
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    column_names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
    iris_data = pd.read_csv(url, header=None, names=column_names)
    x = iris_data['sepal length']
    y = iris_data['sepal width']
    palette = sns.color_palette("husl", 3)
    colors = iris_data['class'].map({
        'Iris-setosa': palette[0],
        'Iris-versicolor': palette[1],
        'Iris-virginica': palette[2]
    })
    s = np.abs(x - y) * 50
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, c=colors, s=s, alpha=0.6, edgecolors='w', linewidth=0.5)
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title('Scatter Plot of Sepal Length vs Sepal Width')
    unique_classes = iris_data['class'].unique()
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=palette[i], markersize=10, label=cls)
               for i, cls in enumerate(unique_classes)]
    plt.legend(handles=handles, title='Class')
    plt.show()


def main():
    przyklad1()
    przyklad2()
    przyklad3()
    przyklad4()
    przyklad5()
    przyklad6()
    przykald7()
    przykald8()
    przyklad9()
    przyklad10()
    przyklad11()
    zad1()
    zad2()
    zad3()
    zad4()
    zad5()
    zad6()


if __name__ == '__main__':
    main()
