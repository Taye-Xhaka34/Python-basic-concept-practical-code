def even(number):
    return number % 2 == 0
numbers = input("Enter numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
number = []
for num in numbers:
    if even(num):
        number.append(num)
print("Even numbers are:", number)