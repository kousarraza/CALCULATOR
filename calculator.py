import streamlit as st
# Title of the app
st.title("🔢Simple Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Dropdown for selecting the operation
operation = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate based on the selected operation
result = None
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed"

# Display the result
st.write(f"Result: {result}")
