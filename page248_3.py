# 1부터 증가시키면서 10000을 넘는 경우를 구하는 프로그램

limit = 10000
i = 1
sum_value = 1

#빈칸
while True:
    if sum_value >10000:
        break
    else:
        i += 1
        sum_value += i
#빈칸

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.". format(i, limit, sum_value))