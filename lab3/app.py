import streamlit as st
import pickle

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(price, delivery_time, number_of_transit_nodes):
    # Perform prediction using the loaded model
    prediction = model.predict([[price, delivery_time, number_of_transit_nodes]])
    return prediction[0]

def main():
    st.title('Delivery Time Prediction')

    # Input form
    st.subheader('Input')
    price = st.number_input('Price', value=0.0)
    delivery_time = st.number_input('Delivery Time', value=0.0)
    transit_nodes = st.number_input('Number of Transit Nodes', value=0)

    if st.button('Predict'):
        # Perform prediction
        prediction = predict(price, delivery_time, transit_nodes)
        st.success(f'The predicted delivery time is: {prediction}')

if __name__ == '__main__':
    main()
