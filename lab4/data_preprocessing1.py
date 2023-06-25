import pandas as pd


# Загрузка датасета
df = pd.read_csv('datasets_storage/data.csv')

# Выбор необходимых столбцов
df = df[['price', 'delivery_time', 'number_of_transit_nodes','departure_city']]

# Сохранение модифицированного датасета
df.to_csv('datasets_storage/data_prep1.csv', index=False)
