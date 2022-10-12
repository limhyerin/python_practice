# 피타고라스의 정리(page153)

user_input1 = input("밑변의 길이를 입력해주세요 : ")     # 밑변 입력
user_input2 = input("높이의 길이를 입력해주세요 : ")     # 높이 입력

b = float(user_input1)     # 입력받은 밑변의 길이 float로 변환
a = float(user_input2)     # 입력받은 높이의 길이 float로 변환

pita = pow(a,2)+pow(b,2)     # 피타고라스 공식
c = pita**(0.5)     # 빗변의 길이 구하는 공식(제곱근 구하기)

print("= 빗변의 길이는",c,"입니다.")     # 출력
