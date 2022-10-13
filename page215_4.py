# 실행 결과 [1,4,7], [2,5,8], [3,6,9]

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number+2)%3].append(number) #0,1,2 / 0,1,2 / 0,1,2

print(output)