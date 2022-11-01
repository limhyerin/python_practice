import random
# 로또 추첨기
# 로또 LOTTO 번호 무작위로 6개 출력하는 프로그램
# 함수로 정의한 로또 추첨 프로그램
import random

def random_num():
    list = []
    for i in range(6):
        num = random.randrange(1,46)
        if num in list:
            num = random.randrange(1,46)
        list.append(num)
    return list

a = random_num()
print("로또 번호 : {}".format(a))
