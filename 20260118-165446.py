import streamlit as st
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

st.set_page_config(page_title="Calculator App", page_icon="🧮")

st.title("🧮 Web-Based Calculator")
st.write("Perform basic arithmetic operations using Python and Streamlit.")

num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")
operation = st.selectbox(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

if st.button("Calculate"):
    if operation == "Addition":
        result = add(num1, num2)
    elif operation == "Subtraction":
        result = subtract(num1, num2)
    elif operation == "Multiplication":
        result = multiply(num1, num2)
    elif operation == "Division":
        result = divide(num1, num2)

    st.success(f"Result: {result}")

st.markdown("---")
st.caption("Calculator Application using Python & Streamlit")
