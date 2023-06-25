import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Загрузка модифицированного датасета
df = pd.read_csv('datasets_storage/data_prep2.csv')

# Создание нового признака с использованием one-hot-encoding для поля "departure_city"
onehot_encoder = OneHotEncoder(sparse_output=False)  # Явно указываем sparse_output=False
departure_city_ohe = onehot_encoder.fit_transform(df[['departure_city']])
departure_city_ohe_df = pd.DataFrame(departure_city_ohe, columns=onehot_encoder.categories_[0])
df = pd.concat([df, departure_city_ohe_df], axis=1)

# Сохранение датасета с новым признаком
df.to_csv('datasets_storage/data_prep3.csv', index=False)
