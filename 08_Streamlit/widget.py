import streamlit as st
import pandas as pd
st.title("TExt input")
name=st.text_input("Enter Your Name:")
age=st.slider("Select your age:",0,100,25)

options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("choose you favorite language",options)
st.write(f"you selected {choice}")

st.write("your age is",age)
if name:
    st.write(f"hello {name}")

data={
    "name":["sameer","arbaz","suhail","khan"],
    "Age":[28,24,98,43],
    "city":["aligarh","Delhi","Banglore","Gurugram"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv") # to save the file
st.write(df)

uploaded_file=st.file_uploader("Choose a CSV file",type='csv')
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)