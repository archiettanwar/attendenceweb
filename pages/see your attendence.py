import streamlit as st
import csv
import pandas

df=pandas.read_csv("Book1.csv")

col1,col2=st.columns(2)
with col1:
    st.header("name of subject")

    with open("Book1.csv",'r') as file:
        reader=list(csv.reader(file))

    sub_index=0

    for i in range(1,len(reader)):
        st.write(reader[i][sub_index])

with col2:
    st.header("Percentage Present changed")

    for i in range(len(df)):
        subject = df["subject"][i]
        present = df["present"][i]
        total = df["total"][i]

        if total == 0:
            percent = 0
        else:
            percent = (present / total) * 100

        if percent >= 50:
            st.write(f"{percent:.2f}% ✅")
        else:
            st.error(f"{percent:.2f}% ❌")