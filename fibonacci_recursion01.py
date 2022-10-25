# 함수를 선언
def fibonacci(n):
    # 피보나치 수를 구하는 내용
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
        
# 피보나치 출력
print("fibonacci(1) : ", fibonacci(1))
print("fibonacci(2) : ", fibonacci(2))
print("fibonacci(3) : ", fibonacci(3))
print("fibonacci(4) : ", fibonacci(4))
print("fibonacci(5) : ", fibonacci(5))