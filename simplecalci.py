import streamlit as st 

# title

st.title ("Simple Calculator")

# inputs

num1 = st.number_input("Enter the 1st number: ") 
num2 = st.number_input("Enter the 2nd number: ")

# Dropdom menu for operatin selection

operation = st.selectbox("Choose an operation you want to perform",("Add","Subtract","Multiply", "Divide"))

# perform the calculation on the selected operation

if operation == "Add":
    result = num1 + num2

elif operation == "Subtract":
    result = num1 - num2

elif operation == "Multiply":
    result = num1 * num2

elif operation == "Divide":
    result = num1 / num2

else:
    result = "Error, Divison by zero."

# result

st.write("Result; :", result)
