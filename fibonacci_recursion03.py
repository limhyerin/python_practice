# 전역변수 선언
count = 0 # 피보나치 수열에서 덧셈한 횟수

# 함수를 선언
def fibonacci(n):
    count += 1
    
    # 피보나치 수를 구하는 내용
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# 함수 호출
print(fibonacci(15))