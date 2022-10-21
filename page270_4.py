# 2차원 리스트 평탄화 page 270

list_a = [1,2,[3,4],5,[6,7],[8,9]]
num = []

for i in list_a:
    if type(i) == list:
        for j in i:
            num.append(j)
    else:
        num.append(i)

print(num)

