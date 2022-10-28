# 숫자 다섯 개가 리스트에 담겨있어요
my_list = [1,2,3,4,5]
var1 = 0

# my_list의 합을 넣어보세요
"""
#아래 동일
for i in range(len(my_list)):
    var1 += i
"""
var1 = sum(my_list)

# my_list의 길이를 넣어 보세요
var2 = len(my_list)

#my_list 원소의 평균을 넣어보세요
var3 = var1/var2

print(var1)
print(var2)
print(var3)