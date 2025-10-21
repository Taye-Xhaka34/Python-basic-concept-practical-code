def fact(m):
    if m==0:
        return 1
    return m * fact(m-1)
result = fact(5)
print(result)