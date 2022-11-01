# 로또 추첨기
# 로또 LOTTO 번호 무작위로 6개 출력하는 프로그램 | 기본 형식
import random

list = []
for i in range(6):
    num = random.randrange(1,46)
    if num in list:
        num = random.randrange(1,46)
    list.append(num)

print("로또 번호 : {}".format(list))
