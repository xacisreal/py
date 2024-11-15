print("Calculator by Xac👾")
while True:
    operation = input("\nEnter the operation or Press x to exit: ")
    if operation == 'x' or operation =='X':
        print("Thank you")
        break
    if operation in ['+', '-', '*', '/']:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Error......Please enter numbers")
            continue
        if operation == '+':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == '-':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == '*':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == '/':
            if num2 == 0:
                print("Invalid")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid operation! Please enter +, -, *, or /. and if you wnat to exit press 'x'")
