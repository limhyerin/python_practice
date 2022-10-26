# 함수를 선언합니다
def test():
    print("A지점 통과")
    yield 1  # 제너레이터를 만드는데 사용하는 키워드
    print("B지점 통과")
    yield 2
    print("C지점 통과")

# 함수를 호출합니다
output = test()
# next() 함수를 호출합니다
print("D지점 통과")
a = next(output)
print(a)
print("E지점 통과")
b = next(output)
print(b)
print("F지점 통과")
c = next(output)
print(c)
# 한번 더 실행하기
next(output)