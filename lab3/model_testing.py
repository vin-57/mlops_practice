# Import required libraries
import pandas as pd
import pickle


# Loading preprocessed test data from a file
test_data = pd.read_csv('test/test_data.csv')

# Loading a model from the model.pkl file
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Model evaluation on test data
X_test = test_data[['price', 'delivery_time', 'number_of_transit_nodes']]
y_test = test_data['label']
accuracy = model.score(X_test, y_test)

# Output of test results
print("Model test accuracy is:", accuracy)
