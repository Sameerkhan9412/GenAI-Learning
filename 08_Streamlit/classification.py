import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data # to save data to cach to reduce loading time
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df["species"]=iris.target
    return df,iris.target_names

df,target_names=load_data()
model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df["species"])

st.sidebar.title("Input features")
sepal_length=st.sidebar.slider("Sepal length",float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width=st.sidebar.slider("Sepal width",float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petal_length=st.sidebar.slider("petal length",float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petal_width=st.sidebar.slider("petal width",float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))

import_data=[[sepal_length,sepal_width,petal_length,petal_width]]

# Prediction
prediction=model.predict(import_data)
predicted_species=target_names[prediction[0]]

st.write("Prediction:")
st.write(f"The predicted species is :{predicted_species}")