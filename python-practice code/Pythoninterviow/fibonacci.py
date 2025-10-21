def fibonac(n):
    if n <= 1:
        return n
    else:
        return fibonac(n-1) + fibonac(n-2)  # ✅ return the sum

s = int(input("Enter a number: "))
print(fibonac(s))
