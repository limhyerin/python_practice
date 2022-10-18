"""
# 원의 반지름을 입력받아 결과 도출 프로그램
str_input = input("원의 반지름 입력")
num_input = float(str_input)
print()
print("반지름:", num_input)
print("둘레:", 2*3.14*num_input)
print("넓이:", 3.14*num_input**2)



# 홀짝 구분하는 프로그램
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for num in numbers:
    if num%2 == 0:
        print(str(num)+"는 짝")
    if num%2==1:
        print(str(num)+"는 홀")



# 정수를 입력받아 2,3,4,5로 나누어떨어지는 숫자인지 판별하는 프로그램
user_input = int(input("정수를 입력해주세요:"))
if user_input % 2 == 0:
    print(user_input,"은 2로 나누어 떨어지는 숫자입니다")
if user_input % 2 != 0:
    print(user_input, "은 2로 나누어 떨어지는 숫자가 아닙니다")

if user_input % 3 == 0:
    print(user_input, "은 3으로 나누어 떨어지는 숫자입니다")
if user_input % 3 != 0:
    print(user_input, "은 3로 나누어 떨어지는 숫자가 아닙니다")

if user_input % 4 == 0:
    print(user_input, "은 4으로 나누어 떨어지는 숫자입니다")
if user_input % 4 != 0:
    print(user_input, "은 4로 나누어 떨어지는 숫자가 아닙니다")

if user_input % 5 == 0:
    print(user_input, "은 5으로 나누어 떨어지는 숫자입니다")
if user_input % 5 != 0:
    print(user_input, "은 5로 나누어 떨어지는 숫자가 아닙니다")



# 리스트 안에 있는 숫자들 중 100이상의 수를 골라내는 프로그램
numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number >= 100:
        print("100이상의 수 :", number)



# 구의 부피와 겉넓이를 구하는 프로그램
import math
pi = 3.141592
r = input("구의 반지름을 입력해주세요:")
fr = float(r)

three = math.pow(fr, 3)
two = math.pow(fr, 2)
bu = 4/3*pi*three  #구의 부피 공식
nul = 4*pi*two  #구의 겉넓이 공식

print("= 구의 부피는 ", bu, "입니다")
print("= 구의 겉넓이는 ", nul, "입니다")



# 피타고라스 정리
#a**2 + b**2 = c**
#높**2 +밑**2 = 빗**2
a = input("밑변의 길이를 입력해주세요: ")
b = input("높이의 길이를 입력해주세요: ")
fa = float(a)
fb = float(b)

fc = (fa**2)+(fb**2) #피타고라스 정리
c = fc**(0.5) #빗변의 길이 구하는 식 ; 본 숫자에 0.5 제곱

print(" = 빗변의 길이는 ",c, "입니다")





if birth_year%12 == 0:
    print("원숭이 띠입니다")
if birth_year%12 == 1:
    print("닭 띠입니다")
if birth_year%12 == 2:
    print("개 띠입니다")
if birth_year%12 == 3:
    print("돼지 띠입니다")
if birth_year%12 == 4:
    print("쥐 띠입니다")
if birth_year%12 == 5:
    print("소 띠입니다")
if birth_year%12 == 6:
    print("범 띠입니다")
if birth_year%12 == 7:
    print("토끼 띠입니다")
if birth_year%12 == 8:
    print("용 띠입니다")
if birth_year%12 == 9:
    print("뱀 띠입니다")
if birth_year%12 == 10:
    print("말 띠입니다")
if birth_year%12 == 11:
    print("양 띠입니다")


# format함수를 사용하여 문자열 (월일) 채우기
a = input("월>>")
b = input("일>>")

print("저의 생일은 {}월 {}일 입니다".format(a,b))



# 입력한 수가 조건에 해당하는지 알아보는 프로그램
a = input("입력>>")
x = int(a)
if x>10 and x<20:
    print("조건에 맞습니다")

if 10<x<20:
    print("조건에 맞습니다")



# 리스트의 숫자들의 자릿수를 출력하는 프로그램
numbers = [273,103,5,32,65,9,72,800,99]

for num in numbers:
    if num / 100 >= 1:
        print(num,"는 3 자릿수입니다.")
    elif num / 10 >= 1:
        print(num, "는 2 자릿수입니다.")
    elif num / 1 >= 1:
        print(num, "는 1 자릿수입니다.")
    else:
        print("ee")


#boruu************************************************************************
numbers = [1,2,3,4,5,6,7,8,9]
output =[[],[],[]]

a = numbers[0:7:3]
b = numbers[1:8:3]
c = numbers[2:9:3]

print(a)

for number in numbers:
    output[].append(a)
    output[].append(b)
    output[].append(c)

print(output)



pets= [
    {"name":"구름", "age":"5"}
    {"name":"초코", "age":"3"}
    {"name":"아지", "age":"1"}
    {"name":"호랑이", "age":"1"}
]

print("#우리 동네 애완 동물들")
for key in dictionary:
    print(key, dictionary[key],"살")

for i in 

for pet in pets:
    print(name)



# 별 반복문
for i in range(1,10):
    print("*"*i)

#case 2
output = ""

for i in range(1,10):
    for j in range(0,i):
        output +="*"
    output +="\n"

print(output)


# 반대로 반복
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))


# 별트리찍기
output =""
for i in range(1, 15):
    for j in range(14, i, -1):
        output += ' '
    for k in range(0,2*i-1):
        output += '*'
    output += '\n'
print(output)


# case 2
for i in range(1, 15):
    for j in range(15-i):
        print(" ", end="") # end - 다음 출력 값과 이어지게 함
    for k in range(1, i*2, 1):
        print("*", end="")
    print("")


# while과 for의 반복
print("while문 반복")
i = 0
while i<10:
    print("{}번째 반복입니다".format(i))
    i += 1

print("\n")
print("for문 반복")
for i in range(10):
    print("{}번째 반복입니다".format(i))


# 구의 부피와 겉넓이 구하는 프로그램
import math
pi = 3.141592
user_input = input("구의반지름을 입력해주세요: ")
r = int(user_input)
bu = 4/3*pi*pow(r,3)
nul = 4*pi*pow(r,2)

print("구의 부피는 ",bu,"입니다.")
print("구의 겉넓이는 ",nul,"입니다.")



# 피타고라스 정리
import math
user_input1 = input("밑변의 길이를 입력해주세요:")
user_input2 = input("높이의 길이를 입력해주세요:")
b = float(user_input1)
a = float(user_input2)

pita = pow(a,2)+pow(b,2)
c = pita**(0.5)
print("= 빗변의 길이는 ",c,"입니다.")



# datetime을 이용해서 현재 시각 나타내는 프로그램
import datetime
now = datetime.datetime.now()

print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second,
))



# 오전/오후 구분 프로그램
import datetime

now = datetime.datetime.now()

if now.hour < 12:
    print("현재시각은 {}시 {}분으로 오전입니다".format(now.hour, now.minute))

if now.hour >= 12:
    print("현재시각은 {}시 {}분으로 오후입니다".format(now.hour, now.minute))



# 현재 달을 나타내고 계절을 띄우는 프로그램
import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5:
    print("이번달은 {}월로 봄입니다!".format(now.month))
if 6 <= now.month <= 8:
    print("이번달은 {}월로 여름입니다!".format(now.month))
if 9 <= now.month <= 11:
    print("이번달은 {}월로 가을입니다!".format(now.month))
if 12 == now.month or 1 <= now.month <= 2:
    print("이번달은 {}월로 겨울입니다!".format(now.month))



# 정수를 입력받아서 홀수와 짝수를 구분하여 출력
user_input = input("정수 입력>")
user = int(user_input)

if user%2 == 0:
    print("짝수입니다")
elif user%2 == 1:
    print("홀수입니다")
else :
    print("잘못된 입력")



# 현재 시간 모듈인 datetime을 불러와서 년, 월, 일, 시, 분, 초 출력
import datetime

now = datetime.datetime.now()

print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour, "시")
print(now.minute,"분")
print(now.second,"초")



# 리스트의 숫자들의 자릿수를 출력하는 프로그램
numbers = [273,103,5,32,65,9,72,800,99]

for num in numbers:
    if num/100>=1:
        print(num,"3자리")
    elif num/10>=1:
        print(num,"2자리")
    elif num/1>=1:
        print(num,"1자리")




# 첫번째 숫자와 두번째 숫자를 입력받아 비교하고 출력하는 프로그램
a = float(input("> 1번째 숫자 : "))
b = float(input("> 2번째 숫자 : "))
print()

if a>b:
    print("처음 입력했던 {}가 {}보다 큽니다".format(a,b))
if b>a:
    print("두 번째로 입력했던 {}가 {}보다 큽니다".format(b,a))


#page 268 도전문제 1
numbers = [1,2,3,4,1,2,3,1,4,1,2,3]
one_count = 0
two_count = 0
three_count =0
four_count = 0
for num in numbers:
    if num == 1:
        one_count += 1
    if num == 2:
        two_count += 1
    if num == 3:
        three_count += 1
    if num == 4:
        four_count += 1
print("[1,2,3,4,1,2,3,1,4,1,2,3]에서")
print("사용된 숫자의 종류는 4개 입니다")
print("참고 - 1:{}, 2:{}, 3:{}, 4:{}".format(one_count,two_count, three_count, four_count))



#1,4,7 / 2,5,8 / 3,6,9
numbers = [1,2,3,4,5,6,7,8,9]
output = [[], [], []]
#output = [numbers[0:8:3], numbers[1:9:3], numbers[2:10:3]]

for number in numbers:
    output[(number+2)%3].append(number) #???

print(output)


# 태어난 해를 입력받아 해당 띠를 출력하는 프로그램
str_input = int(input("태어난 해를 입력해 주세요>>"))

if user_input % 12 == 0:
    print("원숭이 띠입니다")
elif user_input % 12 == 1:
    print("닭 띠입니다")
elif user_input % 12 == 2:
    print ("개 띠입니다")
elif user_input % 12 == 3:
    print("돼지 띠입니다")
elif user_input % 12 == 4:
    print("쥐 띠입니다")
elif user_input % 12 == 5:
    print("소 띠입니다")
elif user_input % 12 == 6:
    print("범 띠입니다")
elif user_input % 12 == 7:
    print("토기 띠입니다")
elif user_input % 12 == 8:
    print("용 띠입니다")
elif user_input % 12 == 9:
    print("뱀 띠입니다")
elif user_input % 12 == 10:
    print("말 띠입니다")
elif user_input % 12 == 11:
    print("양 띠입니다")
else:
    print("")



# 간단한 대화 프로그램
import datetime
now = datetime.datetime.now()

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

user_input = input("입력: ")
if user_input == "안녕" or user_input == "안녕하세요":
    print("안녕하세요")
elif user_input == "지금 몇시야?" or user_input == "지금 몇시에요?":
    print("현재 시각은 {}시 {}분입니다".format(hour,minute))
elif user_input == "오늘 날짜" or user_input == "오늘날짜":
    print("{}년 {}월 {}일 입니다".format(year,month,day))
else:
    print(user_input)

# case 2
user_input = input("입력: ")
if user_input == "안녕":
    print("안녕하세요.")
elif user_input == "안녕하세요":
    print("안녕하세요.")
elif user_input == "지금 몇시야?":
    print("지금은 15시 입니다")
elif user_input == "지금 몇시에요?":
    print("지금은 15시 입니다")
else:
    print(user_input)



# 정수를 입력받아 2,3,4,5로 나누어지는 숫자인지 구분하는 프로그램
user_input = int(input("정수를 입력해주세요"))

if user_input % 2 == 0:
    print(user_input,"은 2로 나누어 떨어지는 숫자입니다.")
elif user_input % 2 != 0:
    print(user_input,"은 2로 나누어 떨어지는 숫자가 아닙니다.")

if user_input % 3 == 0:
    print(user_input,"은 3으로 나누어 떨어지는 숫자입니다.")
elif user_input % 3 != 0:
    print(user_input,"은 3으로 나누어 떨어지는 숫자가 아닙니다.")

if user_input % 4 == 0:
    print(user_input,"은 4로 나누어 떨어지는 숫자입니다.")
elif user_input % 4 != 0:
    print(user_input,"은 4로 나누어 떨어지는 숫자가 아닙니다.")

if user_input % 5 == 0:
    print(user_input,"은 5로 나누어 떨어지는 숫자입니다.")
elif user_input % 5 != 0:
    print(user_input,"은 5로 나누어 떨어지는 숫자가 아닙니다.")


#error
count = 0
numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers)//2):
    j = numbers[0:len(numbers)-1:2]
    print(f"i = {i}, j = {j[count]}")
    count +=1
    #numbers[j] = numbers[j] **2
#print(numbers)

#case 2
numbers = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(numbers)//2):
    for j in range(1, len(numbers),2):
        print(f"i = {i}, j = {j}")
    numbers[j] = numbers[j] **2

print(numbers)



# 염기의 개수를 구하는 프로그램
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




# 염기의 개수를 구하는 프로그램
count_cta = 0
count_caa = 0
count_tgt = 0
count_cag = 0
count_tat = 0
count_acc = 0
count_cat = 0
count_tgc = 0
count_cta = 0
count_caa = 0
count_tgt = 0
count_cag = 0

user_input = input("염기 서열을 입력해주세요: ")
for i in user_input:
    if "cta" in user_input:
        count_cta += 1
print("a의 개수: {}".format(count_a))
print("t의 개수: {}".format(count_t))
print("g의 개수: {}".format(count_g))
print("c의 개수: {}".format(count_c))
print("a의 개수: {}".format(count_a))
print("t의 개수: {}".format(count_t))
print("g의 개수: {}".format(count_g))
print("c의 개수: {}".format(count_c))
print("a의 개수: {}".format(count_a))
print("t의 개수: {}".format(count_t))
print("g의 개수: {}".format(count_g))
print("c의 개수: {}".format(count_c))


#dictionary 예제
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

value = dictionary.get("aaaa")
print("값 :", value)
"""
"""

# 별 피라미드
for i in range(1,10):
    for j in range(0,i,-1):
        print("")
    for k in range(0, 2*1-1):    
        print("*"*i)


for i in range(1,10):
    for j in range(9, i, -1):
        print(""*j)
    print("*"*i)

for i in range(1, 15):
    for j in range(14, 0, -1):
        print(" ", end="")
    for k in range(0, i, 1):
        print("*", end="")
    print("\n")



# 별찍기
for i in range(1, 10):
    print("*"*i)



# 별트리찍기
output =""
for i in range(1, 15):
    for j in range(14, i, -1):
        output += ' '
    for k in range(0,2*i-1):
        output += '*'
    output += '\n'
print(output)

# case 2
for i in range(1, 15):
    for j in range(15-i):
        print(" ", end="") # end - 다음 출력 값과 이어지게 함
    for k in range(1, i*2, 1):
        print("*", end="")
    print("")



# 딕셔너리 출력하는 프로그램
pets = [
    {"name":"구름", "age":5},
    {"name":"초코", "age":3},
    {"name":"아지", "age":1},
    {"name":"호랑이", "age":1}
]

print("# 우리 동네 애완동물들")
for pet in pets:
    print("{} {}살".format(pet["name"], pet["age"]))



# get함수 사용하는 프로그램
product = {
    "name":"하리보",
    "type":"젤리"
}

if "price" in product:    # == if product.get("price") != None:
    print(product["price"])
else :
    print("키를 찾을 수 없습니다")



# 리스트 안에 딕셔너리를 출력하는 프로그램
product = [
    {"제품명" : "건망고 슬라이스",
    "가격":5000,
    "원산지":"동남아"},
    {"제품명" : "호두",
    "가격":3000,
    "원산지":"태국"}
]

for abc in product:
    for key in abc:
        print(key,end="")
        print(abc[key])
        #print("\n")
    print("-"*10)



# 도전문제
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



# 각리스트 안의 있는 값들을 character 딕셔너리 안에 키와 값으로 집어넣고 출력하는 프로그램
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

#빈칸
for key in key_list:
    for value in value_list:
        character[key] = character[value]
#

print(character)


numbers = [1,2,3,4,5,6,7,8,9,2,1,5,1,5,5,5,7,1,4,6,1,8,6,4,4,9,4,5,6,4,7,1,1,2,2,6]

counter = {}
for num in numbers:
    if num in counter:
        counter[num] = counter[num]+1
    else:
        counter[num] = 1

print(numbers,"에서 사용된 숫자의 종류는 ",len(counter.keys()),"개입니다")
print("참고 : ",counter)



# 염기서열을 입력받고 갯수를 출력하는 프로그램
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



#sum_all 함수에 매개변수 2개를 입력하여 전체 값을 더하고 리턴해서 출력하는 프로그램
def sum_all(start, end):
    output=0

    for i in range(start, end+1):
        output+=i
    return output

print("0 to 100 : ", sum_all(0,100))
print("0 to 1000 : ", sum_all(0,1000))
print("50 to 100 : ", sum_all(50,100))
print("500 to 1000 : ", sum_all(500,1000))


"""
def mul(*value):
    num_sum = 1
    for i in value:
        num_sum *= i
    return num_sum

print(mul(5,7,9,10))
