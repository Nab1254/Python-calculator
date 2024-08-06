import streamlit as st
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide


def calculator():
    print("Welcome to the Calculator!")
    while True:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator")
            continue

        print(f"Result: {num1} {operator} {num2} = {result}")

        choice = input("Do you want to quit? (Y/N): ").upper()
        if choice == 'Y':
            print("Exiting the calculator.")
            break
        elif choice == 'N':
            continue
        else:
            print("Invalid choice. Continuing...")
            continue

calculator()
