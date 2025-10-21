# Example array
numbers = [12, 45, 7, 34, 89, 23]

# Assume the first element is the maximum
max_value = numbers[0]

# Loop through each element in the array
for i in range(1, len(numbers)):
    if numbers[i] > max_value:
        max_value = numbers[i]  # update max_value

# Print result
print("Array:", numbers)
print("Maximum value:", max_value)
