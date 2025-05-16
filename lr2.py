import streamlit as st
import pickle

st.title("Taxi Rider prediction")
pr=st.number_input("Enter price per week")
pop=st.number_input("Enter population")
mi=st.number_input("Enter monthly income")
apm=st.number_input("Enter average parking per month")

button=st.button("Predict")
if button:
    model=pickle.load(open("taxi.pkl","rb"))
    res=model.predict([[pr,pop,mi,apm]])[0]
    st.markdown(f"Predicted iris Class: {res}")