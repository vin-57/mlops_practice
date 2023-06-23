import streamlit as st
import pickle

# Load the model
with open('lab3/model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(price, delivery_time, number_of_transit_nodes):
    # Perform prediction using the loaded model
    prediction = model.predict([[price, delivery_time, number_of_transit_nodes]])
    return prediction[0]

def main():
    st.title('Предсказание возможности отказа клиента от доставки')

    # Input form
    st.subheader('Входные данные')
    price = st.number_input('Цена в рублях', value=0.0)
    delivery_time = st.number_input('Время доставки в минутах', value=0.0)
    transit_nodes = st.number_input('Количество промежуточных точек', value=0)

    if st.button('Predict'):
        # Perform prediction
        prediction = predict(price, delivery_time, transit_nodes)
        st.success(f'Вероятный отказ клиента (1 - откажется, 0 - не откажется): {prediction}')

if __name__ == '__main__':
    main()
