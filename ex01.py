def factorial(n):
    mul = 1
    for i in range(1, n+1):
        mul *= i
    return mul

print(factorial(5))