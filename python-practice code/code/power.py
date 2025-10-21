def power(x, n):
    pow = x**n
    return pow
num1 = int(input("Enter a number: "))
num2 = int(input("Enter the power: "))
result = power(num1, num2)
print(f"{num1} raised to the power of {num2} is {result}")
