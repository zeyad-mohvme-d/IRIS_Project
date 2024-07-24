from controller.LoadModel import LoadModel
from controller.Getprediction import GetPrediction
import streamlit as st

st.title("Iris Flowers Prediction ")
st.write("Enter the characteristics of the flower ")

sepal_length = st.number_input(
    "sepal length:", max_value=10.0, min_value=0.0, step=0.01)
sepal_width = st.number_input(
    "sepal width:", max_value=10.0, min_value=0.0, step=0.01)
petal_length = st.number_input(
    "petal length:", max_value=10.0, min_value=0.0, step=0.01)
petal_width = st.number_input(
    "petal width:", max_value=10.0, min_value=0.0, step=0.01)

model = LoadModel('model/Iris_model.pkl')

if st.button('predict'):
    prediction = GetPrediction(
        model, [sepal_length, sepal_width, petal_length, petal_width])

    st.write(f"The prediction is {prediction}")
