# Import required libraries
import pandas as pd  # for working with tabular data
# Logistic regression classifier
from sklearn.linear_model import LogisticRegression
import pickle  # to (de)serialize objects


# Loading processed train data from train_data_preprocessed.csv file
train_data = pd.read_csv('train_preprocessed/train_data_preprocessed.csv')

# Saving signs of shipping cost, delivery time, number of transit nodesв
X_train = train_data[['price', 'delivery_time', 'number_of_transit_nodes']]

# Saving the target label
y_train = train_data['label']

# Building a Logistic Regression Model
model = LogisticRegression()

# Model training on training data
model.fit(X_train, y_train)

# Saving the model to the model.pkl file
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
