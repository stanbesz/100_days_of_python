def add(a,b):
    print(f"{a} + {b} = {a+b}")
    return a+b

def multiply(a,b):
    print(f"{a} * {b} = {a*b}")
    return a*b

def divide(a,b):
    print(f"{a} / {b} = {a/b}")
    return a/b

def subtract(a,b):
    print(f"{a} - {b} = {a-b}")
    return a - b

operators = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def operation(num1,num2,symbol):
    result = 0

    if not isinstance(num1,(float,int)) or not isinstance(num2,(float,int)):
        print("Invalid data types")
        return

    if symbol in operators.keys():
        result = operators[symbol](num1,num2)
    else:
        print("Invalid operand")
        return None
    
    return result

print(

    """
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
    """
)
print("To use the calculator use the options '*','/','-' or '+'")
print("To exit write 'exit'")
loop_active = True

while loop_active:
    num1 = float(input("Provide first number: "))
    symbol = input("What operation will be done?\n+\n-\n*\n/\n")
    num2 = float(input("Provide second number: "))
    result_calc = operation(num1,num2,symbol)

    further_calculation = input(f"Type 'y' to continue calculation with {result_calc} or type 'n' to start a new calculation?  or 'exit'?").lower()
    while further_calculation == "y":
        symbol = input("What operation will be done?\n+\n-\n*\n/\n")
        num2 = float(input("Provide second number: "))
        result_calc = operation(result_calc,num2,symbol)
        further_calculation = input(f"Type 'y' to continue calculation with {result_calc} or type 'n' to start a new calculation? or 'exit'?").lower()

    if further_calculation == "exit":
        print("Please come again!")
        loop_active = False