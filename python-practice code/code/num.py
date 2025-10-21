#create a program that accepts two 10 numbers, then filter the evens, then add 15 to them. display "your data:[.. ..]" and hint don't forget to accept int() only,use loops,filter,map
numbers = []
for i in range(10):
    num = int(input("Enter number {}: ".format(i + 1)))
    numbers.append(num)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
modified_numbers = list(map(lambda x: x + 15, even_numbers))
print("Your data:", modified_numbers)
# End of recent edits