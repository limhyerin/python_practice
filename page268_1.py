# 딕셔너리 키 개수 구하는 함수 : len(딕셔너리.keys())

numbers = [1,2,3,4,1,2,3,1,4,1,2,3]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] = counter[num]+1
    else:
        counter[num] = 1

print("{}에서 사용된 숫자의 종류는 {} 개입니다".format(numbers, len(counter.keys())))

print("참고: ",counter)

