
numbers = [1,2,3,4,1,2,3,1,4,1,2,3]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] = counter[num]+1
    else:
        counter[num] = 1

print(numbers,"에서 사용된 숫자의 종류는",len(counter.keys()),"개입니다") 
# 딕셔너리 키 개수 구하는 함수 : len(딕셔너리.keys())
print("참고: ",counter)

