import math
pi = 3.141592
user_input = input("구의 반지름을 입력해주세요 : ")     # 구의 반지름 입력
r = int(user_input)     # 입력받은 반지름 int 타입으로 변환
bu = 4/3*pi*pow(r,3)     # 구의 부피 구하는 공식
nul = 4*pi*pow(r,2)      #구의 겉넓이 구하는 공식
print("= 구의 부피는 ",bu,"입니다.")    # 출력
print("= 구의 겉넓이는 ",nul,"입니다")    # 출력