# 염기서열을 사용자로부터 입력받고 각각의 염기가 몇개 포함되어 있는지 세는 프로그램
"""
#case 1
user_input = input("염기서열을 입력해주세요 : ")
keys = []
values = []
pair = []

for i in user_input:
    keys.append(pair[0])
    values.append(pair[1])

print("{}의 개수: {}".format(keys, values))


#case 2 
count_a = 0
count_t = 0
count_g = 0
count_c = 0
user_input = input("염기 서열을 입력해주세요: ")

for i in user_input:
    if i == "a":
        count_a += 1
    elif i == "t":
        count_t += 1
    elif i == "g":
        count_g += 1
    elif i == "c":
        count_c += 1

print("a의 개수: {}".format(count_a))
print("t의 개수: {}".format(count_t))
print("g의 개수: {}".format(count_g))
print("c의 개수: {}".format(count_c))
"""

#case 3
user_input = input("염기서열을 입력해주세요:")
counter = {
    "a":0,
    "t":0,
    "g":0,
    "c":0
}

for i in user_input: # 입력받은 염기서열을 하나하나 카운트를 올려서 저장
    counter[i] += 1

for key in counter: # 각각의 키와 값을 반복문으로 반복해서 출력
    print("{}의 개수 : {}".format(key, counter[key]))

    