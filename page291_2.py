# 매개변수로 전달된 값들을 모두 곱해서 리턴하는 가변 매개변수 함수

def mul(*values):
    result = 1
    for i in values:
        result *= i
    return result

# 함수 호출
print(mul(5,7,9,10))

