def calculator(a , b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "Error: Invalid operation"
a = float(input("Enter first number: "))
b = float(input("Enter first number: "))
c = str(input("Enter any one operation[+,-,*,/]: "))
print("Answer :", calculator(a , b , c))