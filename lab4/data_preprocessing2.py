import pandas as pd


# Загрузка датасета
df = pd.read_csv('datasets/data_prep1.csv')

# Заполнение пропущенных значений в поле "price" средним значением
mean_price = df['price'].mean()

# Модификация датасета
df['price'].fillna(mean_price, inplace=True)

# Сохранение модифицированного датасета
df.to_csv('datasets_storage/data_prep2.csv', index=False)
