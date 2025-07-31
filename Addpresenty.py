import streamlit as st
import pandas as pd
import csv
import os

if not os.path.exists("Book1.csv"):
    with open("Book1.csv",'w') as file:
        pass

col1,col2=st.columns(2)

with col1:
    st.title("Attendence Tracker")

with col2:
    st.image("image.png")
#getting the csv file
df = pd.read_csv("Book1.csv")

# yaha subject choose hoga subject variable mai
subject = st.selectbox("Choose a subject", df["subject"])

# Buttons for marking attendance
present = st.button("Present")
absent = st.button("Absent")


if present or absent:
    # reader ek list hai jisme list hai csv file ke cloumn wise
    with open("Book1.csv", 'r') as file:
        reader = list(csv.reader(file))

    header = reader[0]  # ['subject', 'present', 'total']
    subject_index = 0   # subject is in column 0
    present_index = 1   # present count is in column 1
    total_index = 2     # total days is in column 2

    for i in range(1, len(reader)):#reads through all rows
        if reader[i][subject_index] == subject:
            # Convert present string to int for math
            pres = int(reader[i][present_index])
            total = int(reader[i][total_index])

            if present:
                pres += 1  # increment present
            # absent doesn't change present count

            total += 1  # increment total in both cases

            # Update row with strings
            reader[i][present_index] = str(pres)
            reader[i][total_index] = str(total)
            break

    # Write back to the file
    with open("Book1.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(reader)

    st.info(f"Marked {'Present' if present else 'Absent'} for {subject}")
