# 메모 변수를 만듭니다
# 값을 딕셔너리에 저장을 하기 때문에 찾을 때마다 이곳저곳 불러오는게 아닌 저장된 정보를 불러오면 됌
dictionary = {
    1:1,
    2:1
}

# 함수를 선언합니다
def fibonacci(n):
    if n in dictionary:
        # 메모가 되어 있으면 메모된 값을 리턴
        return dictionary[n]
    else:
        # 메모가 되어 있지 않으면 값을 구함
        output = fibonacci(n-1)+fibonacci(n-2)
        dictionary[n] = output
        return output

# 함수를 호출합니다
print("fibonacci(10): ", fibonacci(10))
print("fibonacci(20): ", fibonacci(20))
print("fibonacci(30): ", fibonacci(30))
print("fibonacci(40): ", fibonacci(40))
print("fibonacci(50): ", fibonacci(50))

