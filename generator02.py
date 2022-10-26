# 함수를 선언합니다
def test():
    print("A지점 통과")
    yield "첫번째 통과하셨습니다"
    print("B지점 통과")
    yield "두번째 통과하셨습니다"
    print("C지점 통과")
    yield "세번째 통과하셨습니다"

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
