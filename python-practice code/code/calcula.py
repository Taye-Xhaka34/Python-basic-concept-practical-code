#create 4 functions add, subtract, multiply and divide and those functions return the result ot two arguments num1, num2. and accept 2 numbers user and do the calculation and display the result
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))
    
