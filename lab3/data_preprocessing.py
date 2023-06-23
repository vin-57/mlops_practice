# Import required libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Loading training and test data
# sets of CSV files for analysis and processing.
train_data = pd.read_csv('train/train_data.csv')
test_data = pd.read_csv('test/test_data.csv')

# Performing Feature Standardization
# "price" (cost of delivery), "delivery_time" (delivery time) и "number_of_transit_nodes" (number of transit nodes)
# in training and test datasets.
scaler = StandardScaler()
train_data[['price', 'delivery_time', 'number_of_transit_nodes']] = scaler.fit_transform(train_data[['price', 'delivery_time', 'number_of_transit_nodes']])
test_data[['price', 'delivery_time', 'number_of_transit_nodes']] = scaler.transform(test_data[['price', 'delivery_time', 'number_of_transit_nodes']])

# Checking if two directories exist:
# 'train_preprocessed' and 'test_preprocessed',
# for the purpose of saving preprocessed training and test data.
if not os.path.exists('train_preprocessed'):
    os.makedirs('train_preprocessed')
if not os.path.exists('test_preprocessed'):
    os.makedirs('test_preprocessed')

# Saving preprocessed training data
# and test data in CSV format
train_data.to_csv(
    'train_preprocessed/train_data_preprocessed.csv', index=False
    )
test_data.to_csv(
    'test_preprocessed/test_data_preprocessed.csv', index=False
    )
