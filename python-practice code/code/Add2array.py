arr1 = [2, 4, 6, 8]
arr2 = [1, 3, 5, 7]
result = []
for i in range(len(arr1)):
    sum_value = arr1[i]+arr2[i]
    result.append(sum_value)
    print("arr 1:", arr1)
    print("arr 2:", arr2)
    print("sum of arr1 and arr2:", result)