#factorial example

def factorial(n):
    mul = 1
    for i in range(1, n+1):
        mul *= i
    return mul

user_input = int(input("팩토리얼 입력>> "))
print(factorial(user_input))