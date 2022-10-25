# 전역변수 선언
count = 0 # 피보나치 수열에서 덧셈한 횟수

# 함수를 선언
def fibonacci(n):
    # 어떤 피보나치 수열을 구하는지 출력
    print("fi({})를 구합니다".format(n))
    
    # 전역변수를 함수에서 사용하고자 할때 global 키워드를 이용하여 참조
    global count 
    count += 1
    
    # 피보나치 수를 구하는 내용
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# 해당 내용 출력
print("fibonacci(15) : ", fibonacci(15))
print("fi(15) 계산에 활용된 덧셈 횟수는 {}번입니다.".format(count))