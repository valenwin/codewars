def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


print(factorial(1))
print(factorial(4))
print(factorial(5))
