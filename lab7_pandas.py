import pandas as pd

s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruklsela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528],
        }

df = pd.DataFrame(data)

"""
# 1
print(df)
print(s['c'])
print(s.c)

print(df[0:1])
print("")

print(df['Populacja'])
print(df.iloc[0, 0])
print(df.loc[0, 'Kraj'])
print(df.at[0, 'Kraj'])
print(df.loc[0])

print('Kraj: ' + df.Kraj)
print(df.sample())

print(df.sample(2))
print(df.sample(frac=0.5))
print(df.sample(n=10, replace=True))
print(df.head())
print(df.head(2))
print(df.tail(1))
print(df.describe())
print(df.T)

"""

"""
# 2

print(s[(s > 9)])

print(s.where(s > 10))

print(s.where(s > 10, 'za duze'))
seria = s.copy()
seria.where(seria > 10, 'za duze', inplace=True)
print("########")
print(seria)

print(s[~(s > 10)])

print(s[(s < 13) & (s > 8)])


print(df[df['Populacja'] > 1200000000])
print(df[(df.Populacja > 1000000) & (df.index.isin([0, 2]))])
print('#########')
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))
"""

"""

# 3

s['e'] = 15
print(s.e)
s['f'] = 16
print(s)

df.loc[3] = 'dodane'
print(df)

df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)

new_df = df.drop([3])
print(new_df)

df.drop([3], inplace=True)
print(df)


# df.drop('Kraj', axis=1, inplace=True)

df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']
print(df)

print(df.sort_values('Kraj'))

grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))

print(df.groupby(['Kontynent']).agg({"Populacja": {'sum'}}))

"""
#
data_iris = pd.read_csv('./iris.data', header=None)
print(data_iris)

excel_iris = pd.read_excel('./iris.data')
print(excel_iris)


# print(data_iris[10:21])
# sliced_data = data_iris[1:5]
# print(sliced_data)

