# Import required libraries
import numpy as np
import pandas as pd
import os

# Creating a training sample
train_data = pd.DataFrame({
    'price': np.round(np.random.normal(650000, 100000, 1000)),
    'delivery_time': np.round(np.random.normal(25, 10, 1000)),
    'number_of_transit_nodes': np.round(np.random.normal(3, 2, 1000)),
})

# Adding a label to a train depending on the delivery time
train_data['label'] = np.where(train_data['delivery_time'] > 25, 1, 0)

# Creating a test sample
test_data = pd.DataFrame({
    'price': np.round(np.random.normal(650000, 100000, 500)),
    'delivery_time': np.round(np.random.normal(25, 10, 500)),
    'number_of_transit_nodes': np.round(np.random.normal(3, 2, 500)),
})

# Adding a label to test depending on delivery time
test_data['label'] = np.where(test_data['delivery_time'] > 25, 1, 0)

# Creating the train and test folders
if not os.path.exists('train'):
  os.makedirs('train')
if not os.path.exists('test'):
  os.makedirs('test')

# Saving data to files
train_data.to_csv('train/train_data.csv', index=False)
test_data.to_csv('test/test_data.csv', index=False)
