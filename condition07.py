#성적 입력시 평가를 출력해주는 프로그램

user_input = float(input("성적입력>> "))

if user_input == 4.5:
    print("신")
elif 4.2 <= user_input:
    print("교수님의 사랑")
elif 3.5 <= user_input:
    print("현 체제의 수호자")
elif 2.8 <= user_input:
    print("일반인")
elif 2.3 <= user_input:
    print("소시민")
elif 1.75 <= user_input:
    print("오락문화의 선구자")
elif 1.0 <= user_input:
    print("불가촉천민")
elif 0.5 <= user_input:
    print("자벌레")
elif 0 < user_input:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗") 

