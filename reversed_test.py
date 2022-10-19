"""
# 첫번째 반복문만 출력하는 결과가 나옴
a = reversed([1,2,3,4,5])

for i in a:
    print("첫번째 반복문 : {}".format(i))

for j in a:
    print("두번째 반복문 : {}".format(j))
"""

# 두번의 반복문이 전부 다 나옴
numbers = [1,2,3,4,5]
for i in reversed(numbers):
    print("첫 번째 반복문 : {}".format(i))

for i in reversed(numbers):
    print("두 번째 반복문 : {}".format(i))