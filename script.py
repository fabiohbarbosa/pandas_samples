import pandas as pd


def type_price(price):
    if price < 500000:
       return 'Normal'
    if price >= 500000 and price < 1000000:
       return 'Expensive'
    if price >= 1000000:
       return 'Very Expensive'

df = pd.read_csv('files/house_data.csv')

pd.value_counts(df['bedrooms'])
df.loc[df['bedrooms'] == 3]
df['cat_by_price'] = df['price'].apply(type_price)

print df[['price', 'cat_by_price']]