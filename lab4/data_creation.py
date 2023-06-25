# Импорт необходимых библиотек
import numpy as np
import pandas as pd
import os

# Добавляем новый столбец - departure_city ("город отправления")
cities = ['Guangzhou', 'Moscow']
departure_city = np.random.choice(cities, size=1000)
np.random.seed(0)

# Добавляем новый столбец - forwarder ("экспедитор")
forwarder = ['Guangzhou_forwarder', 'Moscow_forwarder']
freight_forwarder = np.random.choice(forwarder, size=1000)
np.random.seed(0)

# Создание датасета
data = pd.DataFrame({
    'price': np.abs(np.random.normal(650000, 100000, 1000)),
    'delivery_time': np.abs(np.random.normal(25, 10, 1000)),
    'number_of_transit_nodes': np.abs(np.round(np.random.normal(3, 2, 1000))),
    'departure_city': departure_city,
    'freight_forwarder': freight_forwarder
})

# Добавление случайных пропусков в столбце 'price'
num_missing = 5  # Количество пропусков для добавления
missing_indices = np.random.choice(data.index, size=num_missing, replace=False)
data.loc[missing_indices, 'price'] = np.nan

# Сохранение данных в файл
data.to_csv('datasets_storage/data.csv', index=False)
